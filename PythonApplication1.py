import random

#A function to shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

print("This is a program to create a password with lenght between 6 to 16 charecters!")

#A function for quiting the program
def Quit():
    print("Quting the program!")
    quit()

#A function to create the password itself
def Password():
    passwordLength = int(input("Enter your wanted length of password:\n"))

#Main program starts here
    if passwordLength < 6:
        print("This lenght doesn't supported!")
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 6:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + digit1 + digit2 + digit3
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 7:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + digit1 + digit2 + digit3 + random.choice([letter4,digit4])
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 8:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + digit1 + digit2 + digit3 + digit4
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 9:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + digit1 + digit2 + digit3 + digit4 + random.choice([digit5,letter5])
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 10:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + digit1 + digit2 + digit3 + digit4 + digit5
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 11:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + digit1 + digit2 + digit3 + digit4 + digit5 + random.choice([digit6,letter6])
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 12:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 13:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter7 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57))
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        digit7 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + random.choice([digit7,letter7])
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 14:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter7 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57)) 
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        digit7 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 15:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter7 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter8 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57)) 
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        digit7 = chr(random.randint(48,57))
        digit8 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + random.choice([letter8,digit8])
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    elif passwordLength == 16:
        #Generate a random letter (based on ASCII code)
        letter1 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter2 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter3 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter4 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter5 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter6 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter7 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        letter8 = random.choice([chr(random.randint(65,90)),chr(random.randint(97,122))])
        #Generate a random digit (based on ASCII code)
        digit1 = chr(random.randint(48,57)) 
        digit2 = chr(random.randint(48,57))
        digit3 = chr(random.randint(48,57))
        digit4 = chr(random.randint(48,57))
        digit5 = chr(random.randint(48,57))
        digit6 = chr(random.randint(48,57))
        digit7 = chr(random.randint(48,57))
        digit8 = chr(random.randint(48,57))
        #Generate password using all the characters, in random order
        password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8 + digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + digit8
        password = shuffle(password)
        print("The generated password is: " + password) #Ouput
        # Ask the user for more options
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()
    else:
        print("This lenght doesn't supported yet!")
        b = input("Do yo want to create another password?\n[Y] - Yes, [Any key] - No\n")
        if b=='Y' or b=='y':
            Password()
        else:
            Quit()

#....
Password()
