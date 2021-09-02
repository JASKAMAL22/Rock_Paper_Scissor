import random

elements = {"rock":'r' ,"paper": 'p' ,"scissor":'s'}

user_win=0
comp_win=0

while(True):
    user_input = input("Type 'r' for rock | 'p' for paper | 's' for scissor or 'q' to quit : ").lower()
    if user_input == 'q':
        break

    abbrev_list = list(elements.values())
    if user_input not in abbrev_list:
        continue

    random_no = random.choice(list(elements.keys()))

    pick_by_comp = elements[random_no]
    print("Computer Selects", pick_by_comp)

    if ((user_input=='s' and pick_by_comp=='p') or (user_input=='r' and pick_by_comp=='s') or (user_input=='p' and pick_by_comp=='r')):
        print("Hooray! You won :)")
        user_win+=1

    elif((user_input==pick_by_comp=='p') or (user_input==pick_by_comp=='r') or (user_input==pick_by_comp=='s')):
        print("Game Tie ")

    else:
        print("Better luck next time!! ")
        comp_win+=1

print("Computer won {} times".format(comp_win))
print("You won {} times".format(user_win))
print("Goodbye! Have a Nice Day ")