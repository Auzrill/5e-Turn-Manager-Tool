print("Welcome to the combat calculator!")
print("This caculator should help you make the most of your turn.")
print("Follow the case-sensitive prompts to navigate your turn.")
print("At any time, type \"end turn\" to end your turn.")
print("------------")

def welcome():
    print(" \nIt's your turn! \n ")
    
welcome()

def welcome_again():
  print(" \n    It's your turn again! \n ")

action =  False
bonus_action = False
movement = False
movement_speed = ()
has_moved = False

def end_turn():
    print("\n\nWhile it's not your turn, you can use a held action or a reaction.\n")
    turn_reset()
    welcome_again()
    check_options()


def turn_reset():
    global action
    action = False
    global bonus_action
    bonus_action = False
    global movement
    movement = False
    global has_moved
    has_moved = False

def combat_options():
    print("You can use an \"action\", a \"bonus action\", or \"movement\", in any order.")
    print(" ")

def action_used():
    print("You can use a \"bonus action\" or \"movement\" in any order.")
    print("Or, you can end your turn with \"end turn\".")
    print (" ")

def movement_used():
    print("You can use an \"action\" or \"bonus action\" in any order.")
    print("Or, you can end your turn with \"end turn\".")
    print (" ")

def action_error():
    print(" ")
    print("You've already used an action this turn!")
    check_options()

def bonus_action_error():
    print(" ")
    print("You've already used a bonus action this turn!")
    check_options()

def movement_error():
    print(" ")
    print("You've already used your movement this turn!")
    check_options()

def error_message():
    print("I'm sorry, I don't understand.")
    check_options()

def error_message_action():
    print("I'm sorry, I don't understand.")
    action_used()
    ask_decision_minus_action()

def error_message_bonus_action():
    print("I'm sorry, I don't understand.")
    bonus_action_used()
    ask_decision_minus_bonus_action()

def make_an_attack():
    print(" \nYou make an attack! \n ")
    global action
    action = True
    check_options()


def cast_a_spell():
    print(" \nYou cast a spell! \n ")
    global action
    action = True
    check_options()

def dash_action():
    print(" \nYou use the dash action! ")
    print("This lets you move up to your movement speed. \n")
    global action
    action = True
    check_options()

def bonus_action_used():
    print("You can use an \"action\" or \"movement\" in any order.")
    print("Or, you can end your turn with \"end turn\".")
    print (" ")

def make_a_bonus_action():
    print("\nLet's use a bonus action! You can do things like hide, use second wind, etc.")
    print("(Note: you can't hold an \"action\" as a bonus action. ;) ) \n")
    the_bonus_action = input("Tell me what you're doing! ")
    print(f" \nYou did \"{the_bonus_action}\" as a bonus action! \n")
    global bonus_action
    bonus_action = True
    check_options()

def make_something_else():
    something_else = input("Tell me what you're doing! ")
    print(f" \n You did \"{something_else}\" as your action! \n")
    global action
    action = True
    check_options()

def make_movement2():
    print(" \nYou used your movement! \n")
    global movement
    movement = False
    check_options()

def update_moved():
    global has_moved
    has_moved = True
 
def ask_decision_minus_bonus_action():
  decision = input("What would you like to do? ")
  if decision == "bonus action":
    bonus_action_error()
  elif decision == "Bonus action":
    bonus_action_error()
  elif decision == "end turn":
    end_turn()
  else:
    error_message_bonus_action()
    ask_decision_minus_bonus_action()

def ask_decision_minus_action():
  decision = input("What would you like to do? ")
  if decision == "action":
    action_error()
  elif decision == "Action":
    action_error()
  elif decision == "end turn":
    end_turn()
  else:
    error_message_action()
    check_options()

def ask_decision_minus_movement():
  decision = input("What would you like to do? ")
  if decision == "movement":
    movement_error()
  elif decision == "Movement":
    movement_error()
  elif decision == "end turn":
    end_turn()
  else:
    error_message_action()
    check_options()

def something_else():
    print(" \nGreat! You want to do something else as your action.")
    print("If your DM says this 'something else' counts as an action, you can do it!")
    print("Note: You can't use a 'bonus action' as an action.")
    print("If you've changed your mind, say \"nevermind\". \n")
    something_else_selection = input("Is this 'something else' an action? ")
    if something_else_selection == "Yes":
        make_something_else()
    elif something_else_selection == "yes":
        make_something_else()
    elif something_else_selection == "nevermind":
        combat_options()
        ask_decision()
    elif something_else_selection == "No":
        combat_options()
        ask_decision()
    elif something_else_selection == "no":
        combat_options()
        ask_decision()
    elif something_else_selection == "end turn":
        end_turn()
    else:
        error_message()


def answer_action():
        print(" \nGreat! Let's use an action.")
        print("You can \"attack\", \"cast a spell\", \"dash\", or do \"something else\".")
        print("If you've changed your mind, say \"nevermind\".")
        action_selection = input("Pick an action: ")
        if action_selection == "Attack":
          make_an_attack()
        elif action_selection == "attack":
          make_an_attack()
        elif action_selection == "cast a spell":
          cast_a_spell()
        elif action_selection == "Cast a spell":
          cast_a_spell()
        elif action_selection == "Dash":
          dash_action()
        elif action_selection == "dash":
          dash_action()
        elif action_selection == "something else":
          something_else()
        elif action_selection == "nevermind":
          combat_options()
          ask_decision()
        elif action_selection == "end turn":
          end_turn()
        else:
          error_message()

