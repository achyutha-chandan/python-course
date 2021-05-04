#Pizza.py
number_of_pizzas = eval(input( "how many pizzas do u want?") )
cost_per_pizza = eval(input("how much does each cost from the menu?"))
subtotal= number_of_pizzas * cost_per_pizza
tax_rate=0.08
sales_tax=subtotal * tax_rate
total = subtotal + sales_tax
print("the total cost is $" , total)
print("this includes $",subtotal,"for the pizza and")
print("$", sales_tax,"in sales tax.")
