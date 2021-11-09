"""
file: genetester.py

description: This program provides the test cases of
operations of gene slicing, snipping and joining. A strand of DNA
is represented as a linked list

language: python3
author: Rudram Joshi
author: Moinuddin memon

"""
# importing the class DNAList
from dnalist import DNAList

def append_test(dna1, dna2):
    """
    This method tests the append method
    from class DNAList
    :return: None
    """
    print("========append=============")
    dna1.append("C")
    dna1.append("A")

    dna2.append("C")
    dna2.append("T")
    dna2.append("T")
    # The empty item is ignored in append
    dna2.append("")
    print("dna1: ",dna1)
    print("dna2: ",dna2)
    print("========append=============")
    print()

def join_test(dna1, dna2):
    """
    This method tests the join method
    from class DNAList
    :param dna1: First gene list
    :param dna2: Second gene list
    :return: None
    """
    print("========join=============")
    # Joining the two non empty list
    dna1.join(dna2)
    print("dna1.join(dna2): ",dna1)

    # Joining the two empty list
    newDna = DNAList()
    newDna1 = DNAList()
    newDna.join(newDna1)
    print("newDna.join(newDna1): ", newDna)

    # Joining the one empty list to non empty list
    dna1.join(newDna)
    print("dna1.join(newDna): ",dna1)

    # Joining the non-empty list to empty list
    newDna.join(dna1)
    print("newDna.join(dna1): ", newDna)

    print("========join=============")
    print()

def splice_test():
    """
    This method tests the splice method
    from class DNAList
    This method only inserts the other gene after first character
    (0th index).
    :param dna1: First gene list
    :param dna2: Second gene list
    :return: None
    """
    print("========splice=============")
    newGene = DNAList()
    newGene.append("P")
    newGene.append("Q")
    newGene.append("R")

    newGene1 = DNAList("A")
    newGene1.append("B")
    newGene1.append("C")
    newGene1.append("D")
    # This method only inserts after the 0th index
    # It is assumed that the other gene can't be
    # appended above the 0th index.
    print("newGene: ", newGene)
    print("newGene1: ", newGene1)
    newGene.splice(0, newGene1)
    print("newGene.splice(1, newGene1)", newGene)

    print("========splice=============")
    print()
def snip_test(dna1):
    """
    This method tests the snip method
    from class DNAList
    :param dna1: Gene list
    :return: None
    """
    print("========snip=============")
    # Instead of considering the passed argument
    # You can create new gene and test with the appropriate
    # scenario

    # snipping with i1 < i2
    print("dna1: ", dna1)
    dna1.snip(0, 2)
    print("dna1.snip(0, 2)", dna1)

    # snipping with i1 = i2/ i1 > i2/ (i1/i2) > gene size
    # raises error

    print("========snip=============")
    print()

def test_replace():
    """
    This method tests the replace method
    from class DNAList
    :param dna1: First gene list
    :param dna2: Second gene list
    :return: None
    """
    print("========replace=============")
    newGene = DNAList("X")
    newGene.append("Y")
    newGene.append("Z")
    newGene.append("A")
    newGene.append("B")

    newGene2 = DNAList("R")
    newGene2.append("S")
    newGene2.append("T")

    print("newGene: ", newGene)
    print("newGene2: ", newGene2)
    newGene.replace("XY", newGene2)
    print("newGene.replace(""XY"", newGene2): ",newGene)
    print("========replace=============")
    print()

def test_copy(dna1):
    """
    This method tests the copy method
    from class DNAList
    :param dna1: Gene list to get copy
    :return: None
    """
    print("========copy=============")
    # Getting a copy of non empty list
    print("dna1: ", dna1)
    newGene = dna1.copy()
    print("newGene: ", newGene)

    # Getting a copy of empty list
    emptyGene = DNAList()
    print("emptyGene: ", emptyGene)
    resultGene = emptyGene.copy()
    print("resultGene: ", resultGene)
    print("========copy=============")
    print()

def main():
    """
    The main method
    This method calls all the functions to be tested
    :return: None
    """
    # To test the program one can individually look into the method
    # and comment the rest out
    # This following program runs without "raiseValue Error"
    # Printing the object may be handy(print(dna1)) for testing the test cases
    # efficiently and without raised error

    # Defining the object of DNAList Class
    dna1 = DNAList("G")
    dna2 = DNAList()

    append_test(dna1, dna2)
    join_test(dna1, dna2)
    splice_test()
    snip_test(dna1)
    test_replace()
    test_copy(dna1)

if __name__ == '__main__':
    main()




