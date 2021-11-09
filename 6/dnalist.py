"""
file: dnalist.py

description: This program provides the operations of
 gene slicing, snipping and joining. A strand of DNA
 is represented as a linked list

language: python3
author: Rudram Joshi
author: Moinuddin memon

"""
# importing class double linked list from lecture code
from node import DoubleLinkedNode

class DNAList:
    __slots__ = "gene", "size"

    def __init__(self, gene=""):
        """
        Creates a new gene or optionally creates a empty gene
        :param gene: A value of gene strand
        """
        self.size = 0
        if(gene != ""):
            self.gene = DoubleLinkedNode(gene)
            self.gene.front = self.gene
            self.gene.back = self.gene
            self.size += 1
        else:
            self.gene = gene

    def dna_size(self):
        """
        This method returns the size of the dna gene node
        :return: size of gene node
        """
        return self.size == 0

    def update_size(self):
        """
        This method updates the size of gene.
        This method is called every time a size of the
        gene list is updated
        :return: None
        """
        if(self.gene.front != None):
            self.size = 1
        else:
            self.size = 0
        node = self.gene.front
        while node != self.gene:
            self.size += 1
            node = node.front

    def find(self, s):
        """
        This recursive method finds the substring s
        in the given gene list
        :param s: String to find in a gene list
        :return: Whether the string is present or not
        """
        myStrLength = len(s)
        myGene = str(self)
        myGeneLength = len(myGene)

        if(myGeneLength < myStrLength):
            return False
        if(s == myGene[:myStrLength]):
            return True
        else:
            newGene = DNAList(myGene[1:])
            return newGene.find(s)

    def append(self, item):
        """
        This method appends a new item into gene list.
        The time complexity of the function is O(1)
        :param item: Item to append in gene list
        :return: None
        """
        if(item != ""):
            if self.dna_size():
                self.gene = DoubleLinkedNode(item)
                self.gene.front = self.gene
                self.gene.back = self.gene
            else:
                newGene = DoubleLinkedNode(item, self.gene, self.gene.back)
                self.gene.back.front = newGene
                self.gene.back = newGene
            self.size += 1

    def join(self, other):
        """
        This method takes in another DNAList and adds it
        to the end of the list.
        The time complexity of the function is O(1)
        :param other: Other DNAList
        :return: None
        """
        if not (other.dna_size()):
            if self.dna_size():
                self.gene = other.gene
                self.gene.front = other.gene.front
                self.gene.back = other.gene.back

            else:
                other.gene.back.front = self.gene
                self.gene.back.front = other.gene
                self.gene.back = other.gene.back
            self.update_size()

    def splice(self, ind, other):
        """
        This method takes an integer ind as an index into dna list
        and other DNAList. It inserts the other list after the index
        ind'th character in the list.
        The time complexity of the function is O(n)
        :param ind: Index of DNAList
        :param other: Other DNAList to insert into list
        :return: None
        """
        if not (other.dna_size()):
            if self.dna_size():
                raise ValueError("The list is empty")
            else:
                if (ind < self.size):
                    if(ind == self.size-1):
                        self.join(other)
                    else:
                        counter = 0
                        node = self.gene.front
                        newGene = DNAList(self.gene)

                        while node != self.gene:
                            if(counter == ind):
                                break
                            else:
                                counter += 1
                                newGene.append(node)
                                node = node.front

                        newGene.join(other)
                        self.gene = newGene.gene
                        self.gene.front = newGene.gene.front
                        self.gene.back = newGene.gene.back
                        self.update_size()
                else:
                    raise ValueError("Ind out of bound")

    def snip(self, i1, i2):
        """
        This method removes the portion of gene as specified
        by the integers i1 and i2.
        The time complexity of the function is O(n)
        :param i1: startIndex for removing
        :param i2: endIndex for removing
        :return: None
        """
        if i1 >= i2 or i1 > self.size or i2 > self.size:
            raise ValueError("The i1 or i2 is out of bound")
        node = self.gene.front
        counter = 0
        if not (i1 == 0 and i2 == self.size):
            if(i1 != 0):
                newGene = DNAList(self.gene)
            else:
                newGene = DNAList()

            while node != self.gene:
                counter += 1
                if not(counter >= i1 and counter < i2):
                    newGene.append(node)
                node = node.front

            self.gene = newGene.gene
            self.gene.front = newGene.gene.front
            self.gene.back = newGene.gene.back
            self.update_size()
        else:
            self.gene = ""
            self.size = 0

    def replace(self, repstr, other):
        """
        This method finds a string repstr in the given list
        and replace it with the list given by other
        The time complexity of the function is O(n)
        :param repstr:
        :param other:
        :return:
        """
        if(repstr in str(self)):
            startInd = self.__str__().find(repstr)
            endInd = len(repstr) + startInd

            if(startInd == 0 and endInd == self.size):
                self.size = 0
                self.join(other)
            else:
                node = self.gene.front
                counter = 0
                if (startInd != 0):
                    newGene1 = DNAList(self.gene)
                else:
                    newGene1 = DNAList()
                if(endInd < self.size):
                    newGene2 = DNAList()

                while node != self.gene:
                    counter += 1
                    if(counter < startInd):
                        newGene1.append(node)

                    if(counter >= endInd):
                        newGene2.append(node)

                    node = node.front

                newGene1.join(other)
                if(endInd < self.size):
                    newGene1.join(newGene2)

                self.gene = newGene1.gene
                self.gene.front = newGene1.gene.front
                self.gene.back = newGene1.gene.back
                self.update_size()
        else:
            raise ValueError("repstr is not in Gene list")

    def copy(self):
        """
        This method returns a new list with the same content
        as the list given.
        The time complexity of the function is O(n)
        :return:
        """
        if(self.dna_size()):
            return ""
        returnGene = DNAList(self.gene)
        node = self.gene.front
        while node != self.gene:
            returnGene.append(node)
            node = node.front

        return returnGene

    def __str__(self):
        """
        This method return a string representation of the contents of
        the given gene list.
        The time complexity of the function is O(n)
        :return: String with contents of list altogether
        """
        if(self.dna_size()):
            return ""
        retrunString = ""
        retrunString += str(self.gene)
        node = self.gene.front
        while node != self.gene:
            retrunString += str(node)
            node = node.front
        return retrunString