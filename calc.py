num1=int(input("enter your num1:"))
op=input("Enter your operator:")
num2=int(input("Enter your num 2:"))

if op=="+":
	total = num1 + num2
	print(f"{num1}+{num2} = {total}")
elif op=="-":
	print(f"{num1}-{num2} = {num1 - num2}")
elif op == "*":
	print(f"{num1}*{num2} = {num1 * num2}")
elif op == "/":
	print(f"{num1} / {num2} = {num1 / num2}")
elif op == "**":
	print(f"{num1} ** {num2} = {num1 ** num2}")
elif op == "//":
	print(f"{num1} // {num2} = {num1 // num2}")
elif op == "%":
	print(f"{num1} % {num2} = {num1 % num2}")