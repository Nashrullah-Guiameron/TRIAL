import numpy as np

# Save to a binary file in .npy format
# EXAMPLE 2

#1 save and wirte binary file
Example2 = np.array([[5,5,2],
                    [6,2,3],
                    [9,8,4],
                    [6,9,1],
                    [4,5,0]])
np.save('Example2.npy', Example2)



#2 Load data from .npy file
Example2 = np.load('Example2.npy')
print(Example2)