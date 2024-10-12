class Endpoint:
    def __init__(self, name, url, method, headers, body):
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Endpoint(name={self.name}, url={self.url}, method={self.method}, headers={self.headers}, body={self.body})"