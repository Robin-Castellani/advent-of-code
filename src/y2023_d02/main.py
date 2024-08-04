import click
from collections import namedtuple

Config = namedtuple("Configuration", "red, green, blue")
Game = namedtuple("Game", "id, red, green, blue")


def play_game(input_game: str, config: Config) -> int:
    records = input_game.split("\n")
    games_ids = {}
    for game in records:
        game_id, game_sets = game.split(":")
        game_id = int(game_id.split(" ")[-1])
        game_sets = [gs.strip() for gs in game_sets.split(";")]

        # instantiate a Game with the max number of cubes set to 0
        # these will be update for each game set
        games_ids[game_id] = {"red": 0, "green": 0, "blue": 0}

        for game_set in game_sets:
            for cube_set in game_set.split(", "):
                number, color = cube_set.split(" ")

                if games_ids[game_id][color] < int(number):
                    games_ids[game_id][color] = int(number)

        # is the game possible when compared with the configuration?
        if (
            games_ids[game_id]["red"] > config.red
            or games_ids[game_id]["green"] > config.green
            or games_ids[game_id]["blue"] > config.blue
        ):
            games_ids.pop(game_id)
    # sum up the ids of all the possible games
    ids_sum = sum(games_ids.keys())
    return ids_sum


@click.command()
def cli():
    click.echo("Advent of Code - Day 2 🎄")
