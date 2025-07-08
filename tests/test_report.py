import os
import tempfile
import pytest
from src.generate_report import generate_report


def test_generate_valid_report():
    input_file = 'data/temperature_log.csv'
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, 'report.xlsx')
        generate_report(input_file, output_file)
        assert os.path.exists(output_file)

