
import matplotlib.pyplot as plt
import numpy as np
import os



columns_to_plot = [1,6]
variables = ["displacement_x", "rotation_z"]

for solver in ["RBS1","RBS2"]:

    results_path = os.path.join('results', solver)

    data = np.loadtxt(os.path.join(results_path,"RigidBody.dat"),dtype=float,skiprows=1)

    for column, variable in zip(columns_to_plot, variables):

        plt.plot(data[:,0], data[:,column], label=solver+" - "+variable)

plt.legend()
plt.savefig("displacements")
#plt.show()



