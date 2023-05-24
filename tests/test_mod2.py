import pytest

from foo.mod2 import fn2


def test_fn2(capsys):
    fn2()
    out, err = capsys.readouterr()
    assert "fn2" in out
