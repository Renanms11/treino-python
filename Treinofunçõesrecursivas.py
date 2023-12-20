

def fibonnaci(x, a= 0 , b = 1):
  if x > 0 :
      print(a, end=" ")
      fibonnaci(x-1,b,a+b)

fibonnaci(10)
