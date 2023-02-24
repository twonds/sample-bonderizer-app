import zope

from hello.interface import IGreeterConsumer


@zope.interface.implementer(IGreeterConsumer)
class Greeter:

    def say_hello(name: str) -> str:
        """ """
        print("Call Producer")
