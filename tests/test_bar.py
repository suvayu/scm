from bar.moda import fna
from bar.modb import fnb


def test_fna(capsys):
    fna()
    out, err = capsys.readouterr()
    assert "fna" in out


def test_fnb(capsys):
    fnb()
    out, err = capsys.readouterr()
    assert "fnb" in out
