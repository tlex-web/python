import re

N = int(input())


def replace_and_or(match):
    if match.group(0) == "&&":
        return "and"
    elif match.group(0) == "||":
        return "or"
    else:
        return match.group(0)


for _ in range(0, N):
    line = input()
    line = re.sub(r"(?<= )&&(?= )", replace_and_or, line)
    line = re.sub(r"(?<= )\|\|(?= )", replace_and_or, line)
    print(line)
