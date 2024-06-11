
def draw():
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    line = ''
    for i in picture:
        for j in i:
            if j == 0:
                line += ' '
            elif j == 1:
                line += '*'
        print(line)
        line = ''


draw()