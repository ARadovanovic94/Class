someNumber = 10

if(someNumber > 0):
    print("Over zerro")
elif(someNumber < 0):
    print("Bellow zerro")
else:
    print("zerro")
def proveriBroj(broj: int) -> str:
  if(broj > 0):
    return "Over zerro"
  elif(broj < 0):
    return "Bellow zerro"
  else:
    return "zerro"   
  
print(proveriBroj(someNumber))
