
print("Welcome to secret code maker!")
print("1.Eecode a secret code")
print("2.Decode the secret code")

while True :
     Option = input(">")
     
     if Option =="2":
          print("enter your key")
          keynum = input(">")
          print("insert your text:")
          code_decode = input(">")
          lst = []
          word = code_decode
          lst.extend(word)
          print(lst)
          newString = ""
          for i in lst:
               asciiNum = ord(i)
               asciiChar = chr(asciiNum - int(keynum))
               newString += asciiChar
          print(newString)   

     elif Option == "1":
          print("enter your new key")
          keynum = input(">")
          print("insert your text:")
          code_decode = input(">")
          lst = []
          word = code_decode
          lst.extend(word)
          print(lst)
          newString = ""
          for i in lst:
               asciiNum = ord(i)
               asciiChar = chr(asciiNum + int(keynum))
               newString += asciiChar
          print(newString)     

