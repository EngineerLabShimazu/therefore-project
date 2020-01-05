import random
from typing import Sequence
from dataclasses import dataclass
from utils import read_file


@dataclass(frozen=True)
class Theme:
    a: int = 0
    b: int = 1


class ThemesTable:
    a_list: Sequence[str]
    b_list: Sequence[str]

    def __init__(self):
        _themes_table = read_file('Alexa笑点 - お題.csv')
        self.a_list = [_themes[Theme.a] for _themes in _themes_table]
        self.b_list = [_themes[Theme.b] for _themes in _themes_table]

    @staticmethod
    def _select_theme(themes) -> str:
        return random.choice(themes)

    def select_themes(self) -> Sequence[str]:
        return [self._select_theme(self.a_list),
                self._select_theme(self.b_list)]


global_themes_table = ThemesTable()


@dataclass
class Themes:
    a: str
    b: str

    def __init__(self):
        _themes = global_themes_table.select_themes()
        self.a = _themes[Theme.a]
        self.b = _themes[Theme.b]


global_themes = Themes()
