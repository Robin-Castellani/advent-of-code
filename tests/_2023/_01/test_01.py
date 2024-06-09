# from aoc._2023._01.__main__ import read_calibration
from pathlib import Path
from aoc.main_2023_01 import read_calibration

# from aoc.__main__ import read_calibration
import pytest


@pytest.fixture
def input_test():
    with open(Path(__file__).parent / "input_test.txt", "r", encoding="utf-8") as f:
        return f.read()


def test_01(input_test):
    input_calibration = input_test
    expected_calibration = 142

    computed_calibration = read_calibration(input_calibration)

    assert computed_calibration == expected_calibration
