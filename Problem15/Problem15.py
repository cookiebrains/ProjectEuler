width = 12
paths = []

total_paths = 0
total_traversals = 0


def process_traversals(x, y):
    global total_paths
    global total_traversals
    if x == width and y == width:
        total_paths += 1

    if x < width:
        for sub_traversal in process_traversals(x + 1, y):
            total_traversals += 1
        yield 1
    if y < width:
        for sub_traversal in process_traversals(x, y + 1):
            total_traversals += 1
        yield 1


for t in process_traversals(0, 0):
    total_traversals += 1

print(f'square width: {width}')
print(f'total_traversals: {total_traversals}')
print(f'total_paths: {total_paths}')


def traverse(x, y, path):
    if x == width and y == width:
        paths.append(path)

    if x < width:
        traversal = ((x, y), (x + 1, y))
        path_copy = path.copy()
        path_copy.append(traversal)
        traverse(x + 1, y, path_copy)
    if y < width:
        traversal = ((x, y), (x, y + 1))
        path_copy = path.copy()
        path_copy.append(traversal)
        traverse(x, y + 1, path_copy)


def memory_intensive():
    traverse(0, 0, [])
    # for path in paths:
    #     print(path)
    print(f'Number of paths: {len(paths)}')

# 1 = 2
# 2 = 6
# 3 = 20
# 4 = 70
# 5 = 252
# 6 = 924
# 7 = 3432 
# 8 = 12870
# 9 = 48620
# 10 = 184756
# 11 = 705432
# 12 = 2704156
# 13 = 10400600

# Formula
# Where magic number = Number of traversals for a path
# (magic)! / ((magic / 2)! * (magic / 2)!)
#ok
# Example for 20 x 20 grid
# 40 possible traversals (think 20 right and 20 down)
# 40! / (20! * 20!) = 137846528820
