import argparse
import http.server
import socketserver
import logging.config

PORT = 9113

logging.config.fileConfig("log.ini")
logger = logging.getLogger(__file__)

class JSONHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.json'):
            self.send_header('Content-Type', 'application/json')
        return super().end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AI Assist Study - Mock API")
    parser.add_argument('--dir', type=str, help='The directory to serve', default="../data/split-recipes")
    argsv = parser.parse_args()

    handler = lambda *args, **kwargs: JSONHTTPRequestHandler(*args, directory=argsv.dir, **kwargs)
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        logger.info(f"Mock API serving {argsv.dir}, listing on port {PORT}...")
        httpd.serve_forever()
