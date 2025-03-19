import os
import tempfile
import unittest

from src.file_calculation_parser.reader import TextFileReader


class TestTextReader(unittest.TestCase):
    def setUp(self):
        """Create temporary file with some rows to testing"""
        self._temp_filename: str = tempfile.NamedTemporaryFile(delete=False).name
        self._files_rows: list = ["row1", "row2", "row3", " ", "", "\n"]

        with open(self._temp_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self._files_rows))

    def test_can_read_each_rows(self):
        """Check if TextReader read each file and remove empty rows"""
        reader: TextFileReader = TextFileReader(self._temp_filename)
        expected_result: list = [row.strip() for row in self._files_rows if row.strip()]
        self.assertListEqual(list(reader.read()), expected_result)

    def tearDown(self):
        if os.path.exists(self._temp_filename):
            os.remove(self._temp_filename)
