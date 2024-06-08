# QUE1: Which color of shirt is the mean color?

from data import get_color_frequencies


# A function that finds the mean color
def get_mean_color():
    color_freq = get_color_frequencies()  # getting the frequencies in which each color appears
    total_colors = sum(color_freq.values())  # summing the values of the dict which contains the color and freq
    mean_freq = total_colors / len(color_freq)

    closest_color = min(color_freq, key=lambda x: abs(color_freq[x] - mean_freq))
    return closest_color


print(f"The mean color is {get_mean_color()}")



