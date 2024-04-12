available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").casefold()
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

else:
    print("Aren't you glad you got out of there.")
