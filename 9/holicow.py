"""
file: holicow.py

description: This program holicow Class implements the
simulation of triggering a color in
with the usage of a graphical representation of
data points.

language: python3
author: Rudram Joshi
author: Moinuddin memon
"""

from sys import argv
from sys import exit
# Uses the code provided in the lecture
# Only "getConnected" method is added in graph.py
# no more modification is done
from graph import Graph

class holicow:
    """
    A holicow object contains
    :slot graph:Graph of the area
    :slot cow:Cow in the field
    :slot paint:paint ball to color the field
    :slot result: Optimal Outcome of triggering a paint-ball
    """
    __slots__ = "graph", "cow", "paint", "result", "triggered"

    def __init__(self, fileName):
        """
        Iniatialize a graph from a filename.
        Reading and segregating input parameters
        and creating its corresponding graph
        :param fileName: Name of File
        """
        self.cow = {}
        self.paint = {}
        self.result = {}
        self.graph = Graph()
        self.triggered = {}

        try:
            with open(fileName) as f:
                for line in f:
                    if len(line) > 0:
                        temp = line.split()
                        if temp[0] == "cow":
                            coordinates = (int(temp[2]), int(temp[3]))
                            self.cow[temp[1]] = coordinates
                            self.graph.addVertex(temp[1])
                        else:
                            coordinatesRadius = (int(temp[2]), int(temp[3]), int(temp[4]))
                            self.paint[temp[1]] = coordinatesRadius
                            self.triggered[temp[1]] = 0
                            self.graph.addVertex(temp[1])
        except Exception:
            print("File not found: " + fileName)
            exit(1)
        # Calling method to create graph
        self.create_graph()

    def create_graph(self):
        """
        Creates a graph with cows and paint balls
        as vertices.
        Adds new nodes as encountered while traversing the file
        :return: None
        """
        for i, j in self.paint.items():
            for k, l in self.cow.items():
                if (self.is_connected(j[0],j[1], j[2], l[0], l[1])):
                    self.graph.addEdge(i, k)

        for i, j in self.paint.items():
            for k, l in self.paint.items():
                if (i != k):
                    if (self.is_connected(j[0], j[1], j[2], l[0], l[1])):
                        self.graph.addEdge(i, k)


    def is_connected(self, paintX, paintY, paintRadius, x, y):
        """
        Checks whether a color node is within the radius
        of the node
        :param paintX: X-coordinate of the color node
        :param paintY: Y-coordinate of the color node
        :param paintRadius: Radius of color node
        :param x: X-coordinate of position to check
        :param y: Y-coordinate of the position to check
        :return: True/False
        """
        if (x - paintX)*(x - paintX) + (y - paintY)*(y - paintY) <= paintRadius * paintRadius:
            return True
        return False
    def reset_triggered_paintball(self):
        """
        Reset triggered paint ball
        :return: None
        """
        for i in self.triggered:
            self.triggered[i] = 0

    def triggering_paintball(self):
        """
        Calls recursive function to print which nodes are triggered by the
        paint-ball. Method for Output result 2
        :return: None
        """
        myDict = {}
        for i in self.paint:
            print("Triggering", i, "paint ball...")
            self.reset_triggered_paintball()
            self.triggered[i] = 1
            self.result[i] = (self.__triggering_paintball(i, myDict))
        print()

    def __triggering_paintball(self, paintBall, dict):
        """
        Helper function for printing the triggering nodes
        :param paintBall: Paintball triggered
        :param dict: Dictionary to store result
        :return: result of paintball in Dictionary
        """
        retDict = dict.copy()

        for i in self.graph.getConnections(paintBall):
            if(i in self.cow):
                retDict.setdefault(i, set())
                retDict[i].add(paintBall)
                print("\t",i,"is painted",paintBall+"!")

            elif(i in self.paint):
                if(self.triggered[i] == 0):
                    self.triggered[i] = 1
                    print("\t", i, "paint ball is triggered by", paintBall, "paintball")
                    retDict = (self.__triggering_paintball(i, retDict)).copy()

        return retDict

    def display_field(self):
        """
        This method is called for displaying the field.
        Method for Output result 1
        :return: None
        """
        print("Field of Dreams")
        print("---------------")
        for i in self.graph:
            print(i)
        print()

    def sum_of_dict(self, myDict):
        """
        This method returns sum of values in dictionary
        :param myDict: Dictionary
        :return: Sum of values
        """
        sum = 0
        for i in myDict:
            sum = sum + myDict[i]
        return sum

    def display_optimal_result(self):
        """
        This method is called for displaying the optimal result.
        Maximum cow colored by paintball.
        Method for Output result 3
        :return: None
        """
        maxPaintBall = 0
        maxCows = 0
        numberOfCowsPainted = {key: len(value) for key, value in self.result.items()}
        maxPaintBall = max(numberOfCowsPainted, key=numberOfCowsPainted.get)

        dictOfMaxCow = max(self.result.values(), key=len)
        numberOfColors = {key: len(value) for key, value in dictOfMaxCow.items()}
        
        maxCows = self.sum_of_dict(numberOfColors)

        print("Results:")
        if(maxCows == 0):
            print("No cows were painted by any starting paint ball!")
        else:
            print("Triggering the",maxPaintBall,"paint ball is the best choice with",maxCows,"total paint on the cows:")
            for i, j in dictOfMaxCow.items():
                print("\t",i+"'s","colors:",j)
            for i in self.cow:
                if i not in dictOfMaxCow:
                    print("\t",i + "'s", "colors: {}")

    def output(self):
        """
        This method is called for testing the output parts of this program
        Calls all three output methods for testing
        :return: None
        """
        self.display_field()
        self.triggering_paintball()
        self.display_optimal_result()

def main():
    """
    The main function prompts for the file name and enters the
    main loop.
    :return: None
    """
    try:
        file = argv[1]
        obj = holicow(file)
        obj.output()
    except Exception:
        print("Usage: python3 holicow.py {filename}")
        exit(1)


if __name__ == '__main__':
    main()