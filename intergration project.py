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
        # play options menu
        if main_menu == 1:
            print("\nSports Option Menu \n1) Football \n2) Basketball \n3) Baseball \n4) Hockey \n5) Soccer \n")
            user_input = int(input("Enter the number of sport option desired: "))
            print("")
            # football is selected
            if user_input == 1:
                print("You Chose Football Trivia, Let's Begin! \n")
                # football question 1
                print("Question 1: Who won Super Bowl 51 in 2017? \n")
                print("Answers: \n1 ) Atlanta Falcons \n2 ) New England Patriots \n3 ) Oakland Raiders \n4 ) Baltimore Ravens \n")
                user_input = int(input("Enter Answer Here: "))
                print("")
                if user_input == 2:
                    print("Correct! The New England Patriots won \nSuper Bowl 51 in 2017 against the \nAtlanta Falcons. \n")
                    score = score + 1
                    print("score:", score)
                else:
                    print("Incorrect, The New England Patriots won  \nSuper Bowl 51 in 2017 against the \nAtlanta Falcons. \n")
                    print("score:", score)
                print("")
                # next question 1
                user_input = askingUsertoContinue()
                # football question 2
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank you for playing")
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
                    user_input = askingUsertoContinue()
                    # football question 3
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing!")
                        print("score:", score)
                    elif user_input == 1:
                        print("Question 3: Who is the starting quarterback \nof the packers as of 2019? \nAnswers: \n1) Derk Carr \n2) Tom Brady \n3) Aaron Rodgers \n4) Cam Newton \n")
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
                        print("Thank You for playing! \nYou have completed the football portion of \nSports Trivia '19!\n")
                        print("score:", score)
                        print("")
                        print("1) Return to Main Menu \n2) End Game \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("")
                            print("Thank You for playing sports trivia! \n")
                            print("score:", score)
            # basketball is selected
            elif user_input == 2:
                print("You Chose Basketball Trivia, Lets Begin! \n")
                # basketball question 1
                print("Question 1: What team did LeBron James \nget drafted to? \nAnswers: \n1 ) Clevland Cavaleirs \n2 ) Toronto Raptors \n3 ) Miami Heat \n4 ) Chicago Bulls \n")
                user_input = int(input("Enter Answer Here:"))
                print("")
                if user_input == 1:
                    print("Correct, LeBron James was drafted to the \nClevland Calvaliers in 2003. \n")
                    score = score + 1
                    print("Score:", score)
                    print("")
                else:
                    print("Incorrect, LeBron James was drafted to the \nClevland Cavaliers in 2003.\n")
                    print("Score:", score)
                    print("")
                # next question 3
                user_input = askingUsertoContinue()
                # exit for basketball question 1
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank You for playing!")
                # basketball question 2
                elif user_input == 1:
                    print("Question 2: Who holds the record for most \nNBA championships as of 2019?\nAnswers: \n1) LA Lakers \n2) Chicago Bulls \n3) Boston Celtics \n4) Golden State Worriors \n")
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
                    user_input = askingUsertoContinue()
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing!")
                    # basketball question 3
                    elif user_input == 1:
                        print("Question 3: How many NBA teams are there as of 2019 \nAnswers: \n1) 32 \n2) 30 \n3) 18 \n4) 46 \n")
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
                        print("Thank You for playing! \nYou have completed the basketball portion of \nSports Trivia '19!\n")
                        print("score:", score)
                        print("")
                        print("1) Return to Main Menu \n2) End Game \n")
                        user_input = int(input("Enter Answer Here:"))
                        print("")
                        # Exit for basketball question 3
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("Thank You for playing sports trivia!")
            # baseball is selected
            elif user_input == 3:
              print("You Chose Baseball Trivia! Let's Begin!")
              print("")
              #baseball question 1
              print("Question 1: What MLB team does Chris Sale pitch for as of 2019?")
              print("Answers:")
              print("1 ) Boston Red Sox")
              print("2 ) Chicago White sox")
              print("3 ) Tampa Bay Rays")
              print("4 ) CHicago Cubs")
              user_input = int(input("Enter Answer Here: "))
              print("")
              if user_input == 1:
                print("Correct, Chris Sale is the starting pitcher for the Boston Red Sox as of 2019.")
                print("")
                score = score + 1
                print("score:", score)
                print("")
              else:
                print("Incorrect, Chris Sale is the starting pitcher for the Boston Red Sox as of 2019.")
                print("")
                print("score:", score)
                print("")
              # next question 5
              user_input = askingUsertoContinue()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing sports trivia!")
              # baseball question 2
              elif user_input == 1:
                print("Question 2: What MLB team has the most World Series wins?")
                print("Answers:")
                print("1) Boston Red Sox")
                print("2) St. Louis Cardinals")
                print("3) New York Yankees")
                print("4) LA Dodgers")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 3:
                  print("Correct, the New York Yankees have the most World Series wins, with 27 total wins.")
                  print("")
                  score = score + 1
                  print("score:", score)
                  print("")
                else:
                  print("Incorrect, the New York Yankees have the most World Series wins, with 27 total wins.")
                  print("")
                  print("score:", score)
                  print("")
                # next question 6
                user_input = askingUsertoContinue()
                if user_input == 3:
                  user_wishes_to_continue = False
                  print("Thank you for playing Sports Triva!")
                  print("")
                  print("score:", score)
              # baseball question 3
                elif user_input == 1:
                  print("Question 3: What famous baseball player was the first to retire a number?")
                  print("Answers:")
                  print("1) Babe Ruth")
                  print("2) Lou Gehrig")
                  print("3) Jackie Robinson")
                  print("4) Tom Seaver")
                  user_input = int(input("Enter Ansewer Here: "))
                  print("")
                  if user_input == 2:
                    print("Correct, Lou Gehrig was the first MLB player to retire a number in 1939. His number was 4 and retired as a Yankee.")
                    print("")
                    score = score + 1
                    print("score:", score)
                    print("")
                  else:
                    print("Incorrect, Lou Gehrig was the first MLB player to retire a number in 1939. His number was 4 and retired as a Yankee.")
                    print("")
                    print("score:", score)
                    print("")
                  print("Thank You for playing the Baseball portion of Sports Trivia!"
                  "Would you like to return to main menu?")
                  print("1) Return to Main Menu")
                  print("2) End Game")
                  user_input = int(input("Enter Answer Here:"))
                  print("")
                  if user_input == 2:
                    user_wishes_to_continue = False
                    print("Thank You for playing!")
                    print("")
                    print("score:", score)
                    print("")
            # hockey is selected
            elif user_input == 4:
              print("You Chose hockey Trivia!")
              print("Lets Begin!")
              print("")
              # hockey question 1
              print("Question 1: What is the newest team to the NHL as of the 2019 season?")
              print("Answers:")
              print("1 ) Columbus Blue Jackets")
              print("2 ) Florida Panthers")
              print("3 ) Minnesota Wilds")
              print("4 ) Vagas Golden Knights")
              user_input = int(input("Enter Answer Here:"))
              print("")
              if user_input == 4:
                print("Correct, the Vagas Golden Knights are the newest team to the NHL as of the 2019 season.")
                score = score + 1
                print("")
                print("score:", score)
                print("")
              else:
                print("incorrect,the Vagas Golden Knights are the newest team to the NHL as of the 2019 season..")
                print("")
                print("score:", score)
                print("")
              # next question 7
              user_input = askingUsertoContinue()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing Sports Trivia!")
                print("")
                print("score:", score)
                print("")
              # hockey question 2
              elif user_input == 1:
                print("Question 2: What NHl team has the most Stanley Cup wins?")
                print("1) LA Kings")
                print("2) Tampa Bay Lightning")
                print("3) Montreal Canadiens")
                print("4) Ottawa Senators")
                user_input = int(input("Enter Ansewer Here: "))
                print("")
                if user_input == 3:
                  print("Correct, the Montreal Canadiens have won the most Stanly Cups, holding a totla of 24")
                  score = score + 1
                  print("")
                  print("score:", score)
                  print("")
                else:
                  print( "incorrect,the Montreal Canadiens have won the most Stanly Cups, holding a totla of 24")
                  print("")
                  print("score:", score)
                  print("")
                #next question 8
                user_input = askingUsertoContinue()
                if user_input == 3:
                  user_wishes_to_continue = False
                  print("Thank you for playing Sports Trivia!")
                  print("")
                  print("score:", score)
                  print("")
              # hockey question 3
                elif user_input == 1:
                  print("Question 2: How many games are played in regular season hockey?")
                  print("1) 32")
                  print("2) 94")
                  print("3) 82")
                  print("4) 86")
                  user_input = int(input("Enter Ansewer Here: "))
                  print("")
                  if user_input == 3:
                    print("Correct, there are only 82 regualar season games in hockey")
                    score = score + 1
                    print("")
                    print("score:", score)
                    print("")
                  else:
                    print( "incorrect,there are only 82 regular season games in hockey.")
                    print("")
                    print("score:", score)
                    print("")
                  print("Thank You for playing the hockey portion of Sports Trivia! Would you like to return to main menu?")
                  print("1) Return to Main Menu")
                  print("2) End Game")
                  user_input = int(input("Enter Answer Here:"))
                  print("")
                  print("score:", score)
                  print("")
                  if user_input == 2:
                    user_wishes_to_continue = False
                    print("Thank You for playing Sports Trivia!")
                    print("")
                    print("score:", score)
                    print("")
            # soccer is selected
            elif user_input == 5:
              print("You Chose soccer Trivia!")
              print("Lets Begin!")
              # soccer question 1
              print("Question 1: How many professional soccer luages are there in the world as of 2019?")
              print("Answers:")
              print("1 ) 18")
              print("2 ) 21")
              print("3 ) 23")
              print("4 ) 4")
              user_input = int(input("Enter Answer Here:"))
              if user_input == 2:
                print("Correct, there are 21 professional soccer leagues in the world as of 2019.")
                score = score + 1
                print("score:", score)
              else:
                print("Incorrect,there are 21 professional soccer leagues in the world as of 2019.")
                print("score:", score)
              # next question 9
              user_input = askingUsertoContinue()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing Sports Trivia!")
                print("")
                print("score:", score)
              # soccer question 2
              elif user_input == 1:
                print("Question 2: How many total players on the fild during a game?")
                print("1) 11")
                print("2) 22")
                print("3) 16")
                print("4) 9")
                user_input = int(input("Enter Ansewer Here: "))
                if user_input == 2:
                  print("Correct, there are a total 22 players on the fild at once during a game. 11 players per team")
                  score = score + 1
                  print("score:", score)
                else:
                  print( "Incorrect,there are a total 22 players on the fild at once during a game. 11 players per team")
                  print("score:", score)
              # next question 10
              user_input = askingUsertoContinue()
              if user_input == 3:
                user_wishes_to_continue = False
                print("Thank you for playing sports Trivia!")
                print("")
                print("score:", score)
              # soccer question 3
              elif user_input == 1:
                print("Question 3: How many teams are in the Primer Luage as of 2019?")
                print("1) 20")
                print("2) 22")
                print("3) 16")
                print("4) 31")
                user_input = int(input("Enter Ansewer Here: "))
                if user_input == 1:
                  print("Correct, there are only 20 teams in the primer Luage as of 2019")
                  score = score + 1
                  print("score:", score)
                else:
                  print( "Incorrect,there are only 20 teams in the primer Luage as of 2019")
                  print("score:", score)
                print(
                "Thank You for playing the football portion of Sports Trivia! Would you like to return to ")
                print("1) Return to Main Menu")
                print("2) End Game")
                user_input = int(input("Enter Answer Here:"))
                print("")
                print("score:", score)
                print("")
                if user_input == 2:
                  user_wishes_to_continue = False
                  print("Thank You for playing Sports Trivia!")
                  print("")
                  print("score:", score)
        # info from main menu
        elif main_menu == 2:
            print("Game Info")
            print(
                "Thank you for playing Sports Trivia! This trivia game is"
                " a basic knowledge quiz about various sports.\nIn the "
                "Sports"
                " options menu you can select one of 5 different sports to be"
                " quized on.\nEach sport has 3 questions and you will be"
                " awarded 1 point for every question correctly answered."
                " \nWhen you end the game you will recive a * for how many "
                "points you have earned. Challenge your friends to see who"
                " knows the most across all 5 sports!")
            print(" ")
            print("Please select an option below")
            print("1) return to Main Menu")
            print("2) Exit game")
            user_input = int(input("Enter menu option desired here:"))
            if user_input == 2:
                user_wishes_to_continue = False
                print("Thank You for playing Sports trivia!")
                print("")
                print("score:", score)
        # exit from Main Menu
        elif main_menu == 3:
            user_wishes_to_continue = False
            print("Thank You for playing Sports Trivia!")
            print("")
            print("score:", score)

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

main()
