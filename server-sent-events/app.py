import time

from flask import Flask, Response, render_template_string

app = Flask(__name__)

with open("sample.txt") as fp:
    txt = fp.read()


@app.route("/")
def index():
    return render_template_string(
        """
    <!doctype html>
    <html>
      <body>
        <h1>Server-Sent Events Test</h1>
        <div id="events"></div>
        <script>
          const eventSource = new EventSource("/stream");
          eventSource.onmessage = function(event) {
            if (event.data === "[END]") {
              eventSource.close();
              return;
            }
            const el = document.getElementById("events");
            el.innerHTML += event.data;
          };
        </script>
      </body>
    </html>
    """
    )


@app.route("/stream")
def stream():
    def event_stream():
        text = txt
        for ch in text:
            time.sleep(0.01)
            yield f"data: {ch}\n\n"
        yield "data: [END]\n\n"

    return Response(event_stream(), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
