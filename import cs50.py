try:
	from cs50 import get_string
except Exception:
	def get_string(prompt):
		return input(prompt)

name = get_string("What is your name? ")
print("Hello, " + name)