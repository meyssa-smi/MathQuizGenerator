import math
import random



def ascii_name_plaque(name):
    ''' (str)->None
    Draws/Prints name plaque'''
    print()
    print(5*"*"+len(name)*"*"+5*"*")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print("*  "+2*"_"+name+2*"_"+"  *")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print(5*"*"+len(name)*"*"+5*"*")
    print()

def primary_school_quiz(flag, n):
    '''(int, int) -> int
    Preconditions: flag is 0 or 1, n is positive
    Returns the number of correct answers out of n questions
    about subtraction is flag is 0 or exponentiation if flag is 1
    '''
    correct = 0
    for i in range(n):
        a = random.randint(1,9)
        b = random.randint(1,9)
        print(f"Question {i+1}:")
        if flag == 0:
                expected = a-b
                received = int(input(f"What is the result of {a}-{b}? "))
        elif flag==1:
                expected = a**b
                received = int(input(f"What is the result of {a}^{b}? "))
        if expected == received:
                correct = correct+1
    return correct

def high_school_eqsolver(a,b,c):
     ''' (number, number, number)->None
         Prints nicely the roots of ax^2+bx+c=0 equation given coefficients a, b and c
     '''
     if a==0:
          if b!=0 :#linear equation
               print ("The linear equation", str(b)+"\u00B7"+"x + "+str(c)+" = 0")
               root=-c/b
               print ("has the following root/solution:", root)
          else:
               print ("The quadratic equation", str(b)+"\u00B7"+"x + "+str(c)+" = 0")
               if c==0:
                    print("is satisfied for all numbers x")
               else:
                    print("is satisfied for no number x")
     else: # a non-zero
          discriminant=b**2-4*a*c
          if discriminant>0: # the equation is quadratic and has 2 real roots
               print ("The quadratic equation", str(a)+"\u00B7"+"x^2 + "+str(b)+"\u00B7"+"x + "+str(c)+" = 0")
               print ("has the following real roots: ")
               print ((-b+math.sqrt(discriminant))/(2*a), " and", (-b-math.sqrt(discriminant))/(2*a))
          elif discriminant==0: # the equation is quadratic and has 1 real root
               print ("The quadratic equation", str(a)+"\u00B7"+"x^2 + "+str(b)+"\u00B7"+"x + "+str(c)+" = 0")
               print ("has only one solution, a real root: ")
               print(-b/(2*a))
          else:# the equation is quadratic and has 2 complex roots
               print ("The quadratic equation", str(a)+"\u00B7"+"x^2 + "+str(b)+"\u00B7"+"x + "+str(c)+" = 0")
               print ("has the following two complex roots: ")
               print (-b/(2*a), "+ i", math.sqrt(abs(discriminant))/(2*a),  "\n and")
               print (-b/(2*a), "- i", math.sqrt(abs(discriminant))/(2*a) )

               # alternatively this uses python's built in complex numbers:
               #
               #print(complex(b/(2*a), math.sqrt(abs(discriminant))/(2*a)), "\n and")
               #print(complex(b/(2*a), -math.sqrt(abs(discriminant))/(2*a)))




# main
ascii_name_plaque("Welcome to my math quiz-generator / equation-solver")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
     ascii_name_plaque(name+", welcome to my quiz-generator for primary school students.")
     flag = int(input(name+ " what would you like to practice? Enter \n0 for subtraction \n1 for exponentiation\n"))
     n = int(input("How many practice questions would you like to do? "))
     if n<0:
          print("A negative number of questions? Hmm. "+name+" you must be too tired. Take a rest.")
     elif n==0:
          print("Zero questions. OK.")
     else:
          print(f"{name}, here is your {n} questions:")
          correct = primary_school_quiz(flag, n)
          grade = round(100*correct/n, 10)
          if grade >= 90:
               print("Congratulations "+name+"! You'll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
          elif grade >= 70:
               print("You did well "+name+", but I know you can do better.")
          else:
               print("I think you need some more practice "+name+".")

elif status=='2':
     ascii_name_plaque("quadratic equation, a\u00B7"+"x^2 + b"+"\u00B7"+"x + c= 0, solver for "+name)
     
     flag=True
     while flag:
             question=input(name+", would you like a quadratic equation solved? ")

             # your code to handle varous form of "yes" goes here
             question=(question.strip()).lower()

             if question!="yes":
                     flag=False
             else:
                     print("Good choice!")
                     # your code goes here (i.e ask for coefficients a,b and c and call quadratic_eq
                     a1=float(input("Enter a number the coefficient a: "))
                     b1=float(input("Enter a number the coefficient b: "))
                     c1=float(input("Enter a number the coefficient c: "))
                     # make a function call and pass it the three coefficients the user entered
                     high_school_eqsolver(a1,b1,c1)
else:
     print(name+" you are not a target audience for this software.")

print("Good bye "+name+"!")
