import json


class JsonReader:

    @staticmethod
    def read_body(request):
        '''returns a dict from the body of request'''

        data = dict()

        try:
            body = request.body
            data = JsonReader.bytes_to_dict(body)
        except Exception as exc:
            if isinstance(request.data, dict):
                data = request.data
            elif isinstance(request.data, str):
                data = JsonReader.str_to_dict(request.data)

        return data

    @staticmethod
    def str_to_dict(s: str):
        dict = json.loads(s)
        return dict

    @staticmethod
    def dict_to_str(d: dict):
        str = json.dumps(d)
        return str

    @staticmethod
    def bytes_to_dict(b: bytes):
        str = b.decode("utf-8")
        dict = JsonReader.str_to_dict(str)
        return dict
