operators = {
	'+': (0, 'left'),
	'-': (0, 'left'),
	'*': (1, 'left'),
	'/': (1, 'left'),
	'%': (1, 'left'),
	'^': (2, 'right')
}


def tokenize(text: str) -> list:
	ret = []
	current = ''

	i = 0
	for char in text:
		if char in operators:
			if char == '-' and (i == 0 or (text[i - 1] not in operators)):
				current += char
				continue
			if len(current) > 0:
				ret.append(current)
			ret.append(char)
			current = ''
		elif char in '()':
			if len(current) > 0:
				ret.append(current)
			ret.append(char)
			current = ''
		elif char == ' ':
			if len(current) > 0:
				ret.append(current)
			current = ''
		else:
			current += char
		i += 1

	if len(current) > 0:
		ret.append(current)

	return ret

