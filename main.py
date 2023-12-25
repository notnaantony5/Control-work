import json


class BaseFileHandler:
    def __init__(self, path: str):
        self._path = path

    def read(self) -> dict:
        with open(self._path, 'r', encoding='utf-8') as f:
            return self._deserialize(f.read())

    def _deserialize(self, data: str) -> dict:
        return {}

    def write(self, data: dict):
        with open(self._path, 'w', encoding='utf-8') as f:
            f.write(self._serialize(data))

    def _serialize(self, data: dict) -> str:
        return ''


class TXTFileHandler(BaseFileHandler):
    def __init__(self, path, key_sep="=", pair_sep="\n"):
        super().__init__(path)
        self.ks = key_sep
        self.ps = pair_sep
    def _serialize(self, data: dict) -> str:
        return self.ps.join(
            f"{key}{self.ks}{value}" for key, value in data.items()
        )
    def _deserialize(self, data: str) -> dict:
        return {
            key: value  # name=Вася
            for key, value in [line.split(self.ks)
                               for line in data.split(self.ps)]
        }


class JSONFileHandler(BaseFileHandler):
    def _serialize(self, data: dict) -> str:
        return json.dumps(data)

    def _deserialize(self, data: str) -> dict:
        return json.loads(data)


student = {"name": "Вася", "group": "P33", "course": 4}
txt_handler = TXTFileHandler("student.txt", '-----', '\n-\n')
txt_handler.write(student)
print(f"TXT: {txt_handler.read()}")
json_handler = JSONFileHandler("student.json")
json_handler.write(student)
print(f"JSON: {json_handler.read()}")
