# Last Edited on 18/12/2024




import module
import time
from os import system as system
from os import remove as remove

system('pyinstaller --onefile --distpath "." script.py')
system('rmdir /s /q "build"')
system('rmdir /s /q "dist"')
system('rmdir /s /q "__pycache__"')
remove('script.spec')
system('cls')

def timer(s):
        while s: 
                time.sleep(1)
                s -= 1




def main():
        print("OPERATIONS ON, AND USING LISTS AND STRINGS\n")

        print("Enter 1 to REMOVE ALL OCCURRENCES OF A PARTICULAR CHARACTER FROM A GIVEN STRING")
        print("Enter 2 to CHECK NO. OF INSTANCES OF A PARTICULAR CHARACTER IN A STRING")
        print("Enter 3 to SORT POSITIVE AND NEGATIVE INTEGERS FROM A SET OF NUMBERS")
        print("Enter 4 to MERGE TWO LISTS WITHOUT ANY DUPLICATE VALUES")
        print("Enter 5 to REMOVE ALL CHARACTERS APPEARING MORE THAN ONCE AND MAKE A NEW SET OF THEM ")
        print("Enter 6 to PERFORM OPERATIONS ON A LIST (Python) FROM A LIST (general)\n\n")

        while True:
                listSelector = input("Enter your selection from the above list (Exceding values will be adjusted): \033[38;2;255;165;0m")
                print("\033[36m", end="")

                try:
                        listSelector = int(listSelector)
                        
                        if listSelector < 0:
                                print("Input out of range. Being set to 1")
                                print("\n\n---------------------------------------------")
                                module.charRemover()
                        elif listSelector > 6:
                                print("Input out of range. Being set to 6")
                                print("\n\n---------------------------------------------\n\n")
                                module.listOperations()
                        elif listSelector == 1:
                                print("You selected OPTION 1")
                                print("\n\n---------------------------------------------")
                                module.charRemover()
                        elif listSelector == 2:
                                print("You selected OPTION 2")
                                print("\n\n---------------------------------------------")
                                module.charInstance()
                        elif listSelector == 3:
                                print("You selected OPTION 3")
                                print("\n\n---------------------------------------------")
                                module.sortBySign()
                        elif listSelector == 4:
                                print("You selected OPTION 4")
                                print("\n\n---------------------------------------------")
                                module.mergeListNoDupe()
                        elif listSelector == 5:
                                print("You selected OPTION 5")
                                print("\n\n---------------------------------------------")
                                module.filterDupes()
                        else:
                                print("You selected OPTION 6")
                                print("\n\n---------------------------------------------\n\n")
                                module.listOperations()
                        
                        break
                except ValueError:
                        print("\nInvalid Input\n")
                except EOFError:
                        print("\nInvalid Input\n")                

        print("\n\n\n---------------------------------------------")
        print("\n\nType \033[38;2;255;165;0m'CLS'\033[36m to clear screen and continue")
        print("Hit \033[38;2;255;165;0mENTER\033[36m to continue without clearing screen")
        print("Type \033[38;2;255;165;0m'END'\033[36m to terminate")
        print("\n\033[31mANY OTHER ENTRY WILL TERMINATE THE PROGRAM\033[36m\n")

        continueChoice = input("Enter any command from the above list: \033[38;2;255;165;0m")
        print("\033[36m", end="")
        
        if continueChoice.lower() == 'cls':
                for i in range(1, 4):
                        print("Clearing screen in \033[38;2;255;165;0m", 4-i, "\033[36m")
                        timer(1)
                        print("\033[F\033[K", end="")

                system('cls')

                main()
        elif continueChoice.replace(" ", "") == '':
                print("\033[F\033[KEnter any command from the above list: \033[38;2;255;165;0m*BLANK*\033[36m")
                print("\n\n\n---------------------------------------------\n\n\n")
                main()
        elif continueChoice.lower() == 'end':
                print("\nTHANK YOU")

                for i in range(1, 4):
                        print("Terminating in \033[38;2;255;165;0m", 4-i, "\033[36m")
                        timer(1)
                        print("\033[F\033[K", end="")
        else:
                print("\n\033[36mInvalid Input. Terminated")
main()



