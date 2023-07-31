import csv

class CeasarCipherDecoder(object):
    
    def __init__(self):
        self.__maxKeySize = 26


    def __getMode(self):
         while True:
             print('Do you wish to encrypt, decrypt, brute force, or analyse frequency a message?')
             mode = input().lower()
             if mode in 'encrypt e decrypt d bruteforce b frequency f'.split():
                 return mode
             else:
                 print('Enter either "encrypt" or "e" or "decrypt" or "d" or "bruteforce" or "b" or "frequency" or "f".')
        
    def __getMessage(self):
         print('To load from file, press enter.')
         print('Enter your message:')
         user = input()
         if user == "":
              file = open("output.txt", "r")
              user = file.read()
              file.close()
         return user
    
    def __getKey(self):
         key = 0
         while True:
             print('Enter the key number (1-%s)' % (self.__maxKeySize))
             key = int(input())
             if (key >= 1 and key <= self.__maxKeySize):
                 return key

    def __getTranslatedMessage(self,mode, message, key):
        if mode[0] == 'd':
            key = -key
        translated = ''
    
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key
    
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
    
                translated += chr(num)
            else:
                translated += symbol
        return translated
    
    def decode(self):
        mode = self.__getMode()
        message = self.__getMessage()
        if mode in "bruteforce b".split():
             file = open("outputByBruteForce.txt", "w")
             for key in range(1,27):
                 file.write("\n\nKey attempted \t"+str(26-key)+"\n---------\n"+self.__getTranslatedMessage(mode, message, key))
             file.close()
             print("Brute force complete. Check your file explorer.")
        elif mode in "frequency f".split():
             file = open("outputFreq.csv", "w")
             acsv = csv.writer(file)  
             alpha = {}
             for i in range(32,128):
                  alpha[chr(i)] = 0
             for letter in message:
                alpha[letter] += 1    
             for i in range(32, 128):
                  acsv.writerows(chr(i)+","+str(alpha[chr(i)]))
             file.close()
             print('CSV file created')
        else:
             key = self.__getKey()
             print('Your translated text is:')
             print(self.__getTranslatedMessage(mode, message, key))
             file = open("output.txt", "w")
             file.write(self.__getTranslatedMessage(mode, message, key))
             file.close()


    