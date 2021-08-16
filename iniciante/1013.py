valores = input().split(" ")

a, b, c = valores

maior1 = (int(a)+int(b)+abs(int(a)-int(b)))/2
maior2 = (int(c)+maior1+abs(int(c)-maior1))/2
m = int(maior2)

print(m,"eh o maior")