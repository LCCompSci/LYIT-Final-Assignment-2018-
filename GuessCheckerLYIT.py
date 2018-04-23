''' This is the final LYIT Coding assigment as required to finish off our course - Completed 22 April 2018'''

# Need the 'random' library to generate our secret number
import random


# Function to check each guess and feedback appropriately
def guesschecker(guess,my_random,guess_counter,guesses):
    if (guess == my_random): # If player correctly guesses, feedback and return 1 to function call
        print ("\nYou got it! Well done, you got it on your "+guesses[guess_counter]+" guess, brilliant!")
        return 1

    elif (guess_counter==4): # If player has used all their guesses, sympathise!
        print ("\nSorry, you didn't win this time, you've run out of guesses.\nThe number I was thinking of was",my_random,".")

    else: # If player guesses incorrectly but still has guesses left, tell them and give them appropriate hint...
        print ("\nNo luck my friend it wasn't",guess,", you've got",4-guess_counter,"guesses left.")

        if (guess < 1) or (guess > 9): # Outside the range of possible number
            print ("Maybe you should read the rules again! ")

        elif (guess < my_random): # Guessed too low
            print ("Perhaps you'd like a hint...You need to go higher!")

        else: # Guesses too high...
            print ("Perhaps you'd like a hint...You need to go lower!")

# Main function 
def main():
    my_random=random.randint(1,9) # Generate a random number from 1 to 9 inclusive
    guess_counter=0 # Variable to keep track of the number of guesses
    guesses=['first','second','third','fourth','fifth'] # List to use in sentences

    # Tell the player how the game works and wish them well
    print ("\nWelcome to my guessing game - I've chosen a random number between 1 and 9.\nYou've got 5 guesses to match it, best of luck - though I don't think you'll need it!")

    # This loop will run a maximum of 5 times to represent the 5 guesses. On a correct guess it will 'break' from the loop
    while guess_counter<5:

        # Input the user guess, convert it to an integer and pass it to the guesschecker function
        # if it returns '1' it means that they've guessed correctly and it's time to break from the loop
        if (guesschecker(int(input("What's your "+guesses[guess_counter]+" guess? ")),my_random,guess_counter,guesses)==1):
            break
        # Increment the number of guesses on each 'While' loop
        guess_counter += 1


# Call our main() function
if __name__ == "__main__":
    main()
