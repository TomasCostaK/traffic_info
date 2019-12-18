from math import *

start = (2000,1000)
end = (1490,1499)

def divide_subs(start, end):

	if start[0] < end[0]:
		x_length = end[0] - start[0]
		increase_x = 1
	else:
		x_length = start[0] - end[0]
		increase_x = -1

	if start[1] < end[1]:
		y_length = end[1] - start[1]
		increase_y = 1
	else:
		y_length = start[1] - end[1]
		increase_y = -1

	path_length = hypot(x_length, y_length)
	num_subsections = int(path_length//500) + 1

	path_subsect = []
	end_section = tuple(start)

	for i in range(1,num_subsections):
		start_section = end_section
		end_section = (
				start[0] + i*x_length/num_subsections*increase_x,
				start[1] + i*y_length/num_subsections*increase_y
			)
		path_subsect.append((start_section, end_section))


	path_subsect.append((end_section,tuple(end)))
	return path_subsect

print("Street from", start, "to", end)
for a in divide_subs(start, end):
	print("Starts at", a[0], "ends at", a[1])
