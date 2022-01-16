names = sorted([input() for i in range(int(input()))])


def main():
    while True:
        eliminator = names.pop(0)

        if len(names) == 0:
            print('NO RESULT')
            return
        elif len(names) == 1:
            print(names[0])
            return

        for char in set(eliminator):
            for n in range(len(names) - 1, -1, -1):
                if char in names[n]:
                    names.pop(n)

            if len(names) == 0:
                print('NO RESULT')
                return
            elif len(names) == 1:
                print(names[0])
                return


main()