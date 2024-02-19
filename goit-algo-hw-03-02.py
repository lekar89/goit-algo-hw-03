import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.penup()
    fractal_turtle.goto(-150, 90)
    fractal_turtle.pendown()

    order = int(input("Введіть рівень рекурсії (ціле число): "))

    for _ in range(3):
        koch_snowflake(fractal_turtle, order, 300)
        fractal_turtle.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()
