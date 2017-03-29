import json

class Message(dict):
    def __init__(self, text=None, username=None, **kwargs):
        defaults = {'type': 'message'}
        if text:
            defaults['text'] = text
        if username:
            defaults['user'] = username
        defaults.update(kwargs)
        self['text'] = json.dumps(defaults)


class InfoMessage(Message):
    def __init__(self, *args, **kwargs):
        kwargs['type'] = 'info'
        super(InfoMessage, self).__init__(*args, **kwargs)


class SystemMessage(Message):
    def __init__(self, *args, **kwargs):
        kwargs['type'] = 'systems'
        kwargs['username'] = 'systemssa'
        super(SystemMessage, self).__init__(*args, **kwargs)


def message(*args, **kwargs):
    return Message(*args, **kwargs)


def info(*args, **kwargs):
    return InfoMessage(*args, **kwargs)


def system(*args, **kwargs):
    return SystemMessage(*args, **kwargs)
