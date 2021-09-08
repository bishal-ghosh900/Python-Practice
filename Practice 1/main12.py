# Guessing game

secret_number = 5

i = 0
guess = 0
while i < 3:
    guess = int(input("Guess: "))
    if guess == secret_number :
        print("You got it right.")
        break
    i += 1
else:
# while loop executes the block until a condition is satisfied. When the condition becomes false, the statement immediately after the loop is executed. The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed.The else block just after for/while is executed only when the loop is NOT terminated by a break statement
    print("You missed your 3 chances.")