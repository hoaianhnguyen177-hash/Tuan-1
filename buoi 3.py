#bai 1
n = int(input())

for i in range(n):
    print("*" * n)

#bai 2
n = int(input())

for i in range(1, n + 1):
    print("*" * i)

#bai 3
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - 1) + "*" * i)


#bai 4
n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")


#bai 5 
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - 1) + "*" * (2 * i - 1))


#bai 6
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - 1) + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        print(" " * (n - 1) + "*" + " " * (2 * i - 3) + "*")


#bai 7
n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#bai 11
n = int(input())

for i in range(1, n + 1):
    print(i, end=" ")


#bai 12
n = int(input())

tong = 0

for i in range(1, n + 1):
    tong += i

print(tong)

#bai 13
n = int(input())

tong = 0

for i in range(2, n + 1, 2):
    tong += i

print(tong)

#bai 14
n = int(input())

dem = 0

while n > 0:
    dem += 1
    n //= 10

print(dem)

#bai 15
n = int(input())

tong = 0

while n > 0:
    tong += n % 10
    n //= 10

print(tong)

#bai 16
n = int(input())

dao = 0

while n > 0:
    dao = dao * 10 + n % 10
    n //= 10

print(dao)

#bai 17
n = int(input())

tam = n
dao = 0

while tam > 0:
    dao = dao * 10 + tam % 10
    tam //= 10

if dao == n:
    print("YES")
else:
    print("NO")

#bai 21
    s = input()

print(len(s))

#bai 22
s = input()

dem = 0

for c in s:
    if c != " ":
        dem += 1

print(dem)


#bai 23

s = input().lower()

nguyen_am = 0
phu_am = 0

for c in s:
    if c.isalpha():
        if c in "aeiou":
            nguyen_am += 1
        else:
            phu_am += 1

print("Nguyen am:", nguyen_am)
print("Phu am:", phu_am)

#bai 24
s = input()
k = input()

dem = 0

for c in s:
    if c == k:
        dem += 1

print(dem)

#bai 25
s = input()

print(s[::-1])


#bai 26
s = input()

if s == s[::-1]:
    print("YES")
else:
    print("NO")

#bai 27    
s = input()

tu = s.split()

print(len(tu))

