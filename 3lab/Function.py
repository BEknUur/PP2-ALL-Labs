# TASK1

'''
def myfunc(x):
    print(x*28.3495231)

mass=int(input())
myfunc(mass)
'''


'''
#task2
def temperature(x):
    c = (5/9) * (x - 32)
    print(c)

fahrenheit = float(input())
temperature(fahrenheit)
'''
#task3
'''
def solve(numheads,numlegs):
   rabbit=(numlegs-(2*numheads))/2
   chicken=numheads-rabbit
   print(rabbit,chicken)

a=int(input())
b=int(input())
solve(a,b)
'''



#task4
'''
numbers=list(map(int,input().split()))

def filter_prime(numbers):
        list=numbers
        prime_num=[]
        s=0
        for i in list:
            if i<=3 and i!=0:
                prime_num.append(i)
            for j in range(2,i):
                if i<=3 and i==0:
                    break
                elif i%j!=0:
                    s+=1

            if (s==(i-2) and s>2):
                 prime_num.append(i)
                 s=0
            s=0  
        print(prime_num)
filter_prime(numbers)

'''
#5 
'''
words = list(map(str, input().split()))

def reversed_word(word):
    w = word
    wordss = []
    for i in range(len(w) - 1, -1, -1):
        wordss.append(w[i])
    
    for i in wordss:
        print(i,end=" ")

reversed_word(words)
print(" ")

'''

#6
def reversed_word(word):
    w = word
    wordss = []
    for i in range(len(w) - 1, -1, -1):
        wordss.append(w[i])
    
    for i in wordss:
        print(i,end=" ")

reversed_word(words)
print(" ")


#7
def has_33(nums):
    numbers=nums
    bol=False
    for i in range(len(numbers)-1):
        if numbers[i]==numbers[i+1]:
            bol=True
    if bol==True:
        print("True")
    else:
        print("False")

has_33([1,2,3])



#8
def spy_game(nums):
    numbers=nums
    bol=0
    bool1=False
    for i in numbers:
        if i==0:
            bol +=1
        if (bol>=2 and i==7):
            bool1=True
            break
    if bool1==False:
        print("False")
    else:
        print("True")    
    
spy_game([1,2,3,4,0,0,0,4,3,5,3])


#9
def area_circle(radius):
    print(3.14*(radius)**2)

area_circle(4)


#10
def unique(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)




#11
array=list(map(str,input().split()))

def palindrome(list):
    array=list
    wordss = []
    reversed0=[]
    for i in array:
        reversed0.append(i[::-1])
    for i in reversed0:
        for j in array:
            if(i==j):
                print(i,end=" ")
    print("")
palindrome(array)



#12
his=map(int,input().split())
def histogram(lis):
    list=lis
    for i in list:
        print("*"*i)
    
histogram(his)


#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name=str(input())
    secret_number = random.randint(1, 20)
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    attempts = 0

    while True:
        # input
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_the_number()


    






