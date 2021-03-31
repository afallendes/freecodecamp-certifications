import re


def arithmetic_arranger(problems: list, show_result: bool = False):
	""" Returns a graphical representation of simple arithmetics operations.
		Only valid operations are sum and subtraction.
	"""

	# Check number of problems. Max limit is 5.
	if len(problems) > 5:
		return "Error: Too many problems."

	pattern = r"^(\S+) ([\+\-\*\/]) (\S+)$"

	line1, line2, line3 = [ [] for _ in range(3) ]

	if show_result:
		line4 = []

	space_between_problems = 4 * " "

	for problem in problems:
		m = re.match(pattern, problem)

		# Check if there is no regex match
		if not m:
			return "Error: Syntax error."

		n1, operator, n2 = m.groups()

		# Check if operator is invalid
		if operator in ("*", "/"):
			return "Error: Operator must be '+' or '-'."

		# Check if input values are not numbers
		if not n1.isdigit() or not n2.isdigit():
			return "Error: Numbers must only contain digits."

		# Check if input values are longer than 4
		if len(n1) > 4 or len(n2) > 4:
			return "Error: Numbers cannot be more than four digits."
		
		# Calculate max number of chars based on longest input value
		max_chars = max([len(n1), len(n2)])

		# Create a line using rjust to fill with whitespace to the right
		line1.append(n1.rjust(max_chars + 2))
		line2.append(operator + n2.rjust(max_chars + 1))
		line3.append("-" * (max_chars + 2))
		if show_result:
			# Calculate and create result line
			n3 = str(int(n1) + int(n2) if operator == "+" else int(n1) - int(n2))
			line4.append(n3.rjust(max_chars + 2))

	lines = [
	    space_between_problems.join(line1),
	    space_between_problems.join(line2),
	    space_between_problems.join(line3),
	]

	if show_result:
		lines.append(space_between_problems.join(line4))

	return "\n".join(lines)
