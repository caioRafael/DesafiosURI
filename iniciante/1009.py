name = input()
salary = float(input())
vendas = float(input())

comissao = vendas*(15/100)

total = salary + comissao

print("TOTAL = R$ %.2f"%total)