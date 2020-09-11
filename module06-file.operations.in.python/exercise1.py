with open("accounts.txt", mode="wt") as accounts:
    accounts.write("Iban,Full name,Salary\n")  # header
    accounts.write("tr1,jack bauer,100000\n")
    accounts.write("tr2,kate austen,200000\n")
    accounts.write("tr3,jin kwon,300000\n")
    accounts.write("tr4,sun kwon,400000")
