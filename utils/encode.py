from json import JSONEncoder

class TaskEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
