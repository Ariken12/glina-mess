from Checker import Checker


def main():
    desk = Checker()
    desk.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0],
                  [2, 0, 2, 0, 2, 0, 2, 0],
                  [0, 2, 0, 2, 0, 2, 0, 2],
                  [2, 0, 2, 0, 2, 0, 2, 0]]
    err = desk.move(5, 6, 6, 5, 2)
    print(err)
    for i in desk.board:
        print(i)


if __name__ == "__main__":
    main()
