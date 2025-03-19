class TextFileReader:
    def __init__(self, filename: str):
        self._filename = filename

    def read(self):
        with open(self._filename, "r", encoding="utf-8") as f:
            yield from (row.strip() for row in f if row.strip())
