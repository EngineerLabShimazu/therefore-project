import os
import csv
import random
from typing import Sequence
from dataclasses import dataclass
# from theme import Theme


@dataclass(frozen=True)
class Theme:
    a: int = 0
    b: int = 1


def get_row(row_num: int) -> Sequence[str]:
    with open(
            os.path.join(
                os.getcwd(), 'lambda', 'assets', 'Alexa笑点 - お題.csv')
            ) as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        # TODO if out of index: return
        return [row[row_num] for row in spam_reader]


def select_theme(theme: int) -> str:
    return random.choice(get_row(theme))


def select_themes() -> Sequence[str]:
    return [select_theme(Theme.a), select_theme(Theme.b)]


def get_speech_text(_, text_keys):
    if isinstance(text_keys, str):
        text_keys = [text_keys]
    # text keys list to response text
    speech_texts = [_.get(text_key, text_key)
                    for text_key in text_keys]
    separated_value = _.get('SEPARATED_VALUE', '.')
    return f'{separated_value}'.join(speech_texts)
