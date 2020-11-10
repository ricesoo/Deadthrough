print("Welcome to my first python game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 20

if age >= 20:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a cthulhu and lost 5 health.")
                health -= 5

            ans = input("You notice a house a cave and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the Bratva... He doesn't like you and you lose 5 health")
                health -= 5



                ans = input("You somehow dodged Bratva. You saw there is cave. Should you go there (yes/no)? ")
                if ans == "yes":
                 print("You go to cave and suddenly you saw something...")
                elif ans == "no":
                 print("Before Bratva bring his shotgun, you were sucked into....")

                 ans = input("You were in a island with complete darkness, you saw a two little red flashes, should you (approach/dodge)? ")
                 if ans == "dodge":
                    print("Be the kind of person who dares to face life's challenges and overcome them rather than dodging them\n -Roy T. Bennett ")
                    health -= 20
                 elif ans  == "approach":
                    print("You completed the game\n No victory without suffering\n-J. R. R. Tolkien")

                    if health <= 0:
                     print("You now have 0 health and you lost the game...")
                    else:
                        print("You won")


            else:
                print("You fell in the river and lost...")









        else:
            print("You fell down and lost...\nSometimes good things fall apart so better things can fall together\n-Marilyn Monroe")

    else:
        print("Nothing in the universe can stop you from letting go and starting it over again \n-Guy Finley")
else:
    print("Growing up means realizing a lot of your friends aren't really your friends.\n-Pinterest")
