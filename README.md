# RubiksCubeCanonicalForm

There are 17280 possible ways that a Rubik's cube can be rotated and have it's colors permuted. 
This repository uses a brute force method to compute the canonical form of a Rubik's cube.
Any of the 17280 possibilities used as an input will result in the same canonical form.

## Program Instructions

### Requirements 
Make sure you have python3 installed. If not please visit, https://www.python.org/downloads/.

Install numpy using `pip3 install numpy` on your command line.

Install tqdm using `pip3 install tqdm` on your command line. This isn't strictly necessary and lines using this can be commented out but it does help with the output formatting when running the program on multiple settings at once.


### How to run the program

Clone this repository to your local computer.

Navigate to the parent directory `/RubiksCubeCanonicalForm`

To run the program with the provided input.txt file, run `python3 rubiks.py`

To run the program with the the provided rubiks-example.txt file, uncomment lines 325-329. In line 327, change the list splice to however many of the settings you want to run, it is defaulted to 10. Then run `python3 rubiks.py`

To run the tests, run `python3 -m unittest`

## High Level Solution:
- Parse the inputted setting into a 3D 6x3x3 array where each 3x3 array is a face and the order of the faces is as follows: front, left, right, back, top, bottom
- Compute all 17280 orientations and color permutations of the given setting.
  - 4 ways to rotate a single face 90 degrees
  - 6 ways we can reorient the cube to look at a different face
  - 720 ways that 6 colors can be permuted (6! = 720
  - 4 * 6 * 720 = 17280
- Standardize the colors into numbers (1-6) to eliminate discrepancies in inputted colors.
- Filter down the list of settings by finding the "most sorted" setting. A rough sketch of the algorithm is provided at the bottom of the README.
- Return a string of 54 numbers to represent the canonical form.



## Extra Notes
Data Structure for holding a Rubik’s Cube Setting:
3D Array with dimensions as follows: 6x3x3
- 3x3 array to hold the colors for each of the 6 faces
- The order of the faces in the array is: front, left, right, back, top, bottom
Easy to switch between 3D and 1D using numpy whenever convenient for development purposes

What the canonical key should look like:
A string of numbers with length 54 holding the flattened 3D array that was determined to be the canonical form. 
Rather than storing the array itself, storing the string will make it easy to look it up in a generic database or dictionary. 
In my code, I provided ways to show the canonical form as a 54 length string of numbers to ignore custom coloring, a 3D 6x3x3 array with colors, and string with length 54 of the colors originally used in the inputted setting.


A rough sketch of the “most sorted” algorithm is as follows:
With a list of 6 color possibilities [c1, c2, c3, c4, c5, c6]
Filter down this list of 17280 possibilities by finding the “most sorted” list
  * Filter down the possibilities to all lists that start with c1. If the filtered list is not empty, iterate to the next element of the possibilities and check for all possibilities with the next element being c1. Continue till you reach an empty filtered list.
  * When you reach an empty filtered list, back up to the previous iteration where the list isn’t empty and iterate to the next color (c2) and check for the next element being c2
        * If this filtered list is not empty, iterate to the next element of the lists and reset the color back to c1. Repeat again starting with step 1
        * If this filtered list is empty, repeat step 2 with the next color
    * When the filtered list has only 1 list in it, you have solved for the canonical form