def answer_bonus_action():
        print(" \nGreat! Let's use a bonus action.")
        print("If you have an ability, spell, or feature that lets you use a bonus action, \n you can do that here.")
        print("If you've changed your mind, say \"nevermind\". \n")
        bonus_action_selection = input("Can you use a bonus action? ")
        if bonus_action_selection == "Yes":
          make_a_bonus_action()
        elif bonus_action_selection == "yes":
          make_a_bonus_action()
        elif bonus_action_selection == "nevermind":
          combat_options()
          ask_decision()
        elif bonus_action_selection == "No":
          combat_options()
          ask_decision()
        elif bonus_action_selection == "no":
          combat_options()
          ask_decision()
        elif bonus_action_selection == "end turn":
          end_turn()
        else:
          error_message()

def answer_movement():
        print(" \nGreat! Let's use your movement. \n")
        print("You can use all of part of your movement now, and the rest later.")
        #print("(Either way, this program will consider your movement used if you answer \"yes\".) \n")
        print("If you've changed your mind, say \"nevermind\". \n")
        movement_selection = input("Use movement? ")
        if movement_selection == "Yes":
          make_movement()
        elif movement_selection == "yes":
          make_movement()
        elif movement_selection == "nevermind":
          check_options()
          ask_decision()
        elif movement_selection == "No":
          check_options()
          ask_decision()
        elif movement_selection == "no":
          check_options()
          ask_decision()
        elif movement_selection == "end turn":
          end_turn()
        else:
          error_message()

movement_number = ()
movement_result= ()

def make_movement():
  if has_moved == False:
    movement_speed = input("Enter your movement speed as a whole number: ")
    if movement_speed != 0:
      print(" \nHow much of your movement do you want to use? \n")
      print("DO NOT USE LETTERS HERE!")
      global movement_number
      movement_number = input("Enter movment number: ")
      global movement_result
      movement_result = int(movement_speed) - int(movement_number)
      if movement_result > 0:
        global movement
        movement = False
        print(f"You used {movement_number} of your speed and have {movement_result} left!")
        movement_speed = movement_result
        update_moved()
        check_options()
      else:
        print("You've used all of your movement!")
        movement_speed = 0
        movement = True
        update_moved()
        check_options()
  else:
        if movement_result > 0:
            print(f"You have {movement_result} feet of movement left.")
            print("\nHow much of your movement do you want to use? \n")
            print("DO NOT USE LETTERS HERE!")
            movement_number = input("Enter movement numer: ")
            movement_result = int(movement_result) - int(movement_number)
            if movement_result == 0:
                print("You've used all of your movement!")
                movement_speed = 0
                movement = True
                update_moved()
                check_options()
            elif movement_result < 0:
                print("You can't move that much! Try again.")
                movement = False 
                check_options()
            else:
                movement = False
                print(f"You used {movement_number} of your speed and have {movement_result} left!")
                movement_speed = movement_result
                update_moved()
                check_options()
        else:
            print("You've used all of your movement!")
            movement_speed = 0
            movement = True
            update_moved()
            check_options()


def ask_decision():
  decision = input("What would you like to do? ")
  if decision == "action" and action == False:
    answer_action()
  elif decision == "Action" and action == False:
    answer_action()
  elif decision == "bonus action" and bonus_action == False:
    answer_bonus_action()
  elif decision == "Bonus action" and bonus_action == False:
    answer_bonus_action()
  elif decision == "movement" and movement == False:
      answer_movement()
  elif decision == "Movement" and movement == False:
      answer_movement()
  elif decision == "action" and action == True:
      action_error()
  elif decision == "bonus action" and bonus_action == True:
      bonus_action_error()
  elif decision == "movement" and movement == True:
      movement_error()
  elif decision == "end turn":
      end_turn()
  else:
    error_message()
    ask_decision()

def check_options():
  if action == False and bonus_action == False and movement== False:
    combat_options()
    ask_decision()
  elif not action and not bonus_action and movement:
    print("You can still make an \"action\" and \"bonus action\" this turn.")
    ask_decision()
  elif action and not bonus_action and not movement:
    print("You can still make a \"bonus action\" and \"movement\" this turn.")
    ask_decision()
  elif action == False and bonus_action == True and movement == False:
    print("You can still make an \" action\" and \"movement\" this turn.")
    ask_decision()
  elif not action and bonus_action and movement:
    print("You can still make an \"action\" this turn.")
    ask_decision()
  elif action and not bonus_action and movement:
    print("You can still make a \"bonus action\" this turn.")
    ask_decision()
  elif action and bonus_action and not movement:
    print("You can still make a \"movement\" this turn.")
    ask_decision()
  else:
    print("Looks like you're out of options for this turn!")
    end_turn()

check_options()




    


    

    
