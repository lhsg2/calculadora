def som (x,y):
  return x + y

def sub (x,y):
  return x - y

def mult (x,y):
  return x * y

def div (x,y):
  return x / y

print("selecine uma operação")
print("1. Adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")

op = input("degite uma opção (1,2,3,4):")
if op in('1','2','3','4'):
  n1 = float(input("degite um numero:"))
  n2 = float(input("degite outro nuemro:"))
  if op == '1':
    print(f"{n1}+{n2} = {som(n1,n2)}")
     
  if op == '2':
    print(f"{n1}-{n2} = {sub(n1,n2)}")

  if op == '3':
    print(f"{n1}*{n2} = {mult(n1,n2)}")

  if op == '4':
    if n2 !=0:
      print(f"{n1}/{n2} = {div(n1,n2):f.2}")
    else:
      print("erro:não é possivel dividir um numero por zero")
else:
  print("escolha invalida.Por favor, escolha 1,2,3 ou 4")
  
  