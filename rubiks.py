import itertools

import numpy as np
from tqdm import tqdm

def main(rubiksSetting):

    # faceRotationList will hold the 4 setting possibilities that comes from rotating the cube 
    # by 90 degrees using the front face as the focal point
    faceRotationList = rotate_face(rubiksSetting)
    
    # cubeOrientationList will hold all 24 setting possibilities from changing the cube orientation 
    # to the 6 unique possibilities for each of the 4 face rotations
    cubeOrientationList = []
    for i in range(len(faceRotationList)):
        cubeOrientationList.extend(rotate_cube_orientation(faceRotationList[i]))
    

    # totalSettingsList will hold all 17280 setting possibilities based on the initial setting input 
    # after permuting the colors, rotating the front face, and rotating the cube
    totalSettingsList = []
    for i in range(len(cubeOrientationList)):
        totalSettingsList.extend(permute_colors(cubeOrientationList[i]))

    canonicalForm = compute_canonical_form(totalSettingsList)

    # Use the following line instead if you want to view the canonical form as a string of standardized numbers 
    # in order to ignore the inputted colors
    return "".join(str(n) for n in canonicalForm)

    # ========================================================================================================================#
    # The following blocks of code are to view the canonical form with the same set of colors 
    # as the inputted setting in different ways

    # Using a color map, recolor the standardized canonical form
    colorMap = standardize_colors(rubiksSetting)

    coloredCanonicalForm = []
    for elem in canonicalForm:
        coloredCanonicalForm.append(colorMap[elem])

    # Use the following lines if you want to view the canonical form as a string of colors
    # return ''.join(coloredCanonicalForm)

    # Use the following line instead if you want to view the canonical form as a 6x3x3 array
    # return np.array(coloredCanonicalForm).reshape(6, 3, 3)

    # ========================================================================================================================#


# Given a 1D list of a rubiks cube input, this function grabs the 6 colors and creates a map assigning the colors to numbers in alphabetical order.
# Ex. A standard rubiks cube will return a dictionary with color assignments as follows:
# {'B': 1, 'G': 2, 'O': 3, 'R': 4, 'W': 5, 'Y': 6}
# This is useful when computing a canonical form as it will standardize what colors the canonical form will have 
# regardless of the colors and inputted setting
def standardize_colors(rubiksSetting):
    colorMap = {}
    flattenedRubiksSetting = rubiksSetting.flatten()

    listOfColors = sorted(set(flattenedRubiksSetting))
    for i in range(1, 7):
        colorMap[i] = listOfColors[i - 1]
    return colorMap


# Given a 3D array representing a rubiks cube setting, this function will rotate the cube 90 degrees clockwise 3 times
# and return the  different settings that are generated per rotation
def rotate_face(rubiks_setting):
    totalRotations = [rubiks_setting]
    for i in range(3):
        newRotation = []
        for j in range(6):
            if j == 3:
                newRotation.append(np.rot90(totalRotations[i][j]))
            else:
                newRotation.append(np.rot90(totalRotations[i][j], k=3))
        totalRotations.append(newRotation)

    firstRotationPositions = [0, 5, 4, 3, 1, 2]
    totalRotations[1] = [totalRotations[1][i] for i in firstRotationPositions]

    secondRotationPositions = [0, 2, 1, 3, 5, 4]
    totalRotations[2] = [totalRotations[2][j] for j in secondRotationPositions]

    thirdRotationPositions = [0, 4, 5, 3, 2, 1]
    totalRotations[3] = [totalRotations[3][k] for k in thirdRotationPositions]

    return np.array(totalRotations)


# Given a 3D array representing a rubiks cube setting, this function will rearrange the 3D array
# such that all 6 possible orientations of looking at the rubiks cube are returned
# using the front face as the axis of rotation
def rotate_cube_orientation(rubiks_setting):
    orientationList = [rubiks_setting]

    # The following hard coded orientations maintain the setting order (front, left, right, back, top, bottom) and moves/transforms the faces accordingly

    # the original left face as the front face
    # [1, 3, 0, 2, 4, 5]
    orientationA = []
    orientationA.append(rubiks_setting[1])
    orientationA.append(rubiks_setting[3])
    orientationA.append(rubiks_setting[0])
    orientationA.append(rubiks_setting[2])
    orientationA.append(np.rot90(rubiks_setting[4]))
    orientationA.append(np.rot90(rubiks_setting[5], k=3))

    # the original right face as the front face
    # [2, 0, 3, 1, 4, 5]
    orientationB = []
    orientationB.append(rubiks_setting[2])
    orientationB.append(rubiks_setting[0])
    orientationB.append(rubiks_setting[3])
    orientationB.append(rubiks_setting[1])
    orientationB.append(np.rot90(rubiks_setting[4], k=3))
    orientationB.append(np.rot90(rubiks_setting[5]))

    # the original back face as the front face
    # [3, 2, 1, 0, 4, 5]
    orientationC = []
    orientationC.append(rubiks_setting[3])
    orientationC.append(rubiks_setting[2])
    orientationC.append(rubiks_setting[1])
    orientationC.append(rubiks_setting[0])
    orientationC.append(np.rot90(rubiks_setting[4], k=2))
    orientationC.append(np.rot90(rubiks_setting[5], k=2))

    # the original top face as the front face
    # [4, 1, 2, 5, 3, 0]
    orientationD = []
    orientationD.append(rubiks_setting[4])
    orientationD.append(np.rot90(rubiks_setting[1], k=3))
    orientationD.append(np.rot90(rubiks_setting[2]))
    orientationD.append(np.rot90(rubiks_setting[5], k=2))
    orientationD.append(np.rot90(rubiks_setting[3], k=2))
    orientationD.append(rubiks_setting[0])

    # the original bottom face as the front face
    # [5, 1, 2, 4, 0, 3]
    orientationE = []
    orientationE.append(rubiks_setting[5])
    orientationE.append(np.rot90(rubiks_setting[1]))
    orientationE.append(np.rot90(rubiks_setting[2], k=3))
    orientationE.append(np.rot90(rubiks_setting[4], k=2))
    orientationE.append(rubiks_setting[0])
    orientationE.append(np.rot90(rubiks_setting[3], k=2))

    orientationList.append(orientationA)
    orientationList.append(orientationB)
    orientationList.append(orientationC)
    orientationList.append(orientationD)
    orientationList.append(orientationE)
    return np.array(orientationList).tolist()


