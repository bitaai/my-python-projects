import random

def play_game():   
"""playing a round of number limit games  """
    number = random.randint(1, 100)
    attempts = 0
    
print("\n guess a number between 1 and 100
   
    while True:
        try:
            guess = int(input(" ("your guess:"): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print(" enter a number between 1 and 100.")
                continue
            
            if guess < number:
                print(" select it bigger!")
            elif guess > number:
                print("select it smaller!")
            else:
              
print(f"well done! You guessed {number} in {attempts} tries!")

                break
                
        except ValueError:
            print("please enter an integer. ")
    
    return attempts

def main():
    print("="*40)
    print("number guessing game")
    print("="*40)
    
    while True:
        play_game()
        
        again = input("\n are you playing again? (yes/no): ").lower()
        if again != 'no':
            print(" goodby!")
            break

if __name__ == "__main__":
    main()
