#Bai 1
n = int(input())
for i in range (1, 11):
    print(n, "x", i, "=", n * i)


#Bai 2

import random

so = random.randint(1, 50)

while True:
    doan = int(input())

if so == doan:
    print("Doan dung")
    break

elif doan < so:
    print("Lon hon")
else:
    print("Nho hon")


#Bai 3

n = int(input*())

tong = 0

for i in range(1, n +1):
    if i % 10 == 0:
        continue
    tong += i 

print(tong)

#Bai 4

kwh = float(input())

if kwh < 0:
    print("Khong hop le")
elif kwh <= 50:
    tien = kwh * 1678
elif kwh <= 100:
    tien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
else:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536

if kwh >= 0:
    print("Tong tien dien:", format,(tien, ", 0f"), "VND")


#Bai 5
a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai mot tam giac")
elif a == b == c:
    print("Tam giac deu")
elif a == b or a == c or b == c:
    print("Tam giac deu")
elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("Tam giac vuong")
else:
    print("Tam giac thuong") 


#Bai 6
km = float(input())

if km <= 0:
    print("So km phai lon hon 0")
elif km <= 1:
    tien = 15000
elif km <= 30:
    tien = 15000 + (km - 1) * 12000
else:
    tien = 15000 + 29 * 12000 + (km - 30) * 10000
if km > 100:
    tien *= 0.9
if km > 0:
    print("Cuoc taxi:" format(tien, ",.0f"), "VND") 
    
                       


    
