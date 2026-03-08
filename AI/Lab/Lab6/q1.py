import random
def f(x):
  return -x**2+6*x

def hillClimbing():
  x = random.randint(0, 6)
  print(f"Initial x: {x}\nInitial f(x): {f(x)}\n")
  while True:
    current=x
    neighbors=[]
    if x-1>=0:
      neighbors.append(x-1)
    if x+1<=6:
      neighbors.append(x+1)
    
    bestN = x
    bestVal = f(x)
    for n in neighbors:
      if f(n) > bestVal:
        bestVal = f(n)
        bestN = n
    if bestN == x:
      print("Reached Optimized Solution")
      break;
    
    x=bestN
    print(f"Move to x = {x}\nf(x)={f(x)}\n")

  print(f"Final Optimized x: {x}\nMax f(x): {f(x)}\n")

hillClimbing()
