# QUE 5: BONUS if a colour is chosen at random, what is the probability that the color is red?

from data import get_color_frequencies


def get_red_probability():
    color_freq = get_color_frequencies()
    total_colors = sum(color_freq.values())
    red_count = color_freq.get('RED')
    return red_count / total_colors


print(f"The probability of choosing red at ranoom is {get_red_probability():.2%}")