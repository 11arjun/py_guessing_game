# simple while loop strategy, guessing a password
print("Welcome To Arjun & his company \n", "Guess it or Loose it !")
password = "arjun"
username = input(" Username ")

while True:
    guess = input(" Guess Password:").lower()
    if guess ==  password:
         print("Congrats, You've won " + username)
         break
    else:
        print("Wrong password, Try again " + username)
        print("Hint:" , "Starts with A and ends with N")