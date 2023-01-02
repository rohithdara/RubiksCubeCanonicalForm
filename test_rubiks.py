import unittest

from rubiks import (format_single_input, main, permute_colors,
                    rotate_cube_orientation, rotate_face)


class TestRubiks(unittest.TestCase):

    def test_face_rotations(self):
        rubiksSetting = format_single_input("input.txt")
        initialOutput = rotate_face(rubiksSetting)

        for each in initialOutput:
            faceRotations = rotate_face(each)
            for rotation in faceRotations:
                self.assertTrue(rotation in initialOutput)
    
    def test_face_rotations_output_length(self):
        rubiksSetting = format_single_input("input.txt")
        self.assertEquals(4, len(rotate_face(rubiksSetting)))
    
    def test_rotate_cube_orientations(self):
        rubiksSetting = format_single_input("input.txt")
        faceRotations = rotate_face(rubiksSetting)
        
        initialOutput = []
        for rotation in faceRotations:
            initialOutput.extend(rotate_cube_orientation(rotation))
            
        for each in initialOutput:
            cubeOrientations = rotate_cube_orientation(each)
            for orientation in cubeOrientations:
                self.assertTrue(orientation in initialOutput)
        
        self.assertEquals(24, len(initialOutput))
    
    def test_rotate_cube_orientations_output_length(self):
        rubiksSetting = format_single_input("input.txt")
        self.assertEquals(6, len(rotate_cube_orientation(rubiksSetting)))

    
    def test_permute_colors_output_length(self):
        rubiksSetting = format_single_input("input.txt")
        self.assertEquals(720, len(permute_colors(rubiksSetting)))
        
    def test_solved_cube(self):
        rubiksSetting = format_single_input("solved_cube.txt")
        self.assertEquals(main(rubiksSetting), "111111111222222222333333333444444444555555555666666666")
            
        

if __name__ == '__main__':
    unittest.main()