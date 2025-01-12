import loginsystem
print(loginsystem.user)
if (loginsystem.login()):    
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  satu=int(input("masuqqan angqa: "))
  print(satu * 1000)
  x = thisdict.keys()
  print(x)
else:
  exit