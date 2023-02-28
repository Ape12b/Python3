import pandas
from turtle import Screen
from state_turtle import AllState

game = AllState()
screen = Screen()
screen.bgpic("blank_states_img.gif")

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
is_game_on = True
while is_game_on:
    state_guess = screen.textinput("Guess State", "Name of the state:")
    if state_guess is None or len(game.states) == 50:
        game.report()
        is_game_on = False
    elif state_guess.title() in state_list:
        state_x = int(state_data[state_data.state == state_guess].x)
        state_y = int(state_data[state_data.state == state_guess].y)
        game.add_state(state_guess.title(), state_x, state_y)

missed_states = [state.title() for state in state_list if state not in game.states]
missed_states_dict = {"state": missed_states}
missed_states = pandas.DataFrame.from_dict(missed_states_dict)
missed_states.to_csv("missed_states.csv")
screen.exitonclick()
