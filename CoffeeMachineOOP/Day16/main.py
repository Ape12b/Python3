# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("green")
#
# my_screen = Screen()
#
# print(my_screen.canvwidth)
#
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])

table.align = "l"
print(table)