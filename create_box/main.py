"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    n = 0
    for n in range(height):
        for n in range(width):
            box += character
        box += '\n'
    return box
    
def create_border_box(height, width, character):
    box = ''
    n = 0
    space = ' ' * (width-2)
    for n in range(height):
        if n == 0 or n == (height-1):
            for n in range(width):
                box += character
            box += '\n'
        else:
            box += (character + space + character)
            box += '\n'
    return box


if __name__ == '__main__':
    create_box(3, 4, '*')
    create_border_box(20, 20, '*')
