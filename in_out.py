def outer_function(x):
	def inner_function():
		nonlocal x
		x *= 2
		print(x)
	return inner_function

inn = outer_function(5)
inn()
inn()
inn()