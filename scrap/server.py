from wsgiref.simple_server import make_server
from scrap import scrapper
import json

def app(environ, start_response):
    signal_list = scrapper("Colombia")
    response = json.dumps(signal_list)
    status = "200 OK"
    headers = [("Content type", "application/json")]
    start_response (status, headers)
    return [bytes(response, "utf-8")]

server = make_server("localhost", 8000, app)
server.handle_request()

#The server handles the client's requests