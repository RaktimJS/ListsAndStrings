"""

TURN LINE WRAPPING OFF FOR A BETTER VIEW

+-------------------------------------------------------------------+
|***------------   MODULE   ------------***                         |
|                                                                   |
|                                                                   |
|Author: Raktim JS                                                  |
|Institution: Pathsala Public School, Pathsala, Seuj Nagar, 781325  |
|Date: 15/12/2024                                                   |
|Email: raktimunreal4@gmail.com                                     |
|                                                                   |
|                                                                   |
|                        DO NOT PLAGIARISE                          |
|                                                                   |
|                                                                   |
|Includes functions to:                                             |
|        1. Remove all occurrences of a particular character from a |
|           given string                                            |
|        2. Check the no. of instances of a particular character in |
|           a string                                                |
|        3. Take a list of integers and create two different lists  |
|           of positive integers and negative integers              |
|        4. Merge two lists without duplicate values                |
|        5. Remove all duplicates in a given list and return another|
|           list of only duplicates                                 |
|        6. CHECK module1.py                                        |
+-------------------------------------------------------------------+

Last Edited on 27/12/2024

"""




from random import randint

elements = [
        'Algorithm', 'Compiler', 'Debug', 'Firmware', 'Cloud',
        'Cache', 'Kernel', 'Pixel', 'Encryption', 'Bandwidth',
        'Circuit', 'Server', 'Protocol', 'GPU', 'Database',
        'Blockchain', 'Syntax', 'Java', 'Python', 'API',
        'Bitrate', 'Quantum', 'Emulator', 'Virtualization','Cryptography',

        'Russia', 'United States', 'Japan', 'France', 'Germany',
        'Australia', 'South Korea', 'United Kingdom', 'Israel', 'Brazil',
        'South Africa', 'Singapore', 'Indonesia', 'Vietnam', 'Saudi Arabia',
        'United Arab Emirates', 'Qatar', 'Nepal', 'Bhutan', 'Sri Lanka',
        'Mauritius', 'Seychelles', 'Mexico', 'Thailand', 'Kenya',

        'Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Kolkata',
        'Chennai', 'Jaipur', 'Ahmedabad', 'Pune', 'Lucknow',
        'Kanpur', 'Surat', 'Bhopal', 'Indore', 'Patna',
        'Ranchi', 'Guwahati', 'Dehradun', 'Chandigarh', 'Thiruvananthapuram',
        'Bhubaneswar', 'Varanasi', 'Amritsar', 'Jodhpur', 'Agra',

        'Arjun', 'Priya', 'Neha', 'Rahul', 'Ishita',
        'Rohan', 'Kavya', 'Varun', 'Ananya', 'Akash',
        'Riya', 'Rohit', 'Sakshi', 'Aman', 'Sneha',
        'Aarav', 'Divya', 'Karan', 'Shruti', 'Aditya',
        'Meera', 'Yash', 'Simran', 'Sagar', 'Pooja'
]

def randList():
        noOfElements = randint(5, 7)
        output = []
        i = 0

        while i < noOfElements:
                itemSelector = randint(0, len(elements) - (i + 1))
                output.append(elements[itemSelector])
                elements.pop(itemSelector)
                i += 1

        elements.append(output)

        return output

def charRemover():
        print(f"\n\n")

        print(f"REMOVES A DESIRED CHARACTER FROM A STRING GIVEN BY USER")
        print(f"_______________________________________________________\n")

        str = input(f"Enter a string: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")
        toBeRemoved = input(f"Enter the character to be removed from the string (Case sensitive): \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")
        
        print(f"\n")

        if len(toBeRemoved) == 1:
                if toBeRemoved not in str:
                        print(f"\"{toBeRemoved}\" is not present in {str}")
                else:
                        print(f"{str} with all \"{toBeRemoved}\" removed is: ", end="")

                        for i in str:
                                if i == toBeRemoved:
                                        pass
                                else:
                                        print(i, end="")
        else:
                print(f"Can't remove multiple characters at a time")

def charInstance():
        print(f"\n\n")

        print(f"CHECKS NUMBER OF INSTANCES OF A PARTICULAR CHARACTER IN A STRING")
        print(f"________________________________________________________________\n")

        str = input(f"Enter a string: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")

        targetChar = input(f"Enter the character to count instances of: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")

        str = str.upper()
        targetChar = targetChar.upper()

        if len(targetChar) == 1:
                if targetChar not in str:
                        print(f"\n\"{targetChar}\" is not present in {str}")
                else:
                        instance = 0
                        
                        for i in str:
                                if i == targetChar:
                                        instance += 1

                print(f"\nNumber of instances of \"{targetChar}\" in {str} is \033[38;2;255;165;0m{instance}\033[38;2;212;212;212m")
        else:
                print(f"\nCan't remove multiple characters at a time")

