class PangramChecker(object):
    
    def __init__(self):
        
        pass
    
    def checkIfPangram(self,pangramContender):

        target = []
        for i in range(97,97+26):
            target.append(chr(i))
        print("\n> '"+pangramContender+"'")
        test = pangramContender # defensive copy
        test = test.replace(" ","") # remove spaces
        test = test.replace(".","") # remove full stops, etc
        for i in test:
            if i in target:
                target.remove(i)
        if target == []:
            print("'"+pangramContender+"'"+" is a Pangram.")
            return True
        else:
            print("'"+pangramContender+"'"+" is not Pangram.")
            print("A few letters left over...",end="")
            print("\t"+"".join(target))
            return False
    