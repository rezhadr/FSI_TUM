from __future__ import print_function, absolute_import, division #makes KratosMultiphysics backward compatible with python 2.6 and 2.7

import KratosMultiphysics
from KratosMultiphysics.CoSimulationApplication.solver_wrappers.rigid_body.rigid_body_solver import RigidBodySolver

import sys
import time

if __name__ == "__main__":

    with open("ProjectParameters.json",'r') as parameter_file:
        parameters = KratosMultiphysics.Parameters(parameter_file.read())

    model = KratosMultiphysics.Model()
    simulation = RigidBodySolver(model, parameters)
    simulation.Run()
