import tokenizer
import re

ops = tokenizer.operators


def conv_to_rpn(text: str) -> list:
	tokens = tokenizer.tokenize(text)
	queue = []
	stack = []

	for token in tokens:
		if re.search(r'^-?\d*\.\d+$', token):
			queue.append(float(token))
		elif re.search(r'^-?\d+$', token):
			queue.append(int(token))
		elif token in ops:
			if len(stack) > 0:
				while (len(stack) > 0 and not stack[0] == '(') and (
					(ops[token][1] == 'left' and ops[token][0] <= ops[stack[0]][0]) or
					(ops[token][1] == 'right' and ops[token][0] < ops[stack[0]][0])):
					queue.append(stack.pop(0))
			stack.insert(0, token)
		elif token == '(':
			stack.insert(0, token)
		elif token == ')':
			while len(stack) > 0 and not stack[0] == '(':
				queue.append(stack.pop(0))
			stack.pop(0)
		else:
			print(f'Syntax error: {token}')
			queue.append(0)

	while len(stack) > 0:
		queue.append(stack.pop(0))

	return queue


def evaluate_rpn(rpn: list):
	stack = []
	vars = {}
	for token in rpn:
		if type(token) == int or type(token) == float:
			stack.insert(0, token)
		elif token in ops:
			try:
				if token == '+':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a + b)
				elif token == '-':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a - b)
				elif token == '*':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a * b)
				elif token == '/':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a / b)
				elif token == '%':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a % b)
				elif token == '^':
					b = stack.pop(0)
					a = stack.pop(0)
					stack.insert(0, a**b)
			except IndexError:
				print(f'Syntax error {token}')
		else:
			print(f'Syntax error: {token}')
			stack.insert(0, 0)

	if len(stack) > 0:
		return stack.pop(0)
	else:
		return 0


while True:
	print(evaluate_rpn(conv_to_rpn(input('> '))))

