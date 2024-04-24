import eventlet
import logging
import argparse

from sio import sio, sio_app
from monitor import monitor_changes
from app import build_app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Latex Live Server",
        description="Latex PDF visualizer that recompiles and refreshes when source is altered.",
    )
    parser.add_argument(
        "-w",
        "--watch",
        default=".",
        help="Directory or file to be watched for changes",
    )
    parser.add_argument(
        "-c",
        "--cmd",
        default="pdflatex",
        help="Command to run on refresh",
    )
    parser.add_argument(
        "-d",
        "--cmd_dir",
        default=".",
        help="Directory to run command",
    )
    parser.add_argument(
        "-f",
        "--latex-filename",
        default="document.tex",
        help="Filename to run command on",
    )
    parser.add_argument(
        "-a",
        "--cmd_args",
        default="",
        help="Args to run command with",
    )
    parser.add_argument(
        "-o",
        "--cmd_override",
        default=None,
        help="Override all cmd and args on refresh",
    )

    args = parser.parse_args()

    sio.start_background_task(
        monitor_changes,
        sio,
        args.watch,
        args.cmd_dir,
        args.cmd,
        args.latex_filename,
        args.cmd_args,
        args.cmd_override,
    )

    logging.info("Live server started. View your file in http://localhost:8000/")

    eventlet.wsgi.server(
        eventlet.listen(("", 8000)),
        build_app(sio_app, args.cmd_dir, args.latex_filename),
        log_output=False,
    )
