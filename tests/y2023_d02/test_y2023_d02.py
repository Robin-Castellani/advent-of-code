from pathlib import Path
from y2023_d02.main import play_game, Config

import pytest


@pytest.fixture
def input_silver():
    with open(Path(__file__).parent / "input_silver.txt", "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def configuration_silver():
    return Config(12, 13, 14)


def test_silver(input_silver, configuration_silver):
    expected_id_sum = 8

    id_sum = play_game(input_silver, configuration_silver)

    assert id_sum == expected_id_sum
