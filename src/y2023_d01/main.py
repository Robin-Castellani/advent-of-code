import re
import click


def read_calibration(input_calibration: str) -> int:
    numbers_names_to_int = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    number_names = tuple(numbers_names_to_int.keys())
    regex = re.compile("\d|" + "|".join(number_names))

    number_names_reversed = [n[::-1] for n in number_names]
    regex_reverse = re.compile("\d|" + "|".join(number_names_reversed))

    calibration_value = 0
    for line in input_calibration.split("\n"):
        matches = regex.findall(line)
        matches_p = tuple(map(lambda n: numbers_names_to_int.get(n, n), matches))

        matches_reverse = regex_reverse.findall(line[::-1])
        matches_reverse_p = tuple(
            map(lambda n: numbers_names_to_int.get(n[::-1], n), matches_reverse)
        )

        number_as_string = matches_p[0] + matches_reverse_p[0]

        calibration_value += int(number_as_string)

    return calibration_value


@click.command
@click.option(
    "--file",
    "-f",
    type=click.types.File(mode="r", encoding="utf-8"),
    required=True,
    help="Calibration file",
)
def cli(file):
    calibration = read_calibration(file.read())

    click.echo(f"Calibration: {calibration}")
