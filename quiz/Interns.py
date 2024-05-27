# Making Quize game
Ques=int(input("enter the question number between 1 and 20: ")) 
if Ques==1:  
  print("Which one is NOT a legal variable name??")
  l1=["1. my_var", "2. myvar","3. my-var", "4. _myvar"]
  print(l1)
  choose=int(input("enter your choice: ")) 
  match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer")
    case 4:
      print(" wrong answer")
      
elif Ques == 2:
 print("Which of the following character is used to give single-line comments in Python?")
 l2 = ["1.//", "2.#", "3. !", "4./*"]
 print(l2)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("wrong answer")
    case 4:
      print(" wrong answer")

elif Ques == 3:
 print("Which of the following functions is a built-in function in python?")
 l3 = ["1. factorial()", "2.print()", "3.seed()", "4.All of the mentioned"]
 print(l3)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("wrong answer")
    case 4:
      print(" wrong answer")
elif Ques == 4:
   print("Which of the following is not a core data type in Python programming?")
   l4 = ["1. Tuples", "2.list", "3.Class", "4.dictionary"]
   print(l4)
   choose=int(input("enter your choice: ")) 
   match choose:
      case 1:
          print(" Wrong answer")
      case 2:
        print( "wrong answer")
      case 3:
        print("Right answer")
      case 4:
        print(" wrong answer")

elif Ques == 5:
 print("Which of the following method is used for length of character in  Python programming?")
 l5 = ["1. Count()", "2.append()", "3.len()", "4.leng()"]
 print(l5)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer")
    case 4:
      print(" wrong answer")


elif Ques == 6:
 print("What will be the output of the following Python code?")
 print('''x = 'abcd'
for i in x:
    print(i.upper())''')
 l6 = ["1. Abcd", "2.ABCD", "3.abcd", "4.dcba"]
 print(l6)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" wrong answer")

elif Ques == 7:
 print("whichi of the following can be used for and operation in Python?")
 l7 = ["1.&", "2.&&", "3.and", "4.All of them "]
 print(l7)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer")
    case 4:
      print(" wrong answer")

elif Ques == 8:
 print("Which of the following statements is used for list in Python?")
 l8= ["1.[]", "2.{}", "3.()", "4.All of them "]
 print(l8)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Right answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" wrong answer")

elif Ques == 9:
 print("Which of the following statements is used for tuple in Python?")
 l9= ["1.[]", "2.{}", "3.()", "4.All of them "]
 print(l9)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer") 
    case 4:
      print(" wrong answer")

elif Ques == 10:
 print(" To add a new element to a list  which Python command is used?")
 l10= ["1. list1.addEnd()", "2. list1.addLast()", "3.list1.append()", "4.list1.add()"]
 print(l10)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer") 
    case 4:
      print(" wrong answer")
elif Ques == 11:
 print(" What will be the output of the following Python program?")
 print('''i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)''')
 l11= ["1. error", "2. (0 1 2) ", "3. (0 1 2 0)", "4.none of the mentioned"]
 print(l11)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer") 
    case 4:
      print(" wrong answer")

elif Ques == 12:
 print(" What are the two main types of functions in Python?")
 l12= ["1. System function and userdefined function", "2. user function", "3.Custom function and user function", "4.Built-in function & User defined function"]
 print(l12)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Wrong answer") 
    case 4:
      print(" Right answer")

elif Ques == 13:
 print("Which of the following is Python tuple?")
 l13= ["1.[0,1,2,3]", "2.{0,1,2,3}", "3.(0,1,2,3)", "4.All of them "]
 print(l13)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Right answer")
    case 4:
      print(" wrong answer")

elif Ques == 14:
 print("Which of the following is Python list?")
 l14= ["1.[0,1,2,3]", "2.{0,1,2,3}", "3.(0,1,2,3)", "4.All of them "]
 print(l14)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Right answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" wrong answer")

elif Ques == 15:
 print("Which type of Programming does Python support?")
 l15= ["1. object-oriented programming", "2.structured programming", "3. functional programming", "4.All of them "]
 print(l15)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "wrong answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Right answer")

elif Ques == 17:
 print("Is Python case sensitive when dealing with identifiers?")
 l17= ["1. No", "2. Yes", "3. machine dependent", "4.None of them "]
 print(l17)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Wrong answer")

elif Ques == 17:
 print("Which of the following is the correct extension of the Python file?")
 l17= ["1. .python", "2. .py", "3. .pn", "4. .p "]
 print(l17)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Wrong answer")

elif Ques == 18:
 print("Is Python case sensitive when dealing with identifiers?")
 l18= ["1. No", "2. Yes", "3. machine dependent", "4.None of them "]
 print(l18)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Wrong answer")

elif Ques == 19:
 print("Is Python code compiled or interpreted?")
 l19= ["1. Python code is both compiled and interpreted", "2. Python code is neither compiled nor interpreted", 
  "3. Python code is only compiled", 
       "4. Python code is only interpreted "]
 print(l19)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Right answer")
    case 2:
      print( "Wrong answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Wrong answer")

elif Ques == 20:
 print("Which keyword is used for function in Python language?")
 l20= ["1. function", "2. def", "3. func", "4. define "]
 print(l20)
 choose=int(input("enter your choice: ")) 
 match choose:
    case 1:
        print(" Wrong answer")
    case 2:
      print( "Right answer")
    case 3:
      print("Wrong answer")
    case 4:
      print(" Wrong answer")

 
