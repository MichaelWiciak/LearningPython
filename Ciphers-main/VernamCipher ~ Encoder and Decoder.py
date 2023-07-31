class VernamCipher(object):
    
    def __init__(self):
        self.__key = "abcdefghijklmnbodujdjhdabcdefghijklmnbodujdjhd"
    
    def useVernamCipher(self,stringToBeEncrypted):
        text = stringToBeEncrypted
        encryptedText = ""
        pointer = 0
        for char in text:
            encryptedText += chr(ord(char) ^ ord(self.__key[pointer]))
            pointer += 1
            if pointer ==len(self.__key):
                pointer = 0
        return encryptedText
