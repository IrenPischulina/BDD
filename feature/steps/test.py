from behave import *
from game import Game
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

#2
@given("I have created field")
def step_impl(context):
    global game
    game = Game()
    assert game is not None
    assert game.field is not None

@when("I do move down")
def step_impl(context):
    global game
    global game_field_buf
    game_field_buf = copy.deepcopy(game.field)
    game.move_down()

def get_zero_place(field):
    for i in range(4):
        for j in range(4):
            if field[i][j] == 0:
                return [i, j]

@then("Cell above the zero cell move down and the zero cell move up")
def step_impl(context):
    global game
    global game_field_buf

    zero_place_before = get_zero_place(game_field_buf)
    zero_place = get_zero_place(game.field)

    if zero_place_before[0] == 0:
        assert game_field_buf == game.field
    else:
        assert zero_place[1] == zero_place_before[1]
        assert zero_place[0] == zero_place_before[0] - 1

        for i in range(4):
            for j in range(4):
                if [i, j] != zero_place_before and [i, j] != zero_place:
                    assert game_field_buf[i][j] == game.field[i][j]

        assert game_field_buf[zero_place[0]][zero_place[1]] == game.field[zero_place_before[0]][
            zero_place_before[1]]

#3
@when("I do left move")
def step_impl(context):
    global game
    global game_field_buf
    game_field_buf = copy.deepcopy(game.field)
    game.move_left()

@when("I do right move")
def step_impl(context):
    global game
    global game_field_buf
    game_field_buf = copy.deepcopy(game.field)
    game.move_right()

@when("I do up move")
def step_impl(context):
    global game
    global game_field_buf
    game_field_buf = copy.deepcopy(game.field)
    game.move_up()

@then("Cell right from the zero cell move left and the zero cell move right")
def step_impl(context):
    global game
    global game_field_buf

    zero_place_before = get_zero_place(game_field_buf)
    zero_place = get_zero_place(game.field)

    if zero_place_before[0] == 3:
        assert game_field_buf == game.field
    else:
        assert zero_place[1] == zero_place_before[1] + 1
        assert zero_place[0] == zero_place_before[0]

        for i in range(4):
            for j in range(4):
                if [i, j] != zero_place_before and [i, j] != zero_place:
                    assert game_field_buf[i][j] == game.field[i][j]

        assert game_field_buf[zero_place[0]][zero_place[1]] == game.field[zero_place_before[0]][
            zero_place_before[1]]


@then("Cell left from the zero cell move right and the zero cell move left")
def step_impl(context):
    global game
    global game_field_buf

    zero_place_before = get_zero_place(game_field_buf)
    zero_place = get_zero_place(game.field)

    if zero_place_before[0] == 0:
        assert game_field_buf == game.field
    else:
        assert zero_place[1] == zero_place_before[1] - 1
        assert zero_place[0] == zero_place_before[0]

        for i in range(4):
            for j in range(4):
                if [i, j] != zero_place_before and [i, j] != zero_place:
                    assert game_field_buf[i][j] == game.field[i][j]

        assert game_field_buf[zero_place[0]][zero_place[1]] == game.field[zero_place_before[0]][
            zero_place_before[1]]


@then("Cell under the zero cell move up and the zero cell move down")
def step_impl(context):
    global game
    global game_field_buf

    zero_place_before = get_zero_place(game_field_buf)
    zero_place = get_zero_place(game.field)

    if zero_place_before[0] == 3:
        assert game_field_buf == game.field
    else:
        assert zero_place[1] == zero_place_before[1] + 1
        assert zero_place[0] == zero_place_before[0]

        for i in range(4):
            for j in range(4):
                if [i, j] != zero_place_before and [i, j] != zero_place:
                    assert game_field_buf[i][j] == game.field[i][j]

        assert game_field_buf[zero_place[0]][zero_place[1]] == game.field[zero_place_before[0]][
            zero_place_before[1]]

#4
@when("I mix game field")
def step_impl(context):
    global game
    global game_field_buf
    game_field_buf = copy.deepcopy(game.field)
    game.mix()

@then("I have changed game field and no one cell is missing")
def step_impl(context):
    global game
    global game_field_buf
    assert game.field != game_field_buf

    cell_counter = []
    for i in range(16):
        cell_counter.append(0)

    for i in range(4):
        for j in range(4):
            cell_counter[game.field[i][j]] += 1

    for i in range(16):
        assert cell_counter[i] == 1

#5
@then("The game is not wined")
def step_impl(context):
    global game
    assert game.isWin() == False

@then("The game is wined")
def step_impl(context):
    global game
    assert game.isWin()
