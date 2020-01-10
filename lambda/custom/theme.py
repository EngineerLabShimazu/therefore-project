import random
from abc import ABC
from typing import Sequence
from dataclasses import dataclass
from utils import read_file, Singleton


@dataclass(frozen=True)
class Theme:
    a: int = 0
    b: int = 1


class ThemesTable:
    a_list: Sequence[str]
    b_list: Sequence[str]

    def __init__(self):
        _themes_table = read_file('local')
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
class ThemeSet(Singleton, ABC):
    a: str
    b: str

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()
            cls.init()
        return cls._unique_instance

    @classmethod
    def init(cls):
        _themes = global_themes_table.select_themes()
        cls.a = _themes[Theme.a]
        cls.b = _themes[Theme.b]


theme_set = ThemeSet.get_instance()
