from hypothesis import given
from hypothesis.strategies import text

from hello import contract


@given(text())
def test_hello_contract(s):

    assert contract.say_hello(s) == f"Hello {s}"
