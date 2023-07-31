class CeaserCipher(object):
    
    def __init__(self):
        
        self.__key = 5
    
    def useCeaserCipher(self, plaintext):
       
        cipherText = ""
        for i in plaintext:
          if i.isalpha():
            stayInAlphabet = ord(i) + self.__key 
            if stayInAlphabet > ord('z'):
              stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        return cipherText
