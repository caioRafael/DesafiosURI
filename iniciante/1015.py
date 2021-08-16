ponto1 = input().split(" ")
ponto2 = input().split(" ")

x1, y1 = ponto1
x2, y2 = ponto2

distancia = ((float(x2)-float(x1))**2 + (float(y2) - float(y1))**2)**(1/2)

print("%.4f"%distancia)