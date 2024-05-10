from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        return """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
<div class="container">
    <div class="row mt-5">
        <div class="col-6">
            <div class="card bg-primary">
                <div class="card-body text-white">
                    <h3 class="class-title">Контактная информация</h3>
                    <div class="row">
                        <div class="col-6">Москва</div>
                        <div class="col-6">+7 999 888 7766</div>
                        <div class="col-6">Санкт-Петербург</div>
                        <div class="col-6">+7 888 777 6655</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-6">
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Оставьте заявку</h3>
                    <form>
                        <div class="mb-3">
                            <input name="name" type="text" class="form-control" id="exampleInputText1" placeholder="Имя"
                                   aria-describedby="emailHelp">
                        </div>
                        <div class="mb-3">
                            <input name="email" type="email" class="form-control" id="exampleInputEmail1" placeholder="Email"
                                   aria-describedby="emailHelp">
                        </div>
                        <div class="mb-3">
                            <textarea name="message" class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Сообщение"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary ">Отправить</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
