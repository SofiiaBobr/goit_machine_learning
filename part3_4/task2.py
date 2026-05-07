import turtle
def coh(t, len, level):
    if level == 0:
        t.forward(len)
    else:
        for angle in [60, -120, 60, 0]:
            coh(t, len/3, level-1)
            t.left(angle)

if __name__ == "__main__":
    level = int(input(' Введіть рівень рекурсії'))
    t = turtle.Turtle()
    t.speed(0)
    for _ in range(3):
        coh(t, 300, level)
        t.right(120)
    turtle.done()