def draw(maze, start, finish, solution):
    solved = maze
    position = {
        "x": start["x"],
        "y": start["y"]
    }
    for i in solution:

        if int(i) == 1:
            position["y"] += 1
        elif int(i) == 2:
            position["y"] -= 1
        elif int(i) == 3:
            position["x"] -= 1
        elif int(i) == 4:
            position["x"] += 1

        if solved[position["x"]][position["y"]] == 0:
            return False

        if position["x"] == finish["x"] and position["y"] == finish["y"]:
            solved[start["x"]][start["y"]] = 3
            solved[position["x"]][position["y"]] = 3
            return solved

        solved[position["x"]][position["y"]] = 3
