from api import Greeter


class Greeter(Greeter):

    # XXX - how do we reduce this?
    def say_hello(name: str) -> str:
        return "Hello " + name
