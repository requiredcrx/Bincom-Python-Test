# QUE4: BONUS Get the variance of the colors?

from data import get_color_frequencies
import statistics


def get_color_variance():
    color_freq = get_color_frequencies()
    frequencies = list(color_freq.values())
    return round(statistics.variance(frequencies), 1)  # rounded to the nearest decimal


print(f"The variance of the color is {get_color_variance()}")
