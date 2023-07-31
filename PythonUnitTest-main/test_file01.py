import unittest
import file01 as file


class TestBasicCalculation(unittest.TestCase):

    def test_check_key(self):
        self.assertEqual(file.check_key(-1), False)
        self.assertEqual(file.check_key(0), True)
        self.assertEqual(file.check_key(1), True)
        self.assertEqual(file.check_key(50), True)
        self.assertEqual(file.check_key(94), True)
        self.assertEqual(file.check_key(95), False)
        self.assertEqual(file.check_key('a'), False)

    def test_check_upper_lower(self):
        self.assertEqual(file.check_upper_lower("The quick Brown Fox!"), [3, 13])
        self.assertEqual(file.check_upper_lower("Khoor#Zruog#=,"), [2, 8])
        self.assertEqual(file.check_upper_lower("012345"), [0, 0])

    def test_encrypt_decrypt_string(self):
        self.assertEqual(file.encrypt_decrypt_string("Hello World :)"), "Khoor#Zruog#=,")
        self.assertEqual(file.encrypt_decrypt_string("Khoor#Zruog#=,", 3, 2), "Hello World :)")
        self.assertEqual(file.encrypt_decrypt_string("Khoor#Zruog#=,", option=2), "Hello World :)")
        self.assertEqual(file.encrypt_decrypt_string("Hello World :)", key=100), "Invalid key!")
        self.assertEqual(file.encrypt_decrypt_string("Hello World :)", option=4), "Invalid option!")
        

    def test_count_words_in_file(self):
        self.assertEqual(file.count_words_in_file("test1.txt"), {'HELLO': 1, 'WORLD': 2, 'HOW': 1, 'ARE': 1, 'YOU': 1, 'DOING': 1, 'I': 1, 'LOVE': 1, 'THIS': 1})
        self.assertEqual(file.count_words_in_file("test2.txt"), {'TEST': 3, 'ONE': 2, 'TWO': 1, 'THREE': 1})
        self.assertEqual(file.count_words_in_file("test3.txt"), "Wrong file or file path")
    
    def test_summarise_data(self):
        self.assertEqual(file.summarise_data("traffic_data.txt", 0), [13096, 6493, 471876, 50, 9437.52])
        self.assertEqual(file.summarise_data("traffic_data.txt", 1), [11799, 5778, 421298, 50, 8425.96])
        self.assertEqual(file.summarise_data("population_10.txt", 5), [1371851, 1730, 3327840, 34, 97877.65])
        self.assertEqual(file.summarise_data("population_10.txt", 6), [1425791, 1878, 4274491, 38, 112486.61])
        self.assertRaises(FileNotFoundError, file.summarise_data, "filenotexist.txt", 0)



if __name__== "__main__":
    unittest.main()