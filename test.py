import matplotlib.pyplot as plt
import csv
import sys

xlab = 'Time'
ylab = 'Distance [m]'
title = 'Anti-Collision Lidar Data Filter Test'

f1 = open(sys.argv[1] + '/non_filtered_data.csv', 'r')
f2 = open(sys.argv[1] + '/filtered_data.csv', 'r')

non_filtered_data_reader = csv.reader(f1)
filtered_data_reader = csv.reader(f2)

num_list = []
non_filtered_data_list = []
filtered_data_list = []

roi_chunk = (int(sys.argv[2]) + 1) * int(sys.argv[3])
i = 0
for row in non_filtered_data_reader:
	num_list.append(i)
	non_filtered_data_list.append(row[roi_chunk])
	i += 1

for row in filtered_data_reader:
	filtered_data_list.append(row[roi_chunk])	

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.plot(num_list, non_filtered_data_list, 'r', label='Unfiltered Data')
plt.plot(num_list, filtered_data_list, 'b', label='Filtered Data')
#plt.plot(num_list, non_filtered_data_list, 'r', num_list, filtered_data_list, 'b')
plt.legend(loc='upper right')
plt.show()
	
