"""Tests for hello."""
import pytest
from hello.hello import Hello

class TestHello:
    """Tests for Hello."""
    # pylint: disable=unused-argument
    @staticmethod
    @pytest.mark.parametrize(
        'target, expect', [
            ('world', 'Hello world\n'),
            ('U.S.A', 'Hello U.S.A\n'),
        ])
    def test_hello(capsys, target, expect):
        """Constructor should leave to load yaml file."""
        Hello.say_hello(target)
        captured = capsys.readouterr()
        assert captured.out == expect