# Given a 3D array representing a rubiks cube setting, this function will permute the colors of the inputted setting such that all 720 rubiks cube settings from color swappings are returned
# The function returns a list of flattened arrays to make the canonical form computing easier and more efficient
def permute_colors(rubiks_setting):
    listOfPermutations = []
    colorPermutations = list(itertools.permutations([1, 2, 3, 4, 5, 6]))
    for permutation in colorPermutations:
        mapOfCubeColorToStandardizedColors = {}
        colorPermutationIndex = 0
        newCubePermutation = []
        flattened_setting_list = np.array(rubiks_setting).flatten()
        for i in range(len(flattened_setting_list)):
            if flattened_setting_list[i] not in mapOfCubeColorToStandardizedColors:
                mapOfCubeColorToStandardizedColors[
                    flattened_setting_list[i]
                ] = permutation[colorPermutationIndex]
                colorPermutationIndex += 1
            newCubePermutation.append(
                mapOfCubeColorToStandardizedColors[flattened_setting_list[i]]
            )
        listOfPermutations.append(newCubePermutation)
    return listOfPermutations


# Given a list of 3D rubiks cube setting possibilities, this function outputs a single canonical form as a 1D array by finding the "most sorted" setting
def compute_canonical_form(settingsList):
    currentColor = 1
    currentElemIndex = 0
    canonicalForm = None

    while currentElemIndex < 54:
        filteredSettingsList = []
        for i in range(len(settingsList)):
            if settingsList[i][currentElemIndex] == currentColor:
                filteredSettingsList.append(settingsList[i])

        if not filteredSettingsList:
            currentColor += 1

        elif len(filteredSettingsList) == 1:
            break

        else:
            currentColor = 1
            currentElemIndex += 1
            settingsList = filteredSettingsList
    
    canonicalForm = filteredSettingsList[0]
    return canonicalForm


# This is to run a single rubiks cube setting from the input.txt file
def format_single_input(filename):
    # This is the hardcoded positions for where each character from the parsed input list should be to form a 3D 6x3x3 array to represent the rubiks setting with the faces in the following order: front, left, right, back, top, bottom
    positionList = [
      12, 13, 14, 24, 25, 26, 36, 37, 38, 9, 10, 11, 21, 22, 23, 33, 34, 35, 15,
      16, 17, 27, 28, 29, 39, 40, 41, 18, 19, 20, 30, 31, 32, 42, 43, 44, 0, 1,
      2, 3, 4, 5, 6, 7, 8, 45, 46, 47, 48, 49, 50, 51, 52, 53
    ]
    rubiksInput = []
    with open(filename) as f:
        for i in range(9):
            line = f.readline().strip().split()
            rubiksInput.extend(line)
            if not line:
                break
    rubiksInput = [rubiksInput[i] for i in positionList]
    rubiksSetting = np.array(rubiksInput).reshape(6, 3, 3)

    return rubiksSetting


# I used the following to run multiple settings from the rubiks-example.txt file at the same time to test if the canonical settings were equal
def format_rubiks_example_file():
    positionList = [
      12, 13, 14, 24, 25, 26, 36, 37, 38, 9, 10, 11, 21, 22, 23, 33, 34, 35, 15,
      16, 17, 27, 28, 29, 39, 40, 41, 18, 19, 20, 30, 31, 32, 42, 43, 44, 0, 1,
      2, 3, 4, 5, 6, 7, 8, 45, 46, 47, 48, 49, 50, 51, 52, 53
    ]
    rubiksInputList = []
    with open("rubiks-example.txt") as f:
        for _ in range(10):
            next(f)
        for _ in range(17280):
            newSetting = []
            for _ in range(10):
                line = f.readline().strip().split()
                if line[0] == "Form":
                    continue
                newSetting.extend(line)
                if not line:
                    break
            rubiksInput = [newSetting[i] for i in positionList]
            rubiksSetting = np.array(rubiksInput).reshape(6, 3, 3)
            rubiksInputList.append(rubiksSetting)
    return rubiksInputList


if __name__ == "__main__":
    # rubiksSetting = format_single_input("input.txt")
    # print(main(rubiksSetting))

    # Uncomment the following lines to run the program on part or all of the rubiks-example file
    #
    rubiksInputList = format_rubiks_example_file()
    mySet = set()
    for i in tqdm(range(len(rubiksInputList[:10]))):
      mySet.add(main(rubiksInputList[i]))
    print(mySet)
