"""
file: lasers.py

description: This program gives the highest sum of
 numbers possible of a three way laser placed in
 the given grid.

language: python3
author: Rudram Joshi
author: Moinuddin memon

"""
# importing sort function from lecture code
import rit_sort as sort
# My directions constant
DIRECTIONS = ['facing east', 'facing west', 'facing north', 'facing south', 'facing all']

def get_file_content(fileContent):
    """
    This method reads the contents of the file.
    And returns the corresponing Lists of the input
    grid
    :param fileContent: FileToRead
    :return:            dataGrid
    """
    dataList = []
    for i in fileContent:
        dataList.append(i.split(" "))

    returnData = []
    for i in dataList:
        x = []
        for j in i:
            j = int(j)
            x.append(int(j))
        returnData.append((x))
    return returnData

def get_east_sum(columnIndex, rowIndex, data):
    """
    This method calculates the sum of laser
    facing in the east direction
    :param columnIndex: Column Index of grid
    :param rowIndex:    Row Index of grid
    :param data:        grid
    :return:            sum while facing east
    """
    returnSum = data[columnIndex][rowIndex+1]
    returnSum += data[columnIndex-1][rowIndex]
    returnSum += data[columnIndex+1][rowIndex]
    return returnSum

def get_west_sum(columnIndex, rowIndex, data):
    """
    This method calculates the sum of laser
    facing in the west direction
    :param columnIndex: Column Index of grid
    :param rowIndex:    Row Index of grid
    :param data:        grid
    :return:            sum while facing west
    """
    returnSum = data[columnIndex][rowIndex-1]
    returnSum += data[columnIndex-1][rowIndex]
    returnSum += data[columnIndex+1][rowIndex]
    return returnSum

def get_north_sum(columnIndex, rowIndex, data):
    """
    This method calculates the sum of laser
    facing in the north direction
    :param columnIndex: Column Index of grid
    :param rowIndex:    Row Index of grid
    :param data:        grid
    :return:            sum while facing north
    """
    returnSum = data[columnIndex][rowIndex-1]
    returnSum += data[columnIndex][rowIndex+1]
    returnSum += data[columnIndex-1][rowIndex]
    return returnSum

def get_south_sum(columnIndex, rowIndex, data):
    """
    This method calculates the sum of laser
    facing in the south direction
    :param columnIndex: Column Index of grid
    :param rowIndex:    Row Index of grid
    :param data:        grid
    :return:            sum while facing south
    """
    returnSum = data[columnIndex][rowIndex - 1]
    returnSum += data[columnIndex][rowIndex + 1]
    returnSum += data[columnIndex+1][rowIndex]
    return returnSum

def get_all_sum(columnIndex, rowIndex, data):
    """
    This method calculates the sum of laser
    facing in the all directions.
    And returns the maximum sum.
    :param columnIndex: Column Index of grid
    :param rowIndex:    Row Index of grid
    :param data:        grid
    :return:            max sum and direction
    """
    tempList = []
    eastData = (columnIndex, rowIndex, DIRECTIONS[0], get_east_sum(columnIndex, rowIndex, data))
    tempList.append(eastData)
    westData = (columnIndex, rowIndex, DIRECTIONS[1], get_west_sum(columnIndex, rowIndex, data))
    tempList.append(westData)
    northData = (columnIndex, rowIndex, DIRECTIONS[2], get_north_sum(columnIndex, rowIndex, data))
    tempList.append(northData)
    southData = (columnIndex, rowIndex, DIRECTIONS[3], get_south_sum(columnIndex, rowIndex, data))
    tempList.append(southData)
    # sort in descending order
    sort.selectionSort(tempList)
    # return the parameters of max sum
    return tempList[0][2], tempList[0][3]

def sort_data(dataToSort, numberOfLasers):
    """
    This method calls the selection sort function
    to sort the data and slices the data after
    sorting based on number of lasers asked
    :param dataToSort:  List of Laser Placement
    :param numberOfLasers:  Number of Laser to Place
    :return:    Sorted List based on number of laser
    """
    sort.selectionSort(dataToSort)
    return dataToSort[:numberOfLasers]

def get_lasers(myInput):
    """
    This method calculates all the lasers
    possible and returns the list of lasers
    with maximum sum possible and its direction
    :param myInput:  input grid
    :return:         List of lasers
            (coordinates, directions and sum)
    """
    myListOfLaser = []
    for i in range(len(myInput)):
        for j in range(len(myInput[i])):

            if i != 0 and i != len(myInput)-1:
                # All directions possible
                if j != 0 and j != len(myInput[i])-1:
                    myDir, mySum = get_all_sum(i, j, myInput)
                    temp = (i, j, myDir, mySum)
                    myListOfLaser.append(temp)
                # Only East direction possible
                elif j == 0:
                    temp = (i, j, DIRECTIONS[0], get_east_sum(i, j, myInput))
                    myListOfLaser.append(temp)
                # Only West direction possible
                elif j == len(myInput[i])-1:
                    temp = (i, j, DIRECTIONS[1], get_west_sum(i, j, myInput))
                    myListOfLaser.append(temp)
            elif i == 0:
                # Only South direction possible
                if j != 0 and j != len(myInput[i])-1:
                    temp = (i, j, DIRECTIONS[3], get_south_sum(i, j, myInput))
                    myListOfLaser.append(temp)
            elif i == len(myInput)-1:
                # Only North direction possible
                if j != 0 and j != len(myInput[i])-1:
                    temp = (i, j, DIRECTIONS[2], get_north_sum(i, j, myInput))
                    myListOfLaser.append(temp)
    return myListOfLaser

def main():
    """
    Ths main method prompt for reading input file
    and number of lasers possible and gets the result
    And also prints the data.
    :return:    None
    """
    myFileName = input("Enter the file name: ")
    try:
        with open(myFileName) as f:
            myFile = f.read().splitlines()
            myGrid = get_file_content(myFile)
    except FileNotFoundError:
        print("Enter valid file name")
        exit()

    myLasers = get_lasers(myGrid)

    howManyLasers = input("Enter number of lasers: ")

    while (not (int(howManyLasers) >=0 and int(howManyLasers) <= len(myLasers))):
        howManyLasers = input("lasers >= 0 and lasers <= "+str(len(myLasers))+" : ")

    dataToPrint = sort_data(myLasers, int(howManyLasers))
    for i in range(len(dataToPrint)):
        row = dataToPrint[i][0]
        column = dataToPrint[i][1]
        direction = dataToPrint[i][2]
        print("(",column,",",row,")", str(direction))

if __name__ == '__main__':
    main()