import os
import csv
from typing import Sequence


def read_file(file_name: str, full_path: str = '') -> Sequence[Sequence[str]]:
    open_file_path = full_path if full_path \
        else os.path.join(os.getcwd(), file_name)
    with open(open_file_path) as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        return [row for row in spam_reader]


def get_speech_text(_, text_keys):
    if isinstance(text_keys, str):
        text_keys = [text_keys]
    # text keys list to response text
    speech_texts = [_.get(text_key, text_key)
                    for text_key in text_keys]
    separated_value = _.get('SEPARATED_VALUE', '.')
    return f'{separated_value}'.join(speech_texts)
