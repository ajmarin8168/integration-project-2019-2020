"""
integration project: Sports Trivia '19
__author__ = Allan Marin
"""


def main():
    """
    Starts the program
    :return:
    """
    score = 0
    print("Hello and welcome to Sports Trivia '19! \n")
    user_wishes_to_continue = True
    while user_wishes_to_continue:
  # Main Menu
        print("Main Menu \n1) Play Menu \n2) Info \n3) Exit Game \n")
        print("Career Status: ")
        playerCareerStatus(score)
        print("\nStars:")
        for stars in range(score):
            print("*" + "", end="")
        print("")
        main_menu = int(input("Enter the number of menu option desired: "))
        barrierDesign()
        # play options menu
        if main_menu == 1:
            print("\nSports Option Menu \n1) Football \n2) Basketball \n3) Baseball \n4) Hockey \n5) Soccer \n")
            user_input = int(input("Enter the number of sport option desired: "))
            print("")
            barrierDesign()
            # football is selected
            if user_input == 1:
                print("You Chose Football Trivia, Let's Begin! \n")
                # football question 1
                print("Question 1: Who won Super Bowl 51 in 2017? \n")
                print("Answers: \n1 ) Atlanta Falcons \n2 ) New England Patriots \n3 ) Oakland Raiders \n4 ) Baltimore Ravens \n")
                user_input = int(input("Enter Answer Here: "))
                print("")
                if user_input == 2:
                    print("Correct! The New England Patriots won \nSuper Bowl 51 in 2017 against the Atlanta Falcons. \n")
                    score = score + 1
                    print("score:", score)
                else:
                    print("Incorrect, The New England Patriots won  \nSuper Bowl 51 in 2017 against the Atlanta Falcons. \n")
                    print("score:", score)
                print("")
                # next question 1
                barrierDesign()
                user_input = askingUsertoContinue()
                barrierDesign()
                # football question 2
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank you for playing Sprts Trivia '19")
                elif user_input == 1:
                    print("Question 2: who owns the current title of most \nrunning yards in their career as of 2019? \nAnswers: \n1) Frank Gore \n2) Adrian Peterson \n3) Emmitt Smith \n4) Josh Jacobs \n")
                    user_input = int(input("Enter Ansewer Here: "))
                    print("")
                    if user_input == 3:
                        print("Correct, Emmit smith has the record for most \nrunning yards in a career with a total \nof 18,355 yards!")
                        score = score + 1
                        print("")
                        print("score:", score)
                        print("")
                    else:
                        print("Incorrect,Emmit smith has the record for most \nrunning yards in a career with a total \nof 18,355 yards!")
                        print("")
                        print("score:", score)
                        print("")
                    # next question 2
                    barrierDesign()
                    user_input = askingUsertoContinue()
                    barrierDesign()
                    # football question 3
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing Sports Trivia '19!")
                        print("score:", score)
                    elif user_input == 1:
                        print("Question 3: Who is the starting quarterback of the packers as of 2019? \nAnswers: \n1) Derk Carr \n2) Tom Brady \n3) Aaron Rodgers \n4) Cam Newton \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        if user_input == 3:
                          print("Correct, Aaron Rodgers is the starting quarterback \nfor the Packers as of 2019.")
                          score = score + 1
                          print("")
                          print("score:", score)
                          print("")
                        else:
                          print("Incorrect, Aaron Rodgers is the startign quarterback \nfor the Packers as of 2019.")
                          print("")
                          print("score:", score)
                          print("")
                        barrierDesign()
                        print("Thank You for playing! \nYou have completed the football portion of Sports Trivia '19!\n")
                        print("score:", score)
                        print("")
                        barrierDesign()
                        print("1) Return to Main Menu \n2) End Game \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("")
                            print("Thank You for playing sports trivia 19'! \n")
                            print("score:", score)
                        barrierDesign()
            # basketball is selected
            elif user_input == 2:
                print("You Chose Basketball Trivia, Lets Begin! \n")
                # basketball question 1
                print("Question 1: What team did LeBron James get drafted to?\n \nAnswers: \n1 ) Clevland Cavaleirs \n2 ) Toronto Raptors \n3 ) Miami Heat \n4 ) Chicago Bulls \n")
                user_input = int(input("Enter Answer Here:"))
                print("")
                if user_input == 1:
                    print("Correct, LeBron James was drafted to the Clevland Calvaliers in 2003. \n")
                    score = score + 1
                    print("Score:", score)
                    print("")
                else:
                    print("Incorrect, LeBron James was drafted to the Clevland Cavaliers in 2003.\n")
                    print("Score:", score)
                    print("")
                # next question 3
                barrierDesign()
                user_input = askingUsertoContinue()
                barrierDesign()
                # exit for basketball question 1
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank You for playing Sports Trivia '19!")
                # basketball question 2
                elif user_input == 1:
                    print("Question 2: Who holds the record for most \nNBA championships as of 2019?\n \nAnswers: \n1) LA Lakers \n2) Chicago Bulls \n3) Boston Celtics \n4) Golden State Worriors \n")
                    user_input = int(input("Enter Answer Here: "))
                    print("")
                    if user_input == 3:
                        print("Correct, the Boston Celtics hold the most \nNBA championships with a total of 17. \n")
                        score = score + 1
                        print("score:", score)
                        print("")
                    else:
                        print("Incorrect, the Boston Celtics hold the most \nNBA championships with a total of 17. \n")
                        print("score:", score)
                        print("")
                    # next question 4
                    barrierDesign()
                    user_input = askingUsertoContinue()
                    barrierDesign()
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing Sports Trivia '19!")
                    # basketball question 3
                    elif user_input == 1:
                        print("Question 3: How many NBA teams are there as of 2019?\n \nAnswers: \n1) 32 \n2) 30 \n3) 18 \n4) 46 \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        if user_input == 2:
                            print("Correct, There are currently 30 NBA teams as of 2019.\n")
                            score = score + 1
                            print("score:", score)
                            print("")
                        else:
                            print("Incorrect, There are currently 30 NBA teams as of 2019.\n")
                            print("score:", score)
                            print("")
                        barrierDesign()
                        print("Thank You for playing! \nYou have completed the basketball portion of Sports Trivia '19!\n")
                        print("score:", score)
                        print("")
                        barrierDesign()
                        print("1) Return to Main Menu \n2) End Game \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        # Exit for basketball question 3
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("Thank You for playing sports trivia '19!")
                        barrierDesign()
            # baseball is selected
            elif user_input == 3:
              print("You chose baseball trivia, Let's Begin! \n")
              #baseball question 1
              print("Question 1: What MLB team does Chris Sale pitch for as of 2019?\n \nAnswers: \n1 ) Boston Red Sox \n2 ) Chicago White sox \n3 ) Tampa Bay Rays \n4 ) CHicago Cubs \n")
              user_input = int(input("Enter Answer Here: "))
              print("")
              if user_input == 1:
                print("Correct, Chris Sale is the starting pitcher for the \nBoston Red Sox as of 2019.\n")
                score = score + 1
                print("Score:", score)
                print("")
              else:
                print("Incorrect, Chris Sale is the starting pitcher for the \nBoston Red Sox as of 2019.\n")
                print("Score:", score)
                print("")
              # next question 5
              barrierDesign()
              user_input = askingUsertoContinue()
              barrierDesign()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing sports trivia '19!")
              # baseball question 2
              elif user_input == 1:
                print("Question 2: What MLB team has the most World Series wins? \n \nAnswers: \n1) Boston Red Sox \n2) St. Louis Cardinals \n3) New York Yankees \n4) LA Dodgers \n")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 3:
                  print("Correct, the New York Yankees have the most World Series wins, \nwith 27 total wins.\n")
                  score = score + 1
                  print("Score:", score)
                  print("")
                else:
                  print("Incorrect, the New York Yankees have the most World Series wins, \nwith 27 total wins.\n")
                  print("Score:", score)
                  print("")
                # next question 6
                barrierDesign()
                user_input = askingUsertoContinue()
                barrierDesign()
                if user_input == 3:
                  user_wishes_to_continue = False
                  print("Thank you for playing Sports Triva '19!")
                  print("")
                  print("score:", score)
              # baseball question 3
                elif user_input == 1:
                  print("Question 3: What famous baseball player was \nthe first to retire a number? \n \nAnswers: \n1) Babe Ruth \n2) Lou Gehrig \n3) Jackie Robinson \n4) Tom Seaver \n")
                  user_input = int(input("Enter Ansewer Here: "))
                  print("")
                  if user_input == 2:
                    print("Correct, Lou Gehrig was the first MLB player to retire\n a number in 1939. His number was 4 and retired as a Yankee.\n")
                    score = score + 1
                    print("score:", score)
                    print("")
                  else:
                    print("Incorrect, Lou Gehrig was the first MLB player to retire\n a number in 1939. His number was 4 and retired as a Yankee.\n")
                    print("score:", score)
                    print("")
                  barrierDesign()
                  print("Thank You for playing! \nYou have completed the basetball portion of Sports Trivia '19!\n")
                  barrierDesign()
                  print("1) Return to Main Menu")
                  print("2) End Game")
                  user_input = int(input("Enter Answer Here:"))
                  print("")
                  if user_input == 2:
                    user_wishes_to_continue = False
                    print("Thank You for playing Sports Trivia '19!")
                    print("")
                    print("score:", score)
                    print("")
                  barrierDesign()
            # hockey is selected
            elif user_input == 4:
              print("You Chose hockey Trivia, Let's begin!\n")
              # hockey question 1
              print("Question 1: What is the newest team to the NHL as of the 2019 season? \n \nAnswers: \n1 ) Columbus Blue Jackets \n2 ) Florida Panthers \n3 ) Minnesota Wilds \n4 ) Vagas Golden Knights \n")
              user_input = int(input("Enter Answer Here:"))
              print("")
              if user_input == 4:
                print("Correct, the Vagas Golden Knights are \nthe newest team to the NHL as of the 2019 season.\n")
                score = score + 1
                print("Score:", score)
                print("")
              else:
                print("Incorrect,the Vagas Golden Knights are \nthe newest team to the NHL as of the 2019 season.\n")
                print("Score:", score)
              # next question 7
              barrierDesign()
              user_input = askingUsertoContinue()
              barrierDesign()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing Sports Trivia '19!")
                print("")
                print("Score:", score)
                print("")
              # hockey question 2
              elif user_input == 1:
                print("Question 2: What NHl team has the most Stanley Cup wins?\n \nAnswers: \n1) LA Kings \n2) Tampa Bay Lightning \n3) Montreal Canadiens \n4) Ottawa Senators \n")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 3:
                  print("Correct, the Montreal Canadiens have won the most Stanly Cups,\nholding a totla of 24.\n")
                  score = score + 1
                  print("Score:", score)
                  print("")
                else:
                  print( "Incorrect,the Montreal Canadiens have won the most Stanly Cups,\nholding a totla of 24.\n")
                  print("Score:", score)
                #next question 8
                barrierDesign()
                user_input = askingUsertoContinue()
                barrierDesign()
                if user_input == 3:
                  user_wishes_to_continue = False
                  print("Thank you for playing Sports Trivia!")
                  print("")
                  print("score:", score)
                  print("")
              # hockey question 3
                elif user_input == 1:
                  print("Question 3: How many games are played in regular season hockey?\n \nAnswers: \n1) 32 \n2) 94 \n3) 82 \n4) 86 \n")
                  user_input = int(input("Enter Ansewer Here: "))
                  print("")
                  if user_input == 3:
                    print("Correct, there are only 82 regualar season games in hockey \n")
                    score = score + 1
                    print("Score:", score)
                    print("")
                  else:
                    print( "Incorrect,there are only 82 regular season games in hockey.\n")
                    print("Score:", score)
                    print("")
                  barrierDesign()
                  print("Thank You for playing! \nYou have completed the hockey portion of Sports Trivia '19!\n")
                  barrierDesign()
                  print("1) Return to Main Menu")
                  print("2) End Game")
                  user_input = int(input("Enter Answer Here:"))
                  print("")
                  print("score:", score)
                  print("")
                  if user_input == 2:
                    user_wishes_to_continue = False
                    print("Thank You for playing Sports Trivia '19!")
                    print("")
                    print("score:", score)
                    print("")
                  barrierDesign()
            # soccer is selected
            elif user_input == 5:
              print("You Chose soccer Trivia, Let's Begin!\n")
              # soccer question 1
              print("Question 1: How many professional soccer luages are there \nin the world as of 2019?\n \nAnswers: \n1 ) 18 \n2 ) 21 \n3 ) 23 \n4 ) 4 \n")
              user_input = int(input("Enter Answer Here:"))
              print("")
              if user_input == 2:
                print("Correct, there are 21 professional soccer leagues in \nthe world as of 2019.\n")
                score = score + 1
                print("")
                print("Score:", score)
              else:
                print("Incorrect,there are 21 professional soccer leagues in \nthe world as of 2019.\n")
                print("Score:", score)
                print("")
              # next question 9
              barrierDesign()
              user_input = askingUsertoContinue()
              barrierDesign()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing Sports Trivia '19!")
                print("")
                print("score:", score)
              # soccer question 2
              elif user_input == 1:
                print("Question 2: How many total players on the fild during a game?\n \nAnswers: \n1) 11 \n2) 22 \n3) 16 \n4) 9 \n")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 2:
                  print("Correct, there are a total 22 players on the fild \nat once during a game, 11 players per team\n")
                  score = score + 1
                  print("score:", score)
                  print("")
                else:
                  print( "Incorrect,there are a total 22 players on the fild \nat once during a game, 11 players per team\n")
                  print("score:", score)
                  print("")
              # next question 10
              barrierDesign()
              user_input = askingUsertoContinue()
              barrierDesign()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing sports Trivia '19!")
                print("")
                print("score:", score)
              # soccer question 3
              elif user_input == 1:
                print("Question 3: How many teams are in the Primer Luage as of 2019?\n \nAnswers: \n1) 20 \n2) 22 \n3) 16 \n4) 31 \n")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 1:
                  print("Correct, there are only 20 teams in the primer Luage as of 2019 \n")
                  score = score + 1
                  print("score:", score)
                  print("")
                else:
                  print( "Incorrect,there are only 20 teams in the primer Luage as of 2019 \n")
                  print("score:", score)
                print("")
                barrierDesign()
                print("Thank You for playing! \nYou have completed the soccer portion of Sports Trivia '19!\n")
                barrierDesign()
                print("1) Return to Main Menu")
                print("2) End Game \n")
                user_input = int(input("Enter Answer Here:"))
                print("")
                print("score:", score)
                print("")
                if user_input == 2:
                  user_wishes_to_continue = False
                  print("Thank You for playing Sports Trivia '19!")
                  print("")
                  print("score:", score)
                barrierDesign()
        # info from main menu
        elif main_menu == 2:
            print("\nGame Info:\n")
            print(
                "Thank you for playing Sports Trivia '19! This trivia game is \na basic knowledge quiz about various sports.\n \nSports Option Menu:\n \nIn the Sports options menu you can select one of five \ndifferent sports to be quized on.Each sport has \nthree questions and you will be awarded one point for every \nquestion correctly answered.\n \nStars and Career Status:\n \nAt the main menu, you will be able to see a stars counter and \ncareer status dipslay. The stars counter displays a * for \nevery question answered correctly. The career status dipslay \nshows you the current position in your career depending \non how many questions you have gotten correct. There are seven \npossible career status titels, starting at D1 draft pick to \nHall of Famer.\n \nChallenge your friends to see who can get all fifteen questions \ncorrect and flex your sports knowledge.\n")
            barrierDesign()
            print("Please select an option below \n")
            print("1) Return to Main Menu")
            print("2) Exit game \n")
            user_input = int(input("Enter menu option desired here:"))
            if user_input == 2:
                user_wishes_to_continue = False
                print("Thank You for playing Sports trivia '19!")
                print("")
                print("score:", score)
            barrierDesign()    
        # exit from Main Menu
        elif main_menu == 3:
            user_wishes_to_continue = False
            print("Thank You for playing Sports Trivia '19!")
            print("")
            print("score:", score)
            print("")
            print("Career Status: ")
            playerCareerStatus(score)
            print("\nStars:")
            for stars in range(score):
              print("*" + "", end="")
            print("")


def playerCareerStatus(score):
  if (score == 0):
    return (print("D1 Player"))
  elif (score > 0 and score <= 3):
    return (print("First Round Draft pick"))
  elif (score > 3 and score <= 6):
    return (print("Rookie"))
  elif (score > 6 and score <= 9):
    return (print("Starter"))
  elif (score > 9 and score <= 12):
    return (print("All star player"))
  elif (score > 12 and score <15):
    return (print("League MVP"))
  elif (score == 15):
    return (print("Hall of Famer"))
  """
  returns the players career status based on the the score they recive based on the amount of questions correct
  """

def askingUsertoContinue():
    """
    displays a reoccurring question
    """
    print("Would you like another question?")
    print("1 ) Yes")
    print("2 ) Return to Main Menu")
    print("3 ) Exit game \n")
    user_input = int(input("Enter answer here:"))
    print("")
    return user_input

    """
    returns the user input to either deplay next question, return to main menu, or end game
    """

def barrierDesign():
  for stars in range(79):
    print("^" + "", end="")
  print("")
  """
  creates the ^ deigned barrier between questions and menus
  """

main()
