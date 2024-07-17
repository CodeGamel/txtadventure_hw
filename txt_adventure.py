user_input = input("You wake up in the middle of the woods. You are parched and exhausted. You see two paths: one that leads to a forest, and one to a cave. Which one do you take? ")

if user_input == 'cave':
    print('Its dark and silent. All that can be heard is water hitting the cold rock')
    
    action = input('Do you want to use the flashlight or continue in the dark? ')
    
    if action == 'continue in dark':
        print('You walked and fell and continued falling. When you hit the ground you immediately died. Game over.')
    elif action == 'flashlight':
        print('You explore the caves and see a huge hole in the middle of the cave. Good thing you had your flashlight. You continue on until you find a chest filled with one gazillion dollars. You are now rich and won the game. Congrats!')
    else:
        print("Don't waste my time, choose an option.")

elif user_input == 'forest':
    print('You hear a loud creaking echoing through the forest. As you stumble to leave, you trip over a body.')
    
    action = input ('Do you search the body or continue?') 
    
    if action == 'search' :
        print('You found a flashlight! You continue walking and find a cabin. Turns out you live in the forest and you bumped your head.')
    elif action == ('continue') :
        print('You walked off a cliff and died.')

else:
    print("Invalid choice. You stand there confused and lost. Game over.")
