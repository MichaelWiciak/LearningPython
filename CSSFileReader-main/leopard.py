import csv

class Leopard(object):
    
    
    def __init__(self, csvfile):
            try:
                with open(csvfile) as file:
                    reader = csv.reader(file)  # create a 'csv reader' from the file object
                    self.__header = next(reader)
                    self.__data = list(reader)
                
                
            except (FileNotFoundError, IOError):
                print("File not found so the object won't be created")
                del self
                return None
    
    
    def get_header(self):
        return self.__header
    
    def get_dimension(self):
        
        row = 0
        column = 0
        for i in self.__data:
            if row == 0:
                for j in i:
                    column +=1
            row += 1
        
        return [row,column]
    
    def count_instances(self,column_heading, value):
        value = str(value)
        betterHeader = []
        for i in self.__header:
            betterHeader.append(i.lower())
        
        indexOfcolumn_heading = betterHeader.index(column_heading.lower())
        
        counter = 0
        for row in self.__data:
            if row[indexOfcolumn_heading].lower() == value.lower():
                counter +=1
        
        return counter
    
    def total_missing(self):
        
        totalMissing = 0
        for row in self.__data:
            flag = True
            for element in row:
                if element == "NA" or element == "?" or element == "":
                    if flag:
                        totalMissing += 1
                        flag = False
        
        return totalMissing

        