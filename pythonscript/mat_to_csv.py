import scipy.io
import numpy as np

data = scipy.io.loadmat("data/glass.mat")
print(data['__header__'])

for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("data/"+i+".csv"),data[i],delimiter=',')