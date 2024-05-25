import numpy as np

# Save to a text file (txt format)
# EXAMPLE 1

#1 save and wirte text file
Example1 = np.array([[0,8,2,4,2],
                     [4,9,7,4,2],
                     [6,1,0,6,3]])
np.savetxt('Example1.txt', Example1)


#2 Load data from text file
Example1 = np.loadtxt('Example1.txt')
print(Example1)
