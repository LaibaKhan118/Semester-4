#Task 4
from ortools.sat.python import cp_model

model = cp_model.CpModel()
A = model.NewIntVar(0, 3, 'A')
B = model.NewIntVar(0, 3, 'B')
C = model.NewIntVar(0, 3, 'C')

model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"A = {solver.Value(A)}")
    print(f"B = {solver.Value(B)}")
    print(f"C = {solver.Value(C)}")
else:
    print("No solution found.")
