#1
#Create a generator that generates the squares of numbers up to some number N.

def square(n):
    for i in range(1,n+1):
        yield i**2

sandar=square(int(input()))
for san in sandar:
    print(san,end=" ")



#2
#rite a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(0,n+1):
        if(i%2==0):
            yield i
san=int(input())
beknur=even_numbers(san)
for i in beknur:
    print(i,end='')
    if i!=san and i+2<=san:
        print()


#3
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n
def oilan(n):
    for i in range(0,n+1):
        if(i%3==0 and i%4==0):
            yield i

result=oilan(int(input()))
for i in result:
    print(i,end=" ")
    print()

#4
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squaress(a,b):
    for i in range(a,b+1):
        yield i**2

chislo=squaress(int(input()),int(input()))
for i in chislo:
    print(i,end=" ")

 #5
#Implement a generator that returns all numbers from (n) down to 0.   
    def retrn(n):
        while(n>=0):
            yield n
            n-=1

san=retrn(int(input()))
for i in san:
    print(i,end=" ")





        