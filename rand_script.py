from random import randint


def generate_rand_list():
    output_list = []
    for _ in range(15):
        output_list.append(randint(10, 1200))

    return output_list
