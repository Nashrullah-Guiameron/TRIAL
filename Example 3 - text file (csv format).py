import numpy as np

# Save to a text file (csv format)
# EXAMPLE 3

#1 save and wirte text file
Example3 = np.arange(20)
np.savetxt('Example3.csv', Example3, delimiter=',')


#2 Load data from text file
Example3 = np.loadtxt('Example3.csv', delimiter=',')
print(Example3)


# import numpy as np

# # Example data
# data = np.array([[10, 20], [30, 40], [50, 60]])
# # Save to a CSV file
# np.savetxt('data3.csv', data, delimiter=',')

# # Load data from CSV file
# data = np.loadtxt('data3.csv', delimiter=',')
# print(data)