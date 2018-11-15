import numpy

def create_matrix(row, column):
	matrix = numpy.zeros(shape=(row, column))
	return matrix

a = create_matrix(2,2)
print(a)

def nagivate_matrix(matrix, max_row, max_column):
	move_count = 0
	row = 0
	column = 0
	while matrix[row][column] <= max_row:
		while matrix 

		row += 1
		move_count += 1