
import matplotlib.pyplot as plt
import numpy as np
import os



columns_to_plot = [1,2,5,6]
variables = ["displacement_x", "displacement_y", "rotation_y", "rotation_z"]

results_path = os.path.join('results')

data = np.loadtxt(os.path.join(results_path,"RigidBody.dat"),dtype=float,skiprows=1)

for column, variable in zip(columns_to_plot, variables):

    plt.plot(data[:,0], data[:,column], label=variable)

plt.legend()
plt.savefig("displacements")
#plt.show()



