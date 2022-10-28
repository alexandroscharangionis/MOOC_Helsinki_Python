while True:
  editor = input("Editor: ").lower()

  if editor != "visual studio code":
    if editor  == "word" or editor == "notepad":
      print("awful")
    else:
      print("not good")
  else:
    print("an excellent choice!")
    break