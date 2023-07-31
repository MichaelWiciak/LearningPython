def main():
    
    taxIncome = input()
    incomeCalculated = 0
    
    
    try:
        taxIncome = float(taxIncome)
    except ValueError:
        print("Invalid amount!")
        return None
        
    if taxIncome == 0:
        incomeCalculated = 12500.00
        print(incomeCalculated)
        return None
    
    if 50000 > (taxIncome/0.2)+12500:
        incomeCalculated = (taxIncome/0.2)+12500
        print(round(incomeCalculated))
        return None
    else:
        incomeCalculated = 12500 +(50000-12500)
        if 99999 > (taxIncome-7500)/0.4:
            incomeCalculated +=  (taxIncome-7500)/0.4
            print(round(incomeCalculated))
            return None
        else:
            incomeCalculated += 99999
            
            incomeCalculated += (taxIncome-7500-39999.6)/0.45
            print(round(incomeCalculated))
            return None

