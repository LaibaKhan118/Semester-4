#Task 2
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

#define structure
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

#define CPTs
cpd_intelligence = TabularCPD(
    variable='Intelligence',
    variable_card=2,
    values=[[0.3],[0.7]]
)

cpd_studyhours = TabularCPD(
    variable='StudyHours',
    variable_card=2,
    values=[[0.4],[0.6]]
)

cpd_difficulty = TabularCPD(
    variable='Difficulty',
    variable_card=2,
    values=[[0.4],[0.6]]
)
"""
Int  - studyh - diff -  A   -  B   -  C
high - suff   - hard - 0.6  - 0.3  - 0.1
high - suff   - easy - 0.9  - 0.08 - 0.02
high - insuf  - hard - 0.3  - 0.4  - 0.3
high - insuf  - easy - 0.6  - 0.3  - 0.1
low  - suff   - hard - 0.2  - 0.4  - 0.4
low  - suff   - easy - 0.5  - 0.35 - 0.15
low  - insuf  - hard - 0.05 - 0.25 - 0.7
low  - insuf  - easy - 0.2  - 0.4  - 0.4
"""
cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.6, 0.9, 0.3, 0.6, 0.2, 0.5, 0.05, 0.2],
        [0.3, 0.08, 0.4, 0.3, 0.4, 0.35, 0.25, 0.4],
        [0.1, 0.02, 0.3, 0.1, 0.4, 0.15, 0.7, 0.4]],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)
cpd_pass = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.05, 0.8, 0.5],
        [0.95, 0.2, 0.5]],
    evidence=['Grade'],
    evidence_card=[3]
)

#add to model
model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)
#verify
assert model.check_model(), "The model is incorrect"
print("Model verified successfully.\n")

#inference
inference=VariableElimination(model)

#query1: P(Pass | StudyHours=Sufficient(0), Difficulty=Hard(0))

q1=inference.query(
    variables=['Pass'],
    evidence={'StudyHours': 0, 'Difficulty': 0}
)
print("Query 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)")
print(q1)

#query2: P(Intelligence=High(0) | Pass=Yes(1))

q2=inference.query(
    variables=['Intelligence'],
    evidence={'Pass': 1}
)
print("\nQuery 2: P(Intelligence=High | Pass=Yes)")
print(q2)
