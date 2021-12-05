import sys


def main(args):

    with open(
        "test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt"
    ) as f:
        points = {}

        def updatePoint(coord):
            point = points.get(coord)

            if point is not None:
                points[coord] = point + 1
            else:
                points[coord] = 1

        for line in f.readlines():
            [start, end] = line.strip("\n").split("->")

            x_1, y_1 = map(lambda x: int(x), start.split(","))
            x_2, y_2 = map(lambda x: int(x), end.split(","))

            # check if horizontal
            # if x_1 == x_2:
            #     for y in range(min(y_1, y_2), max(y_1, y_2) + 1):
            #         updatePoint((x_1, y))
            # check if vertical
            # elif y_1 == y_2:
            #     for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
            #         updatePoint((x, y_1))
            # handle diagonal
            # else:
            #   x_step = 1 if x_2 > x_1 else -1

            #   y = y_1
            #   y_step = 1 if y_2 > y_1 else -1

            #   for x in range(x_1, x_2 + x_step, x_step):
            #       updatePoint((x, y))
            #       y += y_step

            # check for vertical lines since m doesn't exist
            if x_1 == x_2:
                for y in range(min(y_1, y_2), max(y_1, y_2) + 1):
                    updatePoint((x_1, y))
            else:  # interpolate line
                m = (y_2 - y_1) / (x_2 - x_1)  # gradient of the line
                c = (m * (-x_1)) + y_1  # y intercept

                for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
                    y = round((m * x) + c)  # y = mx + c
                    updatePoint((x, y))

        count = 0

        for point in points.values():
            if point > 1:
                count += 1

        print(count)


if __name__ == "__main__":
    main(sys.argv)
