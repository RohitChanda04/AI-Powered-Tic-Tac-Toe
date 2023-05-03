def user_input():
    userInput = input('\nEnter position between 1 and 9, both inclusive: ')
    if not userInput.isdigit():
        while not userInput.isdigit():
            print('\nThe position needs to be an Integer value and in range 1-9!')
            userInput = input('\nPlease enter position again: ')
    temp = int(userInput)
    if temp < 0:
        while temp < 0:
            user_input()
    if temp not in range(1,10):
        print('\nOut of range!')
        user_input()
    position = temp
    return position