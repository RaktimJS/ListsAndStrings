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

# Last Edited: 16/12/2024




def main():
        print("OPERATIONS ON, AND USING LISTS AND STRINGS\n")

        print("Enter 1 to REMOVE ALL OCCURRENCES OF A PARTICULAR CHARACTER FROM A GIVEN STRING")
        print("Enter 2 to CHECK NO. OF INSTANCES OF A PARTICULAR CHARACTER IN A STRING")
        print("Enter 3 to SORT POSITIVE AND NEGATIVE INTEGERS FROM A SET OF NUMBERS")
        print("Enter 4 to MERGE TWO LISTS WITHOUT ANY DUPLICATE VALUES")
        print("Enter 5 to REMOVE ALL CHARACTERS APPEARING MORE THAN ONCE AND MAKE A NEW SET OF THEM ")
        print("Enter 6 to PERFORM OPERATIONS ON A LIST (Python) FROM A LIST (general)\n\n")

        while True:
                listSelector = input("Enter your selection from the above list (Exceding values will be adjusted): ")

                try:
                        listSelector = int(listSelector)
                        
                        if listSelector < 0:
                                print("Input out of range. Being set to 1")
                                print("\n\n------------------------------")
                                module.charRemover()
                        elif listSelector > 6:
                                print("Input out of range. Being set to 6")
                                print("\n\n------------------------------\n\n")
                                module.listOperations()
                        elif listSelector == 1:
                                print("You selected OPTION 1")
                                print("\n\n------------------------------")
                                module.charRemover()
                        elif listSelector == 2:
                                print("You selected OPTION 2")
                                print("\n\n------------------------------")
                                module.charInstance()
                        elif listSelector == 3:
                                print("You selected OPTION 3")
                                print("\n\n------------------------------")
                                module.sortBySign()
                        elif listSelector == 4:
                                print("You selected OPTION 4")
                                print("\n\n------------------------------")
                                module.mergeListNoDupe()
                        elif listSelector == 5:
                                print("You selected OPTION 5")
                                print("\n\n------------------------------")
                                module.filterDupes()
                        else:
                                print("You selected OPTION 6")
                                print("\n\n------------------------------\n\n")
                                module.listOperations()
                                break
                except ValueError:
                        print("\nInvalid Input\n")
                except EOFError:
                        print("\nInvalid Input\n")                

        while True:
                try:
                        continuationSelector = input("\n\nEnter 1 to continue, 0 to terminate: ")
                        continuationSelector = int(continuationSelector)

                        if continuationSelector == 1:
                                system('cls')
                                main()
                        elif continuationSelector == 0:
                                system('cls')
                                print("THANK YOU!")
                                timer(3)
                                system('cls')
                                break
                except ValueError:
                        print("\nInvalid Input. Terminating\n")
                        timer(3)
                        system('cls')
                        break
                except EOFError:
                        print("\nInvalid Input. Terminating\n")
                        timer(3)
                        system('cls')
                        break
        
main()



