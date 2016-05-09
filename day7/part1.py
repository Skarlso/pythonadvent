lines = [l.strip() for l in open("input.txt", "r").readlines()]


def value(expression):
    if expression.isdigit():
        return expression

    rx1 = re.compile(
            r"(\d+) -> (.)")
    rx2 = re.compile(
            r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)")
    rx3 = re.compile(
            r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)")
    operators = []
