for _ in range(int(input())):
    n = input()

    try:
        n = float(n)

        if (
            (str(n).startswith("+") or str(n).startswith("-") or str(n).startswith("."))
            and str(n).count(".") == 1
            and str(n).count("+") <= 1
            and str(n).count("-") <= 1
        ):
            print(True)

        else:
            print(False)

    except ValueError:
        print(False)
