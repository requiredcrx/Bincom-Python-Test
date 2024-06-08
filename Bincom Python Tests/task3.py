# QUE3: Which color is the median?

from data import colors


def get_median_color():
    sorted_colors = sorted(colors)  # this line sorts the colors, collecting like terms
    n = len(sorted_colors)
    if n % 2 == 0:
        return sorted_colors[n // 2 - 1]
    else:
        return sorted_colors[n // 2]


print(f"The median color is {get_median_color()}")





