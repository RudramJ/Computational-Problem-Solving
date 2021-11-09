"""
file: tests.py
description: Verify the LinkedHashTable class implementation
"""

__author__ = [ "Rudram Joshi", "Moinuddin Memon" ]

from linkedhashtable import LinkedHashTable

def print_set( a_set ):
    print("--------------------------------------------")
    print("front: ", a_set.front, "back: ", a_set.back)
    a_set.print_hashtable()
    print("in sentence form: ", end = "")
    for word in a_set: # uses the iter method
        print( word+" ", end = "" )
    print()
    print("--------------------------------------------")

def test0():
    """
    Method test 1
    :return: None
    """
    table = LinkedHashTable( 10 )
    table.add( "to" )
    table.add( "do" )
    table.add( "is" )
    table.add( "to" )
    table.add( "be" )

    print_set( table )

    print( "'to' in table?", table.contains( "to" ) )
    table.remove( "to" )
    print( "'to' in table?", table.contains( "to" ) )

    print_set( table )

def test1():
    """
    Method test 2
    Testing the different scenarios
    Default testing of contains add and remove
    :return: None
    """
    table = LinkedHashTable( 10, 0.7 )
    table.add('batman')
    table.add('has')
    table.add('lots')
    table.add('of')
    table.add('gizmos')
    table.add('on')
    table.add('his')
    table.add('belt')

    print_set( table )

    table.remove('batman')
    table.remove( "has" )
    print( "'has' in table?", table.contains( "has" ) )
    table.remove( "belt" )
    print( "'belt' in table?", table.contains( "belt" ) )

    print_set( table )

def test2():
    """
    Method test 2
    Testing different scenarios of adding
    adding null doesnot give error!
    :return: None
    """
    table1 = LinkedHashTable(5, 0.7)
    table1.add("a")
    table1.add("x")
    table1.add("r")
    table1.add("")
    table1.add("ww")
    table1.add("a")
    print_set( table1 )
    table1.remove("a")
    table1.remove("x")
    print_set( table1 )

def test3():
    """
    Method test 3
    Testing different scenarios of removing a key
    removing empty string doesnot give and error
    Also trying to check the empty string in the hashtable
    doesnot give any error!
    :return: None
    """
    table = LinkedHashTable()
    table.add("apple")
    table.add("q")
    table.add("")
    table.add("r")
    table.add("rs")
    table.add("trs")

    print_set( table )
    table.remove("q")
    table.remove("apple")
    table.remove("")
    table.remove("")
    print("'apple' in table?", table.contains("apple"))
    print("'""' in table?", table.contains(""))
    print_set( table )

if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()


