def matrix_rows(matrix):
	"""
	returns rows of matrix
	: param : matrix : represented as list of lists
	: return : rows
	: rtype : list of strings
	"""
	rows = [' '.join(matrix[j]) for j in range(len(matrix))]

	return rows


def matrix_cols(matrix):
	"""
	returns cols of matrix
	: param : matrix : represented as list of lists
	: return : cols
	: rtype : list of strings
	"""
	cols = [' '.join(elem) for elem in list(zip(*matrix))]

	return cols


def rows_to_matrix(rows):
	"""
	returns matrix from list of rows
	: param : rows : list of rows
	: return : matrix
	: rtype : list of lists
	"""
	matrix = [s.split() for s in rows]
	return matrix


def str_to_matrix(input_str):
	"""
	returns matrix from string
	: param : str : string which is matrix
	: return : matrix
	: rtype : list of lists
	"""
	rows = input_str.split('\n')
	matrix = rows_to_matrix(rows)

	return matrix


def matrix_to_str(matrix):
	"""
	returns string which represent matrix
	: param : matrix : matrix as list of lists
	: return : string
	: rtype : str
	"""
	m_rows = matrix_rows(matrix)
	out_str = '\n'.join(m_rows)

	return out_str


input_str = '1 2 3 4\n5 6 7 8\n9 10 11 12'

matrix = str_to_matrix(input_str)

print('matrix:\n', matrix)

m_rows = matrix_rows(matrix)
print('rows:\n', m_rows)

m_cols = matrix_cols(matrix)
print('columns\n', m_cols)

matrix = rows_to_matrix(m_cols)

print('transposed matrix\n', matrix)

output_str = matrix_to_str(matrix)
print('str from matrix\n', output_str)
