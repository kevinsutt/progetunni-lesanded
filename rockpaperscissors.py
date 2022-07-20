question = input("Rock, paper or scissors?:  ").lower()
s = question.strip()
print("You have chosen " + str(question))
question2 = input("Rock, paper or scissors?:  ").lower()
f = question2.strip()
print("You have chosen " + str(question2))

if s == "rock" and f == "scissors":
    print("Rock beats scissors. Player1 wins!")
elif s == "rock" and f == "paper":
    print("Paper beats rock. Player2 wins!")
elif s == "paper" and f == "scissors":
    print("Scissors beat paper. Player2 wins!")
elif s == "paper" and f == "rock":
    print("Paper beats rock. Player1 wins!")
elif s == "scissors" and f == "rock":
    print("Rock beats scissors. Player2 wins!")
elif s == "scissors" and f == "paper":
    print("Scissors beats paper. Player1 wins!")
elif s == "paper" and f == "paper":
    print("It is a tie!")
elif s == "rock" and f == "rock":
    print("It is a tie!")
elif s == "scissors" and f == "scissors":
    print("It is a tie!")
else:
    print("A input or inputs is wrong! Please start the game again!")

