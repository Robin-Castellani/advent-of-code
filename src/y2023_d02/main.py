import click
from collections import namedtuple

Config = namedtuple("Configuration", "red, green, blue")


def play_game(input_game: str, config: Config) -> int:
    return 8


@click.command()
def cli():
    click.echo("Advent of Code - Day 2 🎄")
