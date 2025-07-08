import pytest
from src.error_diagnosis import batch_diagnose, diagnose_temperature


def test_diagnose_output():
    temps = [15, 25.04, 26, 40.53, 35]
    result = batch_diagnose(temps)

    valid_labels = ["Too Cold", "Too Hot", "Unstable", "Normal"]
    for r in result:
        assert r in valid_labels

def test_diagnose_temperature():
    with pytest.raises(TypeError):
        diagnose_temperature("Type")

def test_batch_diagnose_type():
    with pytest.raises(TypeError):
        batch_diagnose(None)

    with pytest.raises(Exception):
        batch_diagnose(["a", None, 20, 30])