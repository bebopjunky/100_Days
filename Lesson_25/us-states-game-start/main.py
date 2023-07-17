import pandas
import turtle

screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor)
score = 0
correct = []
while len(correct) != len(data):
    answer = screen.textinput(title=f"Correct {len(correct)}/{len(data)}", prompt="Guess the name of a state: ").title()
    if answer == "Exit":
        break
    if answer in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        correct.append(answer)

# to_learn = []
# for state in states:
#     if state not in correct:
#         to_learn.append(state)

to_learn = [state for state in states if state not in correct]

data_dic = {
    "to learn": [to_learn]
}

data_csv = pandas.DataFrame(data_dic)
data_csv.to_csv("states_to_learn.csv")


