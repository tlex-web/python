if __name__ == "__main__":
    N = int(input())

    def op(command, l, args):
        cmds = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]

        if command not in cmds:
            return False

        if command == "insert":
            l.insert(int(args[0]), int(args[1]))

        elif command == "print":
            print(l)

        elif command == "remove":
            l.remove(int(args[0]))

        elif command == "append":
            l.append(int(args[0]))

        elif command == "sort":
            l.sort()

        elif command == "pop":
            l.pop()

        elif command == "reverse":
            l.reverse()

        return True

    l = []
    for i in range(N):
        command, *args = input().split()
        op(command, l, args)
