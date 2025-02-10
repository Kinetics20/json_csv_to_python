import csv
import json
from collections import defaultdict
from io import StringIO
from pathlib import Path
from pprint import pprint


class TableDecoder:
    _register: dict[str, int] = {}

    @classmethod
    def __init_subclass__(cls, *, extension, **kwargs):
        super().__init_subclass__(**kwargs)

        cls._register[extension] = cls

    @classmethod
    def create(cls, name):
        decoder_class = cls._register[name]
        return decoder_class()

    @classmethod
    def decoders(cls):
        return list(cls._register.keys())

    @staticmethod
    def decode(text):
        raise NotImplementedError


class JsonTableEncoder(TableDecoder, extension='json'):

    @staticmethod
    def decode(text):
        objs = json.loads(text)
        table = defaultdict(list)
        for obj in objs:
            for k, v in obj.items():
                table[k].append(v)
        return dict(table)


class CsvTableEncoder(TableDecoder, extension='csv'):
    @staticmethod
    def decode(text):
        with StringIO(text) as csv_stream:
            reader = csv.DictReader(csv_stream)
            table = defaultdict(list)
            for row in reader:
                for k, v in row.items():
                    table[k].append(v)
        return dict(table)


def load_table(filepath):
    filepath = Path(filepath)
    text = filepath.read_text()
    extension = filepath.suffix.removeprefix('.')
    decoder = TableDecoder.create(extension)
    table = decoder.decode(text)
    return table


def main():
    print(TableDecoder.decoders())
    table = load_table('table.json')
    pprint(table)


if __name__ == '__main__':
    main()
