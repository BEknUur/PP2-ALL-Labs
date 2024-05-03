import re

with open("row.txt")as f:
    soz=f.read()

#1
    text=re.findall("a.*b",soz)
    print(text)

#2
    text=re.findall("a.*bb+|abbb+",soz)
    print(text)

#3
    text=re.findall("[a-z]_+[a-z]+",soz)
    print(text)

#4 
    san= re.findall(r"[A-Z][a-z]+", soz)
print(san)

#5
sozdik=re.findall(r"a+.b",soz)
print(sozdik)
#6
variable=re.sub(r"[.,]",':',soz)
print(variable)

#7
arip=re.sub(r"_",'',soz)
print(arip) 

#8
arip1=re.findall(r"[A-Z][^A-Z]*",soz)
print(arip1)

#9
arip2=re.findall(r"[A-Z][a-z]*",soz)
print(arip2)

#10
arip3=re.sub(r"[A-Z]",'_',soz)
print(arip3)

