from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()
    cars.move()

    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()