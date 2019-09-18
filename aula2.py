idade =  int(input("Digite sua idade:"))

if idade >= 21 and idade <65:
    print("Idade aceita")
    salario = float(input("digite seu salário:"))
    emprestimo = float(input("Digite o valor do empréstimo:"))
else:
    print("Idade não compativel")
if emprestimo<=salario*10:
    print ("Emprestimo Aprovado")
else:
    print("Emprestimo Negado")




    