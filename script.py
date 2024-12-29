# Last Edited on 28/12/2024




# ------------- SETUP ------------- #
import os, time
import module
from pack import pack

pack('script.py', True)

os.system('cls')

def timer(s):
        while s: 
                time.sleep(1)
                s -= 1

# ---------------------------------------------------------------------------- #




def main():
        print(f"\033[38;2;212;212;212m", end="")
        print(f"\n\nOPERATIONS ON, AND USING LISTS AND STRINGS\n")

        print(f"Enter 1 to REMOVE ALL OCCURRENCES OF A PARTICULAR CHARACTER FROM A GIVEN STRING")
        print(f"Enter 2 to CHECK NO. OF INSTANCES OF A PARTICULAR CHARACTER IN A STRING")
        print(f"Enter 3 to SORT POSITIVE AND NEGATIVE INTEGERS FROM A SET OF NUMBERS")
        print(f"Enter 4 to MERGE TWO LISTS WITHOUT ANY DUPLICATE VALUES")
        print(f"Enter 5 to REMOVE ALL CHARACTERS APPEARING MORE THAN ONCE AND MAKE A NEW SET OF THEM ")
        print(f"Enter 6 to PERFORM OPERATIONS ON A LIST (Python) FROM A LIST (general)\n\n")

        while True:
                listSelector = input(f"Enter your selection from the above list (Exceding values will be adjusted): \033[38;2;255;165;0m")
                print(f"\033[38;2;212;212;212m", end="")

                try:
                        listSelector = int(listSelector)
                 
                        if listSelector < 0:
                                print(f"Input out of range. Being set to 1")
                                print(f"\n\n---------------------------------------------")
                                module.charRemover()
                        elif listSelector > 6:
                                print(f"Input out of range. Being set to 6")
                                print(f"\n\n---------------------------------------------\n\n")
                                module.listOperations()
                        elif listSelector == 1:
                                print(f"You selected OPTION 1")
                                print(f"\n\n---------------------------------------------")
                                module.charRemover()
                        elif listSelector == 2:
                                print(f"You selected OPTION 2")
                                print(f"\n\n---------------------------------------------")
                                module.charInstance()
                        elif listSelector == 3:
                                print(f"You selected OPTION 3")
                                print(f"\n\n---------------------------------------------")
                                module.sortBySign()
                        elif listSelector == 4:
                                print(f"You selected OPTION 4")
                                print(f"\n\n---------------------------------------------")
                                module.mergeListNoDupe()
                        elif listSelector == 5:
                                print(f"You selected OPTION 5")
                                print(f"\n\n---------------------------------------------")
                                module.filterDupes()
                        else:
                                print(f"You selected OPTION 6")
                                print(f"\n\n---------------------------------------------\n\n")
                                module.listOperations()

                        break
                except ValueError:
                        print(f"\nInvalid Input\n")
                except EOFError:
                        print(f"\nInvalid Input\n")                

        print(f"\n\n\n---------------------------------------------")
        print(f"\n\nType \033[38;2;255;165;0m'CLS'\033[38;2;212;212;212m to clear screen and continue")
        print(f"Hit \033[38;2;255;165;0mENTER\033[38;2;212;212;212m to continue without clearing screen")
        print(f"Type \033[38;2;255;165;0m'END'\033[38;2;212;212;212m to terminate")
        print(f"\n\033[31mANY OTHER ENTRY WILL TERMINATE THE PROGRAM\033[38;2;212;212;212m\n")

        continueChoice = input(f"Enter any command from the above list (Case insensitive): \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")

        if continueChoice.lower() == 'cls':
                for i in range(1, 4):
                        print(f"Clearing screen in\033[38;2;255;165;0m", 4-i, "\033[38;2;212;212;212m")
                        timer(1)
                        print(f"\033[F\033[K", end="")

                os.system('cls')

                main()
        elif continueChoice.replace(" ", "") == '':
                print(f"\033[F\033[KEnter any command from the above list: \033[38;2;255;165;0m*BLANK*\033[38;2;212;212;212m")
                print(f"\n\n\n---------------------------------------------\n\n\n")
                main()
        elif continueChoice.lower() == 'end':
                print(f"\nTHANK YOU")

                for i in range(1, 4):
                        print(f"Terminating in\033[38;2;255;165;0m", 4-i, "\033[38;2;212;212;212m")
                        timer(1)
                        print(f"\033[F\033[K", end="")

                os.system('cls')
        else:
                print(f"\n\033[31mInvalid Input. Terminated\033[38;2;212;212;212m")
main()



