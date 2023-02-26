# This will be the definition of a contract from consumer to producer
# It is the shared code to test a contract or ensure consumers and producers
# adhere their contract and do not break it
#
# Test can and should be outside this code but use this code to execute tests
#
#
# The designer or creator should ask three questions about the contract
# What does the contract expect?
# What does the contract guarantee?
# What does the contract maintain?
#
# It should contain the following pieces of information:
# Acceptable and unacceptable input values or types, and their meanings
# Return values or types, and their meanings
# Error and exception condition values or types that can occur, and their meanings
# Side effects
# Preconditions
# Postconditions
# Invariants
# (more rarely) Performance guarantees, e.g. for time or space used
#
from zope.interface import verify

from hello.consumer.greeter import Greeter
from hello.interface import IGreeter


def say_hello(name: str) -> str:
    g = Greeter()
    verify.verifyObject(IGreeter, g)

    message = g.say_hello(name)

    assert type(message) is str

