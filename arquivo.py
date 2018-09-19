def soma(num1, num2):

	if this_num(num1) and this_num(num2):
	   return float(num1) + float(num2)
	else:
	   return None

def this_num(a):
	try:
	   float(a)
	   return True
	except ValueError:
	   return False

def menos(num1, num2):
	   return float(num1) - float(num2)
