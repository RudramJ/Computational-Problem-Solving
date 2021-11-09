"""
file: transformer.py

description: This program reads the two file of
message to be sent and transformations to be applied.
And outputs the result file based on transformation done
on the message.

language: python3
author: Rudram Joshi
author: Moinuddin memon

Our method returns the reverse of the string to be encrypted
The instruction is defined as "O"
Example: Message = CANAL , Instruction = O, Operation = e/d
Result = LANAC

"""
import sys

def reverse(str):
    """
    This method increments every even elements in the string
    :return:    Reverse of string
    """
    return str[::-1]

def shifts(str, i, k = 0):
    """
    This method shifts the elements in the string
    according to the user specified location to encrypt and
    decrypt the message
    :param str: Value to be encrypted/decrypted
    :param i:   Index at which to perform operation
    :param k:   Number of groups
    :return:    Result after applying shifting
    """
    if k == 0:
        if str[i] == "Z":
            return str[:i]+chr(ord(str[i])-25)+str[i+1:]
        else:
            return str[:i]+chr(ord(str[i])+1)+str[i+1:]
    else:
        if ord(str[i])+k > 90:
            index = 65+((ord(str[i])+k) % 90)
            return str[:i]+chr(index)+str[i+1:]
        else:
            index = (ord(str[i])+k)
            return str[:i] + chr(index) + str[i + 1:]

def rotate(str, n = 0):
    """
    This methods rotates a string from left to right
    :param str:  Value to be encrypted/decrypted
    :param n:    Number of times to rotate
    :return:     Result of string after applying rotation
    """
    if n == 0:
        return str[-1] + str[:-1]
    elif n >= 1:
        for _ in range(n):
            str = str[-1] + str[:-1]
        return str
    else:
        for i in range(abs(n)):
            str = str[1:]+str[0]
        return str

def duplicate(str,i,k=0):
    """
    This methods duplicates the element
    specified at the index
    :param str: Value to be encrypted/decrypted
    :param i:   Index to perform
    :param k:   Number of elements to be performed on
    :return:    The result after duplicating
    """
    duplicate_str = ""
    if k == 0:
        return str[:i]+str[i]+str[i]+str[i+1:]
    else:
        for _ in range(k+1):
            duplicate_str += str[i]
        return str[:i]+duplicate_str+str[i+1:]

def swap(str, i, j):
    """
    This method swaps the message with user
    specified location
    :param str: Value to be encrypted/decrypted
    :param i:   Index to perform
    :param j:   Exponent
    :return:    The result after swapping
    """
    ith_char=str[i]
    jth_char=str[j]
    return str[:i]+jth_char+str[i+1:j]+ith_char+str[j+1:]

def swap_groups(str, g, i, j):
    """
    This method swaps the message in groups with user
    specified location
    :param str: Value to be encrypted/decrypted
    :param g:   Number of groups
    :param i:   Index to perform
    :param j:   Exponent
    :return:    The result after swapping
    """
    group_length=len(str)//g
    k1 = []
    for b in range(0,len(str),group_length):
        k1.append(str[b:b+group_length])
    k1[i], k1[j] = k1[j], k1[i]
    return "".join(k1)

def decrypt_dupliacte(str,i,k=0):
    """
    This method returns the decrypted value of duplicate
    message done earlier
    :param str: Value to be encrypted/decrypted
    :param i:   Index to perform
    :param k:   Number of elements to be performed on
    :return:    The decrpytion of duplicate values at
                user specified location
    """
    if k == 0:
        return str[:i]+str[i+1:]
    else:
        return str[:i]+str[i+k:]

def get_result(instructList, msgList, myOperation ):
    """
    This methods returns the messages with the set of operation
    done on it specified by the user.
    :param instructList: List of instruction
    :param msgList:      List of messages
    :param myOperation:  Whether to encrypt or decrypt
    :return:             List of message with applied operations
    """
    myReturnList = []
    for element in range (0, len(instructList)):
        myData = msgList[element]
        anInstruct = instructList[element]
        instructionArray = anInstruct.split(';')

        for i in instructionArray:
            if i.startswith("T"):
                if "(" in i:
                    x = int(i[2])
                    temp = i[4:]
                    j = temp.split(',')
                    index = int(j[0])
                    exponent = int(j[-1])
                    if(myOperation == 'e'):
                        myData = swap_groups(myData, x, index, exponent)
                    else:
                        myData = swap_groups(myData, x, exponent, index)
                else:
                    j = i.split(',')
                    index = int(j[0][1])
                    exponent = int(j[-1])
                    if (myOperation == 'e'):
                        myData = swap(myData, index, exponent)
                    else:
                        myData = swap(myData, exponent, index)

            if i.startswith("S"):
                if len(i.split(',')) == 1:
                    if (myOperation == 'e'):
                        myData = shifts(myData, int(i[1]))
                    else:
                        myData = shifts(myData, -int(i[1]))
                else:
                    if (myOperation == 'e'):
                        myData = shifts(myData, int(i.split(',')[0][1]), int(i.split(',')[1]))
                    else:
                        myData = shifts(myData, int(i.split(',')[0][1]), -int(i.split(',')[1]))

            if i.startswith("D"):
                if len(i.split(',')) == 1:
                    if (myOperation == 'e'):
                        myData = duplicate(myData, int(i[1]))
                    else:
                        myData = decrypt_dupliacte(myData, int(i[1]))
                else:
                    if (myOperation == 'e'):
                        myData = duplicate(myData, int(i.split(',')[0][1]), int(i.split(',')[1]))
                    else:
                        myData = decrypt_dupliacte(myData, int(i.split(',')[0][1]), int(i.split(',')[1]))
            if i.startswith("R"):
                if len(i) == 1:
                    myData = rotate(myData)
                else:
                    if (myOperation == 'e'):
                        myData = rotate(myData, int(i[2]))
                    else:
                        myData = rotate(myData, -int(i[2]))
            if i.startswith("O"):
                myData = reverse(myData)
        myReturnList.append(myData)
    return myReturnList

def main():
    """
    The main method
    This method reads the names of message file and
    instruction file and calls the get_result method to
    get the result. Then the message is written in a file
    whose name is provided by the user.
    :return: null
    """

    if(len(sys.argv) > 1):
        messageFile = (sys.argv[1])
        instructionFile = sys.argv[2]
        outputFile = sys.argv[3]
        operationToPerform = sys.argv[4]
    else:
        messageFile = input("Enter the name of message file with extension: ")
        instructionFile = input("Enter the name of instruction file with extension: ")
        outputFile = input("Enter the name of output file with extension: ")
        operationToPerform = input("Enter whether to encrypt or decrypt(d/e): ")

    try:
        with open(messageFile) as f:
            myMessages = f.read()
        with open(instructionFile) as ins:
            myInstruction = ins.read()

    except FileNotFoundError:
        print("Wrong file or file path")
        print("follow this order: message file instruction file output file e/d")
        exit()
    if not outputFile:
        print("Give proper output file name.")
        exit()
    if(operationToPerform == 'e' or operationToPerform == 'd'):
        pass
    else:
        print("Check for input parameters!!.")
        exit()

    myMessagesList = myMessages.split('\n')
    myInstructionList = myInstruction.split('\n')

    myResultList = get_result(myInstructionList, myMessagesList, operationToPerform)

    with open(outputFile, "w") as output:
        for myMessage in myResultList:
            print("myResultList: ", myMessage)
            output.write("%s\n" % myMessage)
    output.close()

if __name__ == '__main__':
    main()