def sortBySign():
        print(f"\n\n")

        print(f"CREATES 2 LISTS OF POSITIVE AND NEGATIVE INTEGERS FROM A LIST OF NUMBERS")
        print(f"________________________________________________________________________\n")

        numList = []
        positiveList = []
        negativeList = []

        zeroCounter = 0
        i = 0

        inputTaker = ""

        while True:
                try:
                        inputTaker = input(f"Enter a number (Type 'END' to end. Case sensitive): \033[38;2;255;165;0m")
                        print(f"\033[38;2;212;212;212m", end="")
                        
                        if inputTaker != "END":
                                inputTaker = int(inputTaker)
                                numList.append(inputTaker)
                                i += 1
                        else:
                                break

                except ValueError:
                        print(f"\nInvalid input\n")
                except EOFError:
                        print(f"\nInvalid Input\n")
        

        for i in numList:
                if i > 0:
                        positiveList.append(i)
                elif i < 0:
                        negativeList.append(i)
                else:
                        zeroCounter += 1

        if len(numList) == 0:
                print(f"The list is empty. Nothing to show")
        else:
                print(f"\n\nThe list you have entered are: {numList}")


                if len(positiveList) == 0:
                        print(f"No number in the above list is positive")
                else:
                        print(f"\nThe list of positive numbers are: {positiveList}")


                if len(negativeList) == 0:
                        print(f"No number in the above list is negative")
                else:
                        print(f"The list of negative numbers are: {negativeList}")


                if zeroCounter == 0:
                        print(f"There is no appearence of 0 is the list")
                else:
                        print(f"Total number of appearence of 0 is: {zeroCounter}")

def mergeListNoDupe():
        print(f"\n\n")

        print(f"MERGE 2 LISTS SUCH THAT THE FINAL LIST HAS NO DUPLICATE VALUES")
        print(f"______________________________________________________________\n")

        numList = []
        numList2 = []
        i = 0

        inputTaker = ""

        print(f"FIRST LIST:")

        while True:
                try:
                        inputTaker = input(f"    Enter a number (Type 'END' to end. Case sensitive): \033[38;2;255;165;0m")
                        print(f"\033[38;2;212;212;212m", end="")
                        
                        if inputTaker != "END":
                                inputTaker = int(inputTaker)
                                numList.append(inputTaker)
                                i += 1
                        else:
                                break

                except ValueError:
                        print(f"\n       Invalid input\n")
                except EOFError:
                        print(f"\n       Invalid Input\n")

        print(f"SECOND LIST:")

        while True:
                try:
                        inputTaker = input(f"    Enter a number (Type 'END' to end. Case sensitive): \033[38;2;255;165;0m")
                        print(f"\033[38;2;212;212;212m", end="")
                        
                        if inputTaker != "END":
                                inputTaker = int(inputTaker)
                                numList2.append(inputTaker)
                                i += 1
                        else:
                                break

                except ValueError:
                        print(f"\n       Invalid input\n")
                except EOFError:
                        print(f"\n       Invalid Input\n")
                
        if len(numList) != 0:
                print(f"\nFirst List: ", numList)
        else:
                print(f"\nFirst List is \033[38;2;255;165;0mEMPTY\033[38;2;212;212;212m")


        if len(numList2) != 0:
                print(f"Second List:", numList2)
        else:
                print(f"Second List is \033[38;2;255;165;0mEMPTY\033[38;2;212;212;212m")
        


        numList.extend(numList2)

        newFullList = []

        for k in numList:
                if k in newFullList:
                        pass
                else:
                        newFullList.append(k)

        if len(newFullList) != 0:
                print(f"\nThe 2 lists joined together without any repetition of elements is:", newFullList)
        else:
                print(f"\nBoth lists are empty")
        

def filterDupes():
        print(f"\n\n")

        print(f"CREATE A LIST OF ALL CHARACTERS THAT REPEAT IN A STRING")
        print(f"_______________________________________________________\n")

        str = input(f"Enter a string: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")
        str = str.replace(" ", "")
        str = str.upper()

        placeholder = str

        singleAppearence = []
        multiAppearence = []
        listOfChars = list(str)

        for i in listOfChars:
                if listOfChars.count(i) == 1 and i not in singleAppearence:
                        singleAppearence.append(i)
                elif listOfChars.count(i) > 1 and i not in multiAppearence:
                        multiAppearence.append(i)


        print(f"\nThe list of elements that appear only once in {placeholder}: {sorted(singleAppearence)}")

        if len(multiAppearence) != 0:
                print(f"The list of elements that appear more that once in {placeholder}: {sorted(multiAppearence)}")
        else:
                print(f"There is no repeating character in {placeholder}")



"""

/*----------LIST OPERATIONS----------*/

"""



listList = list()

randomList = randList()
newList = randomList



# Appender
def appender():
        print(f"\n\n        APPEND VALUES")
        print(f"        -------------")
        value = input(f"        Enter a value: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")
        newList.append(value)

        print(f"\n        The new list is: \n        ", newList)



# Value Inserter
def valueInserter():
        print(f"\n\n\n        INSERT VALUES")
        print(f"        -------------")
        elem = input(f"        Enter an value: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")

        print(f"\n        If position entered exceeds list length. It will be set to it to 1 more than list length")


        while True:
                pos = input(f"\n        Enter the position you want \"{elem}\" to be at: \033[38;2;255;165;0m")
                print(f"\033[38;2;212;212;212m", end="")

                try:
                        pos = int(pos)
                        pos = pos
                        break
                except ValueError:
                        print(f"\n        Invalid input\n")
                except EOFError:
                        print(f"\n        Invalid Input\n")

        newList.insert(pos - 1, elem)

        if pos > len(newList):
                print(f"\n        The list with \"{elem}\" inserted at position {len(newList)} is: \n        ", newList)
        else: 
                print(f"\n        The list with \"{elem}\" inserted at position {pos} is: \n        ", newList)



# List Appender
def listAppender():
        print(f"\n\n\n        APPEND LIST")
        print(f"        -----------")

        numList = []
        
        i = 0

        while True:
                inputTaker = input(f"        Enter a value (Type 'END' to end. Case sensitive): \033[38;2;255;165;0m")
                print(f"\033[38;2;212;212;212m", end="")
                        
                if inputTaker != "END":
                        numList.append(inputTaker)
                        i += 1
                else:
                        break

        newList.append(numList)

        print(f"\n        The new list is: \n        ", newList)



# Modify by position
def modfier():
        print(f"\n\n\n        MODIFY ELEMENTS")
        print(f"        ---------------")

        while True: 
                try:
                        posVal = input(f"        Enter the position of the value you want to modify: \033[38;2;255;165;0m")
                        print(f"\033[38;2;212;212;212m", end="")
                        posVal = int(posVal)
                        posVal = posVal - 1
                        break;
                except ValueError:
                        print(f"\n        Invalid input\n")
                except EOFError:
                        print(f"\n        Invalid Input\n")
        
        elemVal = input(f"        Enter the new value: \033[38;2;255;165;0m")
        print(f"\033[38;2;212;212;212m", end="")

        newList.pop(posVal)
        newList.insert(posVal, elemVal)

        print(f"        The modified list is: \n        ", newList)



# Delete Element By Position
def delByPos():
        print(f"\n\n\n        DELETE ELEMENT BY POSITION")
        print(f"        --------------------------")

        while True: 
                try:
                        posVal = input(f"        Enter the position: \033[38;2;255;165;0m")
                        print(f"\033[38;2;212;212;212m", end="")
                        posVal = int(posVal)
                        posVal = posVal - 1
                        break;
                except ValueError:
                        print(f"\n        Invalid input\n")
                except EOFError:
                        print(f"\n        Invalid Input\n")
        
        newList.pop(posVal)

        print(f"        The modified list is: \n        ", newList)



# Delete Element By Value
def delByVal():
        print(f"\n\n\n        DELETE ELEMENT BY VALUE")
        print(f"        -----------------------")

        while True:
                value = input(f"        Enter the value: \033[38;2;255;165;0m")
                print(f"\033[38;2;212;212;212m", end="")

                if value in newList:
                        newList.remove(value)
                        break;
                else:
                        print(f"        Entered value is not in the list")

        print(f"        The updated list is: \n        ", newList)



# Ascending Sort
def ascendingSorter():
        print(f"\n\n\n        ASCENDING SORT")
        print(f"        --------------")

        for i in newList:
                if type(i) == list:
                        listList.append(newList[newList.index(i)])
                        newList.remove(i)
                        break

        newList.sort(key = str.upper)
        newList.extend(listList)

        print(f"        Sorted in ascending order: \n        ", end="")
        print(newList)
        


# Descending Sort
def descendingSorter():
        print(f"\n\n\n        DESCENDING SORT")
        print(f"        ---------------")

        print(f"        Sorted in descending order: \n        ", end="")
        newList.reverse()
        print(newList)



# Parent List Operation Function
def listOperations():
        print(f"PERFORM VARIOUS OPERATIONS TO A LIST")
        print(f"____________________________________\n")

        print(f"        Original List: ", newList)

        appender()
        valueInserter()
        listAppender()
        modfier()
        delByPos()
        delByVal()
        ascendingSorter()
        descendingSorter()

        # Display
        print(f"\n\n\n")
        print(f"        The list after all different operations is: \n        ", newList)



