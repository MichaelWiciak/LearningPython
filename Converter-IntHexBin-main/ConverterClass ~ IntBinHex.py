class Converter(object):
    
    def __init__(self):
        
        pass
    
    def intToBin(self,num):
        print("Enter positive integer")
        n = num
        bits = ""
        while (n > 0):
        	b = n % 2
        	n = n // 2
        	bits = str(b) + bits 
    
        print(str(num)+" in binary is: "+bits)
        return bits

    def binToInt(self,num):
        binary = str(num)
        rt = 0
        for i in range(len(binary)-1,-1,-1):
            rt += eval(binary[i])*(2 ** (len(binary)-i-1))
    	
        print(str(num)+" in base 10 is: "+str(rt))
        return rt

    def intToHex(self,num):
        print(str(num)+" in hex is: "+hex(num)[2:])
        return hex(num)
        
    def hexToInt(self,num):
        print(str(num)+" in hex is: "+str(int(num)))
        return int(num)
    
