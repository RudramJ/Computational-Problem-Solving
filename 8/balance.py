"""
file: balance.py

description: This program takes the input of balance puzzle
(weight and dist) and draws outputs result of
the balance puzzle and specifies whether it is balance or not.

language: python3
author: Rudram Joshi
author: Moinuddin memon
"""
import turtle as t
# Global constants for drawing
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# This class operates the weights hanging in the beam
class Weight:

    __slots__ = 'weight', 'dist'

    def __init__(self, dist, weight):
        """
        The __init__ method of weight class initializes the attributes of weight objects
        weight and distance.
        :param dist:     distance from center
        :param weight:   weight
        :return: None
        """
        self.weight = weight
        self.dist = dist

    def get_weight(self):
        """
        This method returns the weight of this weight object.
        :return: weight
        """
        return self.weight

    def scale_to_fit(self):
        """
        Recursive method to get the left and right of weight
        :return: left and right of weight tuple
        """
        return 0, 0

    def draw(self):
        """
        This method draws the vertical line indicating weight
        :return: None
        :pre: Position of hang(facing SOUTH)
        :post: Position of hang(facing SOUTH)
        """
        t.forward(30)
        t.up()
        t.forward(15)
        t.down()
        t.write(str(self.weight), align='center', font=("Arial", 12, "normal"))
        t.up()
        t.back(15)
        t.down()
        t.back(30)

# This class operates the beam in the puzzle to draw and check for balance
class Beam:

    __slots__ = 'beamNumber', 'weight', 'left', 'right', 'dist', 'scaleFactor', 'beamList'

    def __init__(self, number ):
        """
        The __init__ method of beam initializes the attributes of beam objects.
        Like weight, left, right, list of beams etc
        :param number: beam number
        :return: None
        """
        self.beamNumber = number
        self.weight = 0
        self.left = 0
        self.right = 0
        self.dist = 0
        self.scaleFactor = 0
        self.beamList = list()

    def add_beam(self, beamObj):
        """
        This method add an object of beam to the beam of the beam
        contains the beam in its hanger
        :param beamObj: beam Object
        :return: None
        """
        self.beamList.append(beamObj)

    def scale_to_fit(self):
        """
        This method calculates the scaling to draw the puzzle.
        This method recursively calculates the scale of every bea in the list and returns
        the L and R respectively of each beam
        :return: addition of left and right of beam components
        """
        finalLeft = 0
        finalRight = 0
        largerTickPossible = 0

        for i in range(len(self.beamList) - 1):
            leftTempL, leftTempR = self.beamList[i].scale_to_fit()
            rightTempL, rightTempR = self.beamList[i+1].scale_to_fit()
            if i == 0:
                finalLeft = leftTempL
            elif i == len(self.beamList) - 2:
                finalRight = rightTempR

            totalBeamLenghth = abs(leftTempR) + 20 + abs(rightTempL)
            tempSum = (abs((-1*self.beamList[i].dist) + self.beamList[i + 1].dist))
            tickPossible = totalBeamLenghth/tempSum
            if tickPossible < largerTickPossible:
                pass
            else:
                largerTickPossible = tickPossible

        self.scaleFactor = largerTickPossible
        self.right = self.right * self.scaleFactor
        self.left = self.left * self.scaleFactor
        retrunL = (self.left + finalLeft)
        retrunR = (self.right + finalRight)
        return retrunL, retrunR

    def get_weight(self):
        """
        This method calculates the weight of the beam object.
        This method recursively calculates the weight of beam appended
        in the list.
        :return: weight
        """
        weightOfAll = 0
        sumLeft = 0
        sumRight = 0
        negativeWeight = 0

        for beams in self.beamList:
            weight = beams.get_weight()
            if weight > 0:
                weightOfAll = weightOfAll + weight
                if beams.dist > 0:
                    sumRight = sumRight + (beams.dist * weight)
                else:
                    sumLeft = sumLeft + (beams.dist * weight)
            else:
                negativeWeight = beams
        balanceIt = 0
        if negativeWeight != 0:
            balanceIt = abs((sumLeft + sumRight)/negativeWeight.dist)
            negativeWeight.weight = balanceIt

        self.weight = weightOfAll + balanceIt
        return self.weight

    def draw(self):
        """
        This method draws the beam based on the scaling factor provided. The ticks
        are calculated based on distance and scaling factor.
        On ticks the draw of weight class is called to draw the vertical line
        :return: None
        """
        t.forward(30)
        t.right(90)
        counter = 0

        while counter != len(self.beamList) and int(self.beamList[counter].dist) < 0:

            t.forward((-1*self.beamList[counter].dist)*self.scaleFactor)
            t.left(90)
            self.beamList[counter].draw()
            t.right(90)
            t.back((-1*self.beamList[counter].dist)*self.scaleFactor)
            counter = counter + 1

        t.right(180)

        while counter != len(self.beamList) and int(self.beamList[counter].dist) > 0:
            t.forward(self.beamList[counter].dist * self.scaleFactor)
            t.right(90)
            self.beamList[counter].draw()
            t.left(90)
            t.back(self.beamList[counter].dist * self.scaleFactor)
            counter = counter + 1

        t.right(90)
        t.back(30)

    def check_balanced(self):
        """
        This method is called to print whether the given puzzle is
        balanced or not.
        :return: None
        """
        right_beam = self.beamList[-1]
        left_beam = self.beamList[0]
        right_torque = right_beam.get_weight() * right_beam.dist
        left_torque = left_beam.get_weight() * left_beam.dist
        if (right_torque + left_torque) == 0:
            print('The puzzle is balanced!')
        else:
            print('The puzzle is unbalanced!')

def init():
    """
    This function sets up the turtle window for drawing.
    :return: None
    :pre: No pre conditions
    :post: Pos( 0, 75 ) Heading( South )
    """
    t.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2,
                          WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    t.up()
    t.setheading(270)
    t.title('balance')
    t.speed(0)
    t.pensize(2)
    t.back(75)

def get_root_beam(nameOfFile):
    """
    This method returns the object of beam which is the root
    (topmost) by reading the contents of input file
    :param nameOfFile: File name
    :return: root Beam object
    """
    rootBeam = None
    beamList = []
    try:
        with open(nameOfFile) as file:
            for line in file:
                inputBeamWeight = line.split()
                beamObject = Beam(inputBeamWeight[0])
                if inputBeamWeight[0] == 'B':
                    rootBeam = beamObject
                beamList.append(beamObject)

                for i in range(1, len(inputBeamWeight), 2):
                    if i == 1:
                        beamObject.left = int(inputBeamWeight[i])
                    elif i == len(inputBeamWeight) - 2:
                        beamObject.right = int(inputBeamWeight[i])
                    negativeWeight = 0
                    for j in beamList:
                        if inputBeamWeight[i + 1] == j.beamNumber:
                            j.dist = int(inputBeamWeight[i])
                            beamObject.add_beam(j)
                            negativeWeight = 1
                    if negativeWeight == 0:
                        weightObject = Weight(int(inputBeamWeight[i]), int(inputBeamWeight[i + 1]))
                        beamObject.add_beam(weightObject)
    except Exception:
        print("File read error")
        exit()
    return rootBeam

def draw_puzzle(beamRoot):
    """
    This method initializes the init method and
    calls the draw method of beam to draw the puzzle
    :param beamRoot: Object of beam
    :return: None
    """
    init()
    beamRoot.draw()
    t.mainloop()

def main():
    """
    The main method, This method initializes the parameters to
    check and draw the given balance puzzle.
    :return: None
    """
    root = get_root_beam("Input.txt")
    root.scale_to_fit()
    root.get_weight()
    root.check_balanced()
    draw_puzzle(root)

if __name__ == '__main__':
    main()