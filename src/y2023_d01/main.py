import click


def read_calibration(input_calibration: str) -> int:
    integers_as_strings = tuple(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    calibration_value = 0
    for line in input_calibration.split("\n"):
        number_as_string = ""
        for letter in line:
            if letter in integers_as_strings:
                number_as_string += letter

        if len(number_as_string) == 1:
            number_as_string += number_as_string
        if len(number_as_string) > 2:
            number_as_string = number_as_string[0] + number_as_string[-1]

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
