import turtle
import pandas
data = pandas.read_csv("50_states.csv")
stateList = data["state"].to_list()

# setup game screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle to write 
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

correctGuesses = []
score = 0
while score <=50:
    answer = (screen.textinput(title= f"{score}/50 states guessed", prompt= "Guess a state!")).title()
    if answer in stateList:
        score += 1        
        state = data[data.state == answer]
        x = state['x'].iloc[0]
        y = state['y'].iloc[0]
        text_turtle.penup()
        text_turtle.goto(x,y)
        text_turtle.pendown()
        text_turtle.write(answer)        
        correctGuesses.append(answer)
        
turtle.mainloop()
