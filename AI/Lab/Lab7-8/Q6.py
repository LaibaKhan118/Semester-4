#Task 6
from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.NewIntVar(0, 20, 'x')
y = model.NewIntVar(0, 20, 'y')
z = model.NewIntVar(0, 20, 'z')

model.Add(x + 2*y + z <= 20)
model.Add(3*x + y <= 18)

model.Maximize(4*x + 2*y + z)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print(f"Optimal value: {solver.ObjectiveValue()}")
    print(f"x = {solver.Value(x)}")
    print(f"y = {solver.Value(y)}")
    print(f"z = {solver.Value(z)}")
else:
    print("No optimal solution found.")
