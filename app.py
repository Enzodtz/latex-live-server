import socketio
import os


def build_app(sio_app: socketio.WSGIApp, cmd_dir: str, latex_filename: str):
    pdf_filename = ".".join(latex_filename.split(".")[:-1]) + ".pdf"
    pdf_path = os.path.join(cmd_dir, pdf_filename)
    base_path = os.path.dirname(os.path.realpath(__file__))
    html_path = os.path.join(base_path, "index_html")

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
        data = open(html_path).read()
        return [data]

    return app
