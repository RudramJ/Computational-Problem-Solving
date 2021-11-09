"""
CSCI-603: lab 5 homework

Main Author: Sean Strout @ RIT CS

Author: Rudram Joshi
Author: Moinuddin Memon

Implementations of in-place sorts for selectionSort.
The program of main author has been modified and used for
sorting the list of tuple in descending order
"""

def _findMaxIndex(data, mark):
    """
    A helper routine for selectionSort which finds the index
    of the largest value of last index of tuple at the mark index or greater.
    :param data: a list of data
    :param mark: an index which is in range 0..len(data)-1 inclusive
    :return: An index which is in range 0..len(data)-1 inclusive
    """

    # assume the maximum value is at initial mark position
    maxIndex = mark

    # loop over the remaining positions greater than the mark
    for mark in range(mark + 1, len(data)):
        # if a larger value is found, record its index
        # sorts based on last index of tuple
        if data[mark][-1] > data[maxIndex][-1]:
            maxIndex = mark

    return maxIndex

def selectionSort(data):
    """
    Perform an in-place selection sort of data.
    :param data: The data to be sorted (a list of tuple)
    :return: None
    """
    for mark in range(len(data) - 1):
        maxIndex = _findMaxIndex(data, mark)
        # swap the element at marker with the min index
        data[mark], data[maxIndex] = data[maxIndex], data[mark]

