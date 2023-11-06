import numpy as np
filename = 'D:/path/to/the/save/folder/ABIDE_pcp/abide.npy'
data = np.load(filename, allow_pickle=True)
print(data)
