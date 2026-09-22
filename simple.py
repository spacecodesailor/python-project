#!/usr/bin/env python3 
import time 
import socket 
from http.server import HTTPServer, BaseHTTPRequestHandler 
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        if self.path == '/healthz' or self.path == '/readiness': 
            self.send_response(200) 
            self.send_header('Content-type', 'text/plain') 
            self.end_headers() 
            self.wfile.write(b"OK") 
        else: 
            hostname = socket.gethostname() 
            current_time = time.strftime("%Y-%m-%d %H:%M:%S") 
            response_text = f"Host: {hostname} | Time: {current_time}\n" 
            self.send_response(200) 
            self.send_header('Content-type', 'text/plain') 
            self.end_headers() 
            self.wfile.write(response_text.encode('utf-8')) 

def run_server(): 
    server_address = ('', 8080) 
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler) 
    print("Démarrage du serveur sur le port 8080...") 
    httpd.serve_forever() 
if __name__ == '__main__': 
    run_server()
