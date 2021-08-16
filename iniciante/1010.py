a = input().split(" ")
b = input().split(" ")

ca, na, va = a
cb, nb, vb = b

total = (int(na)*float(va))+(int(nb)*float(vb))

print("VALOR A PAGAR: R$ %.2f"%total)