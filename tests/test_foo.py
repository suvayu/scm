from foo.mod1 import fn1
from foo.mod2 import fn2


def test_fn1(capsys):
    fn1()
    out, err = capsys.readouterr()
    assert "fn1" in out


def test_fn2(capsys):
    fn2()
    out, err = capsys.readouterr()
    assert "fn2" in out
