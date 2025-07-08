import os
from src.data_simulator import generate_temperature_data

def test_temperature_data_generation(tmp_path):
    temp_file = tmp_path / "test_temperature.csv"
    original_path = "data/temperature_log.csv"

    generate_temperature_data(num_records=10)

    assert os.path.exists(original_path)

    with open(original_path, "r") as f:
        lines = f.readlines()
        assert len(lines) > 1