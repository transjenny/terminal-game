import os
import time

print("welcome to my text thingy")
print("starting up")
time.sleep(2)
print("game started")
time.sleep(1)
os.system('clear')

def the_ladder():
    if make_a_choice_YorN("As you start using the ladder, it starts to get wobbly. Do you jump to a nearby opening in the wall?"):
            if make_a_choice_YorN("You jump into the opening. It leads into a deep cave too far for you to see the walls. Do you move further into the cave?"):
                if make_a_choice_YorN("You see carvings on the wall nearby. It's very dark. Do you get closer to see what the carvings say?"):
                    print('You look at the carvings. They say "you\'re a burden on us."')
                    if make_a_choice_YorN("Do you look at more of the carvings?"):
                        print('The next carving you read says, "why can\'t I be normal, why, why."')
                        if make_a_choice_YorN("There seems to be a button next to the carvings. Do you press it?"):
                            print("After you press it, a hologram starts playing.")
                            print('"Why can\'t I be normal? Everyone hates me now," with someone crying on the hologram.')
                            print("The roof opens, and then you get thrown out of the cave system to the outside.")
                            print("Ending three: There are so many unanswered questions.")
                        else:
                            print("you just just fading away. you know your going to die")
                            print("Ending 8: gone, no signs")
                    else:
                        print("the wall moves in and crushs you")
                        print("Ending 9:")


def make_a_choice_YorN(string):
    print(string)
    a = input("what will you do? ")
    yes = False
    if "y" in a or "Y" in a:
        yes = True
    elif "n" in a or "N" in a:
        pass
    else:
        yes = make_a_choice_YorN("yes or no?")
    return yes

def make_a_choice_YorN_timed(string):
    start_time = time.time()  # Record the start time
    print(string)
    a = input("what will you do? ")
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    yes = False
    if "y" in a or "Y" in a:
        yes = True
    elif "n" in a or "N" in a:
        pass
    else:
        yes, elapsed_time = make_a_choice_YorN_timed("yes or no?")

    
    return yes, elapsed_time

if make_a_choice_YorN("you find yourself in a dark and deep cave. It seems to be getting deeper by the minute.\nYou see some carvings on the walls. Do you go to them?"):
    if make_a_choice_YorN("You walk up to the wall with the carvings. As you walk up to the carvings, a feeling of dread starts following you. Do you get closer so you can read them?"):
        if make_a_choice_YorN('You walk up to the first carving. It reads "why are you like this?" Your feeling of dread is worse now. Do you continue?'):
            choice, elapsed_time = make_a_choice_YorN_timed("You start reading the next one. The floor drops under you. You need to quickly grab onto something or you will die.\nGrab onto a nearby torch that's on the wall?")
            if elapsed_time > 3:
                print("Ending two: You died. Everyone thinks you ran away.")
                exit()
            elif choice:
                if make_a_choice_YorN("You see an object in the middle of the cave moving up. Do you jump onto it?"):
                    if make_a_choice_YorN("You make the jump, and it moves you up to the exit of the cave. Do you jump out of the cave?"):
                        print("Ending one: You made it to the outside. You still have no idea what happened or why.")
                    else:
                        print("Ending four: the platform fell under you and you died, everyone thinks your missing")
            elif(choice == False):
                print("Ending five: you fell and died, but you made an sos call before you died. people know where you were")
        else:
            if(make_a_choice_YorN("look look around and see a ladder. do you climb it?")):
                the_ladder()
            else:
                if( make_a_choice_YorN("there is nothing else for you todo. do you climb the ladder?")):
                    the_ladder()
                else:
                    if(make_a_choice_YorN("you look at the carving and a arrow hits you in your back, blood is everywhere, do you take it out?")):
                        print("Ending six: you died, you were never found")
                    else:
                        if(make_a_choice_YorN("run to the sunlight you need super far down the cave?")):
                            print("you start running to the sunlight and more arrows hit you, one after the other\n you press the sos butten on your radio\n you pass out then wake up in a hisbital, you dont rerember what happened anymore.")
                            print("Ending 7: no menory ")
                        else:
                            print("Ending 8: you die, no one ever finds you or knows you")
            
            

else:
    if make_a_choice_YorN("You see a ladder labeled 'support'. Do you use the ladder to get out?"):
        if make_a_choice_YorN("As you start using the ladder, it starts to get wobbly. Do you jump to a nearby opening in the wall?"):
            if make_a_choice_YorN("You jump into the opening. It leads into a deep cave too far for you to see the walls. Do you move further into the cave?"):
                if make_a_choice_YorN("You see carvings on the wall nearby. It's very dark. Do you get closer to see what the carvings say?"):
                    print('You look at the carvings. They say "you\'re a burden on us."')
                    if make_a_choice_YorN("Do you look at more of the carvings?"):
                        print('The next carving you read says, "why can\'t I be normal, why, why."')
                        if make_a_choice_YorN("There seems to be a button next to the carvings. Do you press it?"):
                            print("After you press it, a hologram starts playing.")
                            print('"Why can\'t I be normal? Everyone hates me now," with someone crying on the hologram.')
                            print("The roof opens, and then you get thrown out of the cave system to the outside.")
                            print("Ending three: There are so many unanswered questions.")



