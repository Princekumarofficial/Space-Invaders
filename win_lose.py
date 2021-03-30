from turtle import Turtle, setposition


class WIN_LOSE():

    def __init__(self):
        self.all_turtle = []

    def win(self):
        winner = Turtle()
        winner.color("white")
        winner.write("YOU WIN", align='center', font=('Courier', 25, 'bold'))
        winner.penup()
        winner.hideturtle()
        winner.setposition(0, 380)

    def lose(self):
        loser = Turtle()
        loser.color("white")
        loser.write("YOU LOSE", align='center', font=('Courier', 25, 'bold'))
        loser.penup()
        loser.hideturtle()
        loser.setposition(0, 380)

