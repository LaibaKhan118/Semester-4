#Task 5
from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, vars):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.vars = vars
        self.count = 0
    def on_solution_callback(self):
        self.count += 1
        print(f"Solution {self.count}: ", end="")
        for v in self.vars:
            print(f"{v.Name()}={self.Value(v)}", end=" ")
        print()

model = cp_model.CpModel()
A = model.NewIntVar(0, 3, 'A')
B = model.NewIntVar(0, 3, 'B')
C = model.NewIntVar(0, 3, 'C')

model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True
printer = SolutionPrinter([A, B, C])
solver.Solve(model, printer)
print(f"Total solutions: {printer.count}")
