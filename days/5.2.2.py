from updateData import loadDay # Automatically updates data files
import numpy as np

DAY = 5
TEST = False

data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

MAX: int = 999999999999

class span():
    def __init__(self, start: int, length: int) -> None:
        self.start = start
        self.end = start + length - 1

    def __str__(self) -> str:
        return f'({self.start} -> {self.end})'

class link():
    def __init__(self, source: int, destination: int, length: int) -> None:
        self.difference = destination - source
        self.s_span = span(source, length)
        self.d_span = span(destination, length)

    def convert(self, s: span):
        return span(s.start + self.difference, s.end + self.difference)

    def __str__(self) -> str:
        return f'{self.s_span} -> {self.d_span}'
    
def overlap(s1: span, s2: span):
    start = max(s1.start, s2.start)
    end = min(s1.end, s2.end)

    if end < start:
        return None
    else:
        length = end - start + 1
        return span(start, length)

# overlap_check: list[tuple[span, span]] = [(span(2, 5), span(6, 3)), (span(10, 2), span(8, 3)), (span(1, 10), span(4, 3))]
# for o in overlap_check:
#     print(o[0], o[1], overlap(o[0], o[1]))

lines: list[str] = data.readlines()

seeds = [int(word) for word in lines.pop(0).split()[1:]]
seed_ranges: list[span] = []
for i in range(int(len(seeds)/2)):
    seed_ranges.append(span(seeds[i*2], seeds[i*2+1]))

# for seed_range in seed_ranges:
#     print(seed_range)

levels: dict[str, list[link]] = {}

current_level: str = ""
for line in lines:
        line: str = line.strip()

        if line == "":
            continue

        if '-' in line:
            current_level = line.split()[0]
            levels[current_level] = []
            continue

        numbers = line.split()
        destination = int(numbers[0])
        source = int(numbers[1])
        length = int(numbers[2])

        levels[current_level].append(link(source, destination, length))

for key in list(levels.keys()):
    levels[key].sort(key=lambda x: x.s_span.start)
    l = levels[key].copy()

    start = 0
    end = l[0].s_span.start
    length = end - start
    if length > 0:
        levels[key].append(link(start, start, length))

    for i in range(len(l) - 2):
        start = l[i].s_span.end + 1
        end = l[i+1].s_span.start
        length = end - start
        if length > 0:
            levels[key].append(link(start, start, length))

    start = l[len(l) - 1].s_span.end + 1
    end = MAX
    length = end - start + 1
    if length > 0:
        levels[key].append(link(start, start, length))

# for key in list(levels.keys()):
#     print(key)
#     l = levels[key]
#     for i in range(len(l)):
#         for j in range(len(l)):
#             if i != j:
#                 o = overlap(l[i].s_span, l[j].s_span)
#                 if o is not None:
#                      print(i, j)
    
#     for l in levels[key]:
#         print(" ", l)

# for key in list(levels.keys()):
#     print(key)
#     for l in levels[key]:
#         print(" ", l)

# print(len(levels))

def traverse2min(s: span, level: int = 0) -> int:
    if level >= len(levels):
        return s.start

    min_end: int = MAX

    for l in list(levels.values())[level]:
        o = overlap(s, l.s_span)
        if o is not None:
            new_min = traverse2min(l.convert(o), level+1)
            if new_min < min_end and new_min != 0:
                min_end = new_min

    return min_end

min_location = MAX
for seed_range in seed_ranges:
    print("traversing", seed_range)
    new_location = traverse2min(seed_range)
    if new_location < min_location:
        min_location = new_location

print(min_location)
# 30504694 too low
# 4275623
# 42451649