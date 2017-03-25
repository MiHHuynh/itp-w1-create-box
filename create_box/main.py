"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    n = 0
    for n in range(height):
        for n in range(width):
            box += character
        box += '\n'
    return box


if __name__ == '__main__':
    create_box(3, 4, '*')
