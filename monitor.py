import socketio
import os
import logging
import eventlet
import subprocess
import sys
from typing import List, Optional


def on_change(
    sio: socketio.Server,
    cmd_dir: str,
    cmd: str,
    latex_filename: str,
    cmd_args: List[str],
    cmd_override: Optional[str],
):
    logging.info("Reloading...")
    try:
        output = subprocess.run(
            (
                [cmd_override]
                if cmd_override
                else [cmd, "-interaction", "nonstopmode", latex_filename] + cmd_args
            ),
            cwd=cmd_dir,
            stdout=subprocess.PIPE,
        )

        if output.returncode != 0:
            err = output.stdout.decode()
            err = err.split("!")[1].split("\n")[0].replace(" .", ".")[1:]
            logging.info("Error while compiling latex:")
            logging.info(err)
            return

    except Exception as e:
        logging.info(f"Unexpected error while compiling: {e}")
        sys.exit(1)

    sio.emit("reload")
    logging.info("Reloaded successfully")


def monitor_changes(
    sio: socketio.Server,
    watch_path: str,
    cmd_dir: str,
    cmd: str,
    latex_filename: str,
    cmd_args: List[str],
    cmd_override: Optional[str],
):
    logging.info(f"Observing directory {watch_path}")
    last_update = os.stat(watch_path).st_mtime
    while True:
        new_update = os.stat(watch_path).st_mtime
        eventlet.sleep(0.05)
        if last_update != new_update:
            on_change(
                sio,
                cmd_dir,
                cmd,
                latex_filename,
                cmd_args,
                cmd_override,
            )
            last_update = new_update
