from pathlib import Path
from y2023_d01.main import read_calibration

import pytest


@pytest.fixture
def input_silver():
    with open(Path(__file__).parent / "input_silver.txt", "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def input_gold():
    with open(Path(__file__).parent / "input_gold.txt", "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def input_custom():
    with open(Path(__file__).parent / "input_custom.txt", "r", encoding="utf-8") as f:
        return f.read()


def test_silver(input_silver):
    input_calibration = input_silver
    expected_calibration = 142

    computed_calibration = read_calibration(input_calibration)

    assert computed_calibration == expected_calibration


def test_gold(input_gold):
    input_calibration = input_gold
    expected_calibration = 281

    computed_calibration = read_calibration(input_calibration)

    assert computed_calibration == expected_calibration


def test_custom(input_custom):
    input_calibration = input_custom
    expected_calibration = 98

    computed_calibration = read_calibration(input_calibration)

    assert computed_calibration == expected_calibration
