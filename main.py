from turtle import Screen
from player import Player
from aliens import Aliens
from missile import Missile
import aliens
from win_lose import WIN_LOSE

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
missile = Missile()
win_lose = WIN_LOSE()


aliens_first_row = Aliens.create_aliens(-250, 240, 15, 36)
aliens_second_row = Aliens.create_aliens(-220, 200, 14, 33)
aliens_third_row = Aliens.create_aliens(-250, 160, 15, 36)
aliens_fourth_row = Aliens.create_aliens(-220, 120, 14, 33)

screen.listen()
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    Aliens.move_cars()
    missile.move_missile()

    if missile.ycor() > 240:
        missile.shoot_again_man(player.xcor(), player.ycor())
    

    for c in range(len(aliens.all_cars)):
        if missile.distance(aliens.all_cars[c]) < 13:
            Aliens.destroy_bricks(aliens.all_cars[c])
            Aliens.clear_screen(aliens.all_cars[c])
            missile.destroy_missile()
            missile.clear_screen()

        if player.distance(aliens.all_cars[c]) < 20:
            win_lose.lose()
            game_is_on = False

        if aliens.all_cars[c].ycor() < -250:
            win_lose.lose()
            game_is_on = False


        

screen.exitonclick()
            


    


    

            

        