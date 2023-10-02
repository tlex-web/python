def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count


def validate(s: str) -> list[bool]:
    v1 = [c.isalnum() for c in s]
    v2 = [c.isalpha() for c in s]
    v3 = [c.isdigit() for c in s]
    v4 = [c.islower() for c in s]
    v5 = [c.isupper() for c in s]

    return [any(v1), any(v2), any(v3), any(v4), any(v5)]


for _ in range(int(input())):
    s = input()
    print(validate(s))


def print_rangoli(size):
    # your code goes here
    import string

    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print("\n".join(L[:0:-1] + L))
