import pytest

from foo.mod1 import fn1


def test_fn1(capsys):
    fn1()
    out, err = capsys.readouterr()
    assert "fn1" in out
