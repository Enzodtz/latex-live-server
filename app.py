import socketio
import os


def build_app(sio_app: socketio.WSGIApp, cmd_dir: str, latex_filename: str):
    pdf_filename = ".".join(latex_filename.split(".")[:-1]) + ".pdf"
    pdf_path = os.path.join(cmd_dir, pdf_filename)

    def app(env, start_response, *args, **kwargs):
        path = env["PATH_INFO"]

        if path == "/document.pdf":
            # Static pdf
            start_response("200 OK", [("Content-Type", "application/pdf")])
            return [open(pdf_path, "rb").read()]
        elif path != "/":
            # Socketio
            return sio_app(env, start_response, *args, **kwargs)

        # Frontend
        start_response("200 OK", [("Content-Type", "text/html")])
        data = open("./index.html").read()
        return [data]

    return app
