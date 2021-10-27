# Sourced from https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

def empty() -> list[list[int]]:
    return [[0 for i in range(100)] for j in range(100)]


def replace_at(grid: list[list[int]], subgrid: list[list[int]], start_x: int, start_y: int) -> None:
    end_x = start_x + len(subgrid[0])

    for i, row in enumerate(subgrid):
        grid[start_y + i][start_x:end_x] = row


def get_example(name: str, grid_width: int, grid_height: int) -> list[list[int]]:
    midgrid = lambda sub, w=grid_width, h=grid_height: (sub, w // 2 - len(sub[0]) // 2, h // 2 - len(sub) // 2)
    out: list[list[int]] = empty()
    match name.lower().strip():
        case "blinker":
            subgrid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        case "r-pentomino":
            subgrid = [[0, 1, 1], [1, 1, 0], [0, 1, 0]]
        case "diehard":
            subgrid = [[0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0,], [0, 1, 0, 0, 0, 1, 1, 1]]
        case _:
            raise ValueError(f"Couldn't find example {name}")
    replace_at(out, *midgrid(subgrid))
    return out
