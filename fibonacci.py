nterm = int(input())
# print(val)
def fibonanci(nterm):
  try:
        if (nterm > 0):
            result = nterm + fibonanci(nterm - 1)
            print(nterm)
            print(result)
        else:
            result=0 
        return result  
  except:
      print(NameError)           
print("fibonanci")
fibonanci(nterm)