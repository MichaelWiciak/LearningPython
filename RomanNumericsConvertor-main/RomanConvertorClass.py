class RomanNumeralsConvertor(object):
    
    def __init__(self):
        self.__symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        self.__value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.__roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900, 'M':1000}
    
    def intToRoman(self,num):
        
        n = num
        flagToLeave = False
        while not(flagToLeave):
            if n<=0:
                print("Number is too small")
                return None
            elif n>3999:
                print("Number is too big")
                return None
            else:
                flagToLeave = True

        answer = ""
        pointer = 0
        while pointer<len(self.__symbols):
        	while n >= self.__value[pointer]:
        		answer += self.__symbols[pointer]
        		n -= self.__value[pointer]
        	pointer += 1
        return answer
    
    def romanToInt(self,aString):

        s = str(aString)
        i = 0
        num = 0
        while i < len(s):
           if i+1<len(s) and s[i:i+2] in self.__roman:
              num+=self.__roman[s[i:i+2]]
              i+=2
           else:
              num+=self.__roman[s[i]]
              i+=1
        return num