import logging
import utils
from dataclasses import dataclass
from state import State
from theme import theme_set

logger = logging.getLogger('therefor-project')
logger.setLevel(logging.INFO)


def launch(intent):
    return {
        'text_keys': f'{utils.get_skill_name()}、へようこそ！'
                     '今から私が「AはBだ」、とお題を出しますので、10秒で平和な結末に落としてください。'
                     '例を聞きますか？',
        'next_state': State.EXAMPLE
        }


def example(intent):
    text_keys = []
    if intent == 'AMAZON.YesIntent':
        text_keys.append('たとえば…')
        text_keys.append(
            '<voice name="Mizuki">あなたは私の太陽です。いつも私を照らしてくれます。</voice>')

    for text_key in ['ふふふ、',
                     'ではやってみましょう。',
                     f'{theme_set.a}は{theme_set.b}だ。',
                     'ﾁｯﾁｯﾁｯ、',
                     '3、2、1、',
                     'うまく落とせましたか？']:
        text_keys.append(text_key)

    return {
        'text_keys': text_keys,
        'next_state': State.SAVE_THEME
        }


def save_theme(intent):
    return {
        'text_keys': ['終了するには、おわりと言ってください。',
                      'さぁ、どんどん行きますよ。',
                      f'{theme_set.a}は{theme_set.b}だ。',
                      'ﾁｯﾁｯﾁｯ、',
                      '3、2、1、',
                      'うまく落とせましたか？'],
        'next_state': State.SAVE_THEME
        }


@dataclass
class Parameter:
    intent: str
    state: str


class Backend:
    @classmethod
    def main(cls, parameter: dict):
        param = Parameter(
            parameter.get('intent'),
            parameter.get('state')
            )
        if param.state == State.LAUNCH:
            return launch(param.intent)
        elif param.state == State.EXAMPLE:
            return example(param.intent)
        elif param.state == State.SAVE_THEME:
            return save_theme(param.intent)
        return {'text_keys': 'ステートが存在しません'}
