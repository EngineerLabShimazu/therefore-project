from dataclasses import dataclass
import logging
from state import State

logger = logging.getLogger('heart-yell')
logger.setLevel(logging.INFO)


def launch(intent):
    return {
        'text_keys': 'Alexa笑点へようこそ！'
                     '今から私が「AはB」といいますので、10秒で平和な結末に落としてください。'
                     '例を聞きますか？',
        'next_state': State.EXAMPLE
        }


def example(intent):
    return {
        'text_keys': 'たとえば…あなたは私の太陽です。'
                     'いつも私を照らしてくれます。'
                     'ふふふ、'
                     'ではやってみましょう。'
                     'AはBだ。'
                     'ﾁｯﾁｯﾁｯ、'
                     '3、2、1、'
                     'さぁ、うまく落とせましたか？'
                     'このネタを記録しておきたいですか？',
        'next_state': State.SAVE_THEME
        }


def save_theme(intent):
    return {
        'text_keys': '記録しました。'
                     'どんどん行きますよ。'
                     '終了するには、終了と言ってください。'
                     'では次です。'
                     'AはBだ。'
                     'ﾁｯﾁｯﾁｯ、'
                     '3、2、1、'
                     'さぁ、うまく落とせましたか？'
                     'このネタを記録しておきたいですか？',
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
