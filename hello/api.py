from bonderizer import Service

# Work towards very simple and almost implicit,
# how do we be simple and explicit?

class Greeter(Service):

    def say_hello(name: str) -> str:
        return "Hello " + name
