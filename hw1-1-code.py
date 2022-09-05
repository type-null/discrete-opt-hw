# ESI 6448 - Discrete Optimization Theory
#  Homework 1, Question 1.1

import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model("hw1-1")
m.setParam("LogFile", "hw1-1-log.log")

# Create variables
x1 = m.addVar(lb=0, vtype=GRB.INTEGER, name="x1")
x2 = m.addVar(lb=0, vtype=GRB.INTEGER, name="x2")

# Set objective
m.setObjective(x1 + 0.64 * x2, GRB.MAXIMIZE)

# Add constraints
m.addConstr(50 * x1 + 30 * x2 <= 250, "c0")
m.addConstr(3 * x1 - 2 * x2 >= -4, "c1")

# Optimize model
m.optimize()

for v in m.getVars():
    print('%s %g' % (v.VarName, v.X))

print('Obj: %g' % m.ObjVal)