from behave import *
from game4 import Game
import copy
game = None
game_field_buf = None


@given("I have my game class")
def step_impl(context):
    Game()


@When("I create new game")
def step_impl(context):
    global game
    game = Game()
    assert game is not None


@then("I have created field with size 4x4 and numbers from 1 to 15 and one empty cell")
def step_impl(context):
    global game
    assert game.field is not None
    assert len(game.field) == 4
    assert len(game.field[0]) == 4
    for i in range(4):
        for j in range(4):
            if i != 3 and j != 3:
                assert game.field[i][j] == j+i*4+1
    assert game.field[3][3] == 0