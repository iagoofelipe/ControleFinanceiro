from typing import Iterable

def generateStrColumns(columns:Iterable[str], removeId=False):
    if removeId:
        columns = tuple(filter(lambda x: x != 'id', columns))

    return ('`' + '`, `'.join(columns) + '`'), len(columns)

def generateStrParams(len_columns:int):
    return ','.join(['%s' for _ in range(len_columns)])

def generateStrKeyParams(columns:Iterable[str]):
    return ', '.join(map(lambda x: f'`{x}`=%s', columns))