# latex-live-server

View latex changes live on browser.

### Installing

Install requirements:
```
pip install -r requirements.txt
```

Then you can run `main.py` to start the live server. My recommendation is to set an alias so you can call it globally. Alternativelly, a PR to convert it to a python module would be appreciated.

### Running

When a change is detected on the specified dir (default to current), Latex Live Server will automatically recompile the latex files into a pdf and refresh the browser tab to the new version. It also includes a lot of configuration.

#### Starting the server
```sh
python3 main.py
```
This will start the Live Server on http://localhost:8000 and listen for changes in the current directory and recompile the pdf with `pdflatex` starting on `document.tex` file and producing `document.pdf` output on the same dir. Currently both in an out files need to have the same name.

#### Settings

See `--help` for configurations and more.

```sh
usage: Latex Live Server [-h] [-w WATCH] [-c CMD] [-d CMD_DIR] [-f LATEX_FILENAME] [-a CMD_ARGS] [-o CMD_OVERRIDE]

Latex PDF visualizer that recompiles and refreshes when source is altered.

optional arguments:
  -h, --help            show this help message and exit
  -w WATCH, --watch WATCH
                        Directory or file to be watched for changes
  -c CMD, --cmd CMD     Command to run on refresh
  -d CMD_DIR, --cmd_dir CMD_DIR
                        Directory to run command
  -f LATEX_FILENAME, --latex-filename LATEX_FILENAME
                        Filename to run command on
  -a CMD_ARGS, --cmd_args CMD_ARGS
                        Args to run command with
  -o CMD_OVERRIDE, --cmd_override CMD_OVERRIDE
                        Override all cmd and args on refresh
```
