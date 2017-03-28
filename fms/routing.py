from channels.routing import include

from chat.routing import routing

routing = [
    include(routing, path=r"^/chat"),
]