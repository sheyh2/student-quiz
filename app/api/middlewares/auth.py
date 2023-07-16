from werkzeug.wrappers import Request, Response, ResponseStream


class Authenticate:
    def __init__(self, app):
        self.app = app

    # def __call__(self, eviron, start_response):
    #     pass
        # request = Request(eviron)
        # print("middleware")

