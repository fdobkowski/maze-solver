import pygad
from matplotlib import pyplot as plt
import numpy
from draw_solution import draw

Gene_space = [1, 2, 3, 4]
Sol_per_pop = 1000
Num_parents_mating = 1000
Num_generations = 100
Keep_parents = 500
Selection_type = "sss"
Crossover_type = "single_point"
Mutation_Type = "random"
Mutation_Percent_Genes = 5


def solve_maze(maze, start, finish):
    def fitness_func(solution, solution_idx):
        position = {
            "x": start["x"],
            "y": start["y"]
        }

        for i in solution:
            if i == 1:
                if position["y"] < len(maze[0]) - 1 and maze[position["x"]][position["y"] + 1] != 0:
                    position["y"] += 1
                else:
                    break
            elif i == 2:
                if position["y"] > 0 and maze[position["x"]][position["y"] - 1] != 0:
                    position["y"] -= 1
                else:
                    break
            elif i == 3:
                if position["x"] > 0 and maze[position["x"] - 1][position["y"]] != 0:
                    position["x"] -= 1
                else:
                    break
            elif i == 4:
                if position["x"] < len(maze) - 1 and maze[position["x"] + 1][position["y"]] != 0:
                    position["x"] += 1
                else:
                    break

            if position["x"] == finish["x"] and position["y"] == finish["y"]:
                break

        fitness = -(numpy.abs(finish["x"] - position["x"]) + numpy.abs(finish["y"] - position["y"]))

        return fitness

    ga_instance = pygad.GA(gene_space=Gene_space,
                           num_generations=Num_generations,
                           num_parents_mating=Num_parents_mating,
                           fitness_func=fitness_func,
                           sol_per_pop=Sol_per_pop,
                           num_genes=len(maze) ** 2,
                           parent_selection_type=Selection_type,
                           keep_parents=Keep_parents,
                           crossover_type=Crossover_type,
                           mutation_type=Mutation_Type,
                           mutation_percent_genes=Mutation_Percent_Genes,
                           stop_criteria="reach_0")

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    plt.subplots(figsize=(10, 5))

    plt.subplot(1, 2, 1), plt.imshow(maze), plt.title("Maze", fontsize=15, pad=10)

    solved = draw(maze, start, finish, solution)

    if not solved:
        plt.subplot(1, 2, 2)
        plt.text(0.5, 0.5, "No path found", ha='center', va='center', fontsize=25)
        plt.title("Solved", fontsize=20, pad=10)
    else:
        plt.subplot(1, 2, 2)
        plt.imshow(solved)
        plt.title("Solved", fontsize=20, pad=10)

    plt.show()


solve_maze([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             {"x": 1, "y": 1}, {"x": 10, "y": 10})
