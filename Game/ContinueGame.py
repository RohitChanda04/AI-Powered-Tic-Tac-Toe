def continue_game():
    answer = input("Do you want to play again?")
    if answer in ['Yes','Y','yes','y','YES']:
        return True
    elif answer in ['No','N','no','n','NO']:
        return False
    else:
        print("Please provide a valid answer...")
        print("For 'yes', you can write 'Yes','yes','Y','y', or 'YES'.")
        print("For 'no', you can write 'No','no','N','n', or 'NO'.")
        continue_game()