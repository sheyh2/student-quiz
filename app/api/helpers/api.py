from typing import Dict


class Api:
    def __init__(self):
        self.status = True
        self.code = 200
        self.message = 'ok'
        self.meta = {}

    def set_status(self, status: bool):
        self.status = status

    def set_code(self, code: int):
        self.code = code

    def set_message(self, message: str):
        self.message = message

    def get_status(self):
        return self.status

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def compose_data(self, data) -> Dict:
        base_data = {
            'status': self.get_status(),
            'code': self.get_code(),
            'message': self.get_message(),
            'content': data,
        }

        return base_data
