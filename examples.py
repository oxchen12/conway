# Examples sourced from https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


def replace_at(grid: list[list[int]], subgrid: list[list[int]], start_x: int, start_y: int) -> None:
    end_x = start_x + len(subgrid[0])

    for i, row in enumerate(subgrid):
        grid[start_y + i][start_x:end_x] = row


def get_example(name: str, grid_width: int, grid_height: int) -> list[list[int]]:
    out: list[list[int]] = [[0 for i in range(grid_width)] for j in range(grid_height)]
    match name.lower().strip():
        # oscillators
        case "blinker":
            subgrid = [[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]]
        case "pulsar":
            subgrid = [[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]]
        case "pentadecathalon":
            subgrid = [[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]]
        # Methuselahs
        case "r-pentomino":
            subgrid = [[0, 1, 1],
                       [1, 1, 0],
                       [0, 1, 0]]
        case "diehard":
            subgrid = [[0, 0, 0, 0, 0, 0, 1, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 1, 1, 1]]
        case "acorn":
            subgrid = [[0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0],
                       [1, 1, 0, 0, 1, 1, 1]]
        case "stones":
            subgrid = [[1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1],
                       [0, 1, 1, 0, 1],
                       [1, 0, 1, 0, 1]]
        # no example exists
        case _:
            raise ValueError(f"Couldn't find example {name}")
    replace_at(out, subgrid, grid_width // 2 - len(subgrid) // 2, grid_height // 2 - len(subgrid) // 2)
    return out
