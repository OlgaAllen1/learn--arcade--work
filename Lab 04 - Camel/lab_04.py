import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    number_of_drinks = 3

    done = False
    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        pickone = input().upper()

        traveling = False

        if pickone == "Q":
            print("The end")
            done = True

        elif pickone == "A":
            if number_of_drinks > 0:
                number_of_drinks -= 1
                thirst = 0
                print(f"You have {number_of_drinks} drinks left")
            else:
                print("You don't have drinks left")

        elif pickone == "B":
            traveling = True
            iteration_travel = random.randint(5, 12)
            miles_traveled = miles_traveled+iteration_travel
            print(f"You traveled {iteration_travel} miles")
            thirst += 1
            camel_tiredness += 1
            natives_traveled += random.randint(7, 14)

        elif pickone == "C":
            traveling = True
            iteration_travel = random.randint(10, 20)
            miles_traveled = miles_traveled + iteration_travel
            print(f"You traveled {iteration_travel} miles")
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            natives_traveled += random.randint(7, 14)

        elif pickone == "D":
            print("The camel is happy!")
            camel_tiredness = 0
            natives_traveled = natives_traveled + random.randint(7, 14)

        elif pickone == "E":
            print(f"Miles traveled: {miles_traveled}")
            print(f"Drinks: {number_of_drinks}")
            print(f"The Natives are {miles_traveled-natives_traveled} miles behind you")
            print(f"Thirst is {thirst}")
            print(f"Camel tiredness {camel_tiredness}")

        if traveling and random.randrange(20) == 0:
            print("You found an Oasis!!!")
            number_of_drinks = 3
            camel_tiredness = 0
            thirst = 0

        if thirst > 6:
            print("You died of thirst!")
            done = True
            break
        elif thirst > 4:
            print("You are thirsty!")

        if camel_tiredness > 8:
            print("Your camel is dead!")
            done = True
            break
        elif camel_tiredness > 5:
            print("Your camel is getting tired.")

        if miles_traveled - natives_traveled < 0:
            print("The natives killed you!")
            done = True
            break
        elif miles_traveled-natives_traveled < 15:
            print("The natives are getting close!")

        if miles_traveled >= 200:
            print("You won the game!")
            done = True


main()
