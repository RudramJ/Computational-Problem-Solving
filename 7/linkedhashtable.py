"""
file: LinkedHashTable.py

description: This program provides the implementation of
 hash table with nodes at every index(Chained hashtable)
 This class contains various method add, remove and contains

language: python3
author: Rudram Joshi
author: Moinuddin memon

"""
# Node class for linkedhashtable
class Node:
    __slots__ = 'key', 'prevLink', 'hashLink', 'nextLink'
    def __init__(self, key, prev = None, hash = None, next = None ):
        """
        Create a new node and optionally link it to existing one
        :param key: key to be stored
        :param prev: previous Node
        :param hash: hashLink Node
        :param next: next Node
        """
        self.key = key
        self.prevLink = prev
        self.hashLink = hash
        self.nextLink = next

    def __str__(self):
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.key)

# Class LinkedHashTable
class LinkedHashTable:

    __slots__ = 'table','tableForChain','size','cap','maxload','front', 'back'

    def __init__(self, size=10, maxload=0.7):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 10)
        :param maxload: Max load factor (default 0.7)
        '''
        self.front = None
        self.back = None
        self.size = 0
        self.cap = size
        self.maxload = maxload
        self.table = list()
        self.tableForChain = list()
        for _ in range(self.cap):
            self.table.append(None)
            self.tableForChain.append(None)

    def __iter__(self):
        """
        This method is called to make the class iterable
        :return: None
        """
        node = self.front
        while (node != None):
            yield  node.key
            node = node.nextLink

    def update_table(self, sizeChange):
        """
        This method updates the table according to add and remove function
        If load factor exceeds load limit size is doubled
        If load factor drops below 1 - load limit, size is halfed
        :param sizeChange:
        :return:
        """
        listpreviousNode = []
        previousNode = self.front
        while previousNode != None:
            listpreviousNode.append(previousNode)
            previousNode = previousNode.nextLink

        self.front = None
        self.back = None
        self.size = 0
        self.cap = int(self.cap*sizeChange)

        self.table = list()
        self.tableForChain = list()
        for _ in range(self.cap):
            self.table.append(None)
            self.tableForChain.append(None)

        for i in listpreviousNode:
            self.add(i.key)

    def is_max_load(self):
        """
        This method returns whether the maximum load
        is reached or not
        :return: None
        """
        isMax = (self.size/self.cap) > self.maxload
        return isMax

    def is_min_load(self):
        """
        This method returns whether the minimum load
        is reached or not
        :return: None
        """
        isMin = (self.size/self.cap) < (1 -self.maxload)
        return isMin

    def add(self, key):
        '''
        Adds the given (value) to the map, replacing entry with same key if present.
        :param value: Value of new entry
        '''
        # load exceeds
        if (self.is_max_load()):
            self.update_table(2)

        if (key != ""):
            index = self.hash_func(key) % self.cap

            if(self.table[index] is None and self.size == 0):
                self.size += 1
                self.table[index] = Node(key)
                self.front = self.table[index]
                self.back = self.table[index]

            elif(self.table[index] is None and self.size != 0):
                self.size += 1
                self.table[index] = Node(key, self.back, None, None)
                self.back.nextLink = self.table[index]
                self.back = self.table[index]

            elif(self.table[index] is not None and self.table[index].key != key):
                self.size += 1

                node = self.table[index]
                while (node.hashLink != None):
                    node = node.hashLink

                self.back.nextLink = Node(key, self.back, None, None)
                self.back = self.back.nextLink
                node.hashLink = self.back

    def get_number_of_nodes(self, index):
        """
        Gets the numbers of nodes at given index
        of hash table
        :param index:  Index of HashTable
        :return:    None
        """
        count = 0
        node = self.table[index]
        while node != None:
            node = node.hashLink
            count += 1
        return count

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        if(key != ""):
            index = self.hash_func(key) % self.cap
            if not self.contains(key):
                return False
            else:
                front_obj = self.front
                if front_obj.key == key:
                    self.front = front_obj.nextLink
                    self.size -= 1
                    self.table[index] = front_obj.hashLink
                    return True
                back_obj = self.back
                if back_obj.key == key:
                    self.size -= 1
                    if (self.table[index].hashLink is None):
                        self.table[index] = None
                    elif(self.table[index].hashLink is not None):
                        self.back = self.back.prevLink
                        self.back.nextLink = None
                        self.back.hashLink = None


                    return True
                else:
                    node = self.table[index]
                    if self.table[index].key == key and self.get_number_of_nodes(index) == 1:
                        self.size -= 1
                        node.prevLink.nextLink = node.nextLink
                        node.nextLink.prevLink = node.prevLink
                        self.table[index] = None

                    while node.key != key:
                        node = node.hashLink
                    if node.hashLink is None:
                        if node.prevLink is not None:
                            self.size -= 1
                            node.prevLink.hashLink = None
                    else:
                        if self.table[index].key == key and self.get_number_of_nodes(index) > 1:
                            self.size -= 1
                            node.prevLink.nextLink = node.nextLink
                            node.nextLink.prevLink = node.prevLink
                            self.table[index] = node.nextLink
                        else:
                            self.size -= 1
                            node.prevLink.nextLink = node.nextLink
                            node.nextLink.prevLink = node.prevLink
                            node.prevLink.hashLink = node.nextLink

                if (self.is_min_load()):
                    self.update_table(0.5)

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        if (key != ""):
            index = self.hash_func(key) % self.cap
            if(self.table[index] != None):
                if(self.table[index].key == key):
                    return True
                else:
                    node = self.table[index]
                    while(node.hashLink != None):
                        if(node.hashLink.key == key):
                            return True
                        node = node.hashLink
        return False

    def hash_func(self, key):
        '''
        Not using Python's built in hash function here since we want to
        have repeatable testing.
        :param key: Key to store
        :return: Hash value for that key
        '''
        if(key == ""):
            raise ValueError()
        return ord(key[0]) - 97

    def print_hashtable(self):
        """
        This method prints the hashtable created
        You can also test the class by calling this method which prints the
        hashtable as defined in the writeup
        :return: None
        """
        # print("front: ", self.front, "back: ",self.back)
        for i in range(self.cap):
            if(self.table[i] != None):
                print("Table index ",i,": ", end="")
                print(str(self.table[i].key), " --> ", end="")
                node = self.table[i]

                while(node.hashLink != None):
                    print(str(node.hashLink), " --> ", end="")
                    node = node.hashLink
            else:
                print("Table index ", i, ": ", end="")
            print()
