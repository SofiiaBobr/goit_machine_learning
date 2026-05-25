
import turtle


def draw_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    turtle.left(45)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.right(90)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.left(45)
    turtle.backward(branch_length)


if __name__ == "__main__":
    level = int(input("Enter recursion level: "))

    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()

    draw_tree(100, level)

    turtle.done()
