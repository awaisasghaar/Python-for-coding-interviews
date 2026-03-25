import pytest
from functions import main

def test_grade_A(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "90")
    main()
    assert "Grade A" in capsys.readouterr().out