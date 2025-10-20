import http.server
import socketserver
import json
from .core.llm_provider import LLMProvider

PORT = 8000

gemini_provider = LLMProvider(provider_cli_command="gemini")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="../../ui", **kwargs)

    def do_POST(self):
        if self.path == '/ask':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            prompt = data.get('prompt')
            if prompt:
                response = gemini_provider.ask(prompt)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'response': response}).encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad Request: No prompt provided')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        print("Open http://localhost:8000 in your browser")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
