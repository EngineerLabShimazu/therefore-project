from dataclasses import dataclass


@dataclass
class State:
    LAUNCH = 'launch'
    EXAMPLE = 'example'
    SAVE_THEME = 'save_theme'
    HELP = 'help'

    @staticmethod
    def get_state_from_session(handler_input):
        return handler_input.attributes_manager.session_attributes.get(
            'state')

    @staticmethod
    def set_state_to_session(handler_input, state):
        handler_input.attributes_manager.session_attributes[
            'state'] = state
