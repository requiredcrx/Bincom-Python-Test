# QUE2: Which color is mostly worn throughout the week?

from data import get_color_frequencies


# func to get most worn color
def get_most_worn_color():
    color_freq = get_color_frequencies()
    return color_freq.most_common(1)[0][0]


print(f"The most worn color is {get_most_worn_color()}")
