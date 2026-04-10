#Task 3

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

#define structure
model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])
#define CPTs
cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.3],[0.7]]
)
cpd_fever=TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.1, 0.5],
        [0.9, 0.5]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)
cpd_cough=TabularCPD(
    variable='Cough',
    variable_card=2,
    values=[
        [0.2, 0.4],
        [0.8, 0.6]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)
cpd_fatigue=TabularCPD(
    variable='Fatigue',
    variable_card=2,
    values=[
        [0.3, 0.7],
        [0.7, 0.3]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)
cpd_chills=TabularCPD(
    variable='Chills',
    variable_card=2,
    values=[
        [0.4, 0.6],
        [0.6, 0.4]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

#add cpds
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
#verify
assert model.check_model(), "Model is incorrect"
print("Model Verified Successfully")

#inference
inference=VariableElimination(model)

#queries
# 1.
print("P(Disease | Fever=Yes, Cough=Yes)")
q1=inference.query(
    variables=['Disease'],
    evidence={'Fever': 1, 'Cough': 1}
)
print(q1)
# 2.
print("\nP(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
q2=inference.query(
    variables=['Disease'],
    evidence={'Fever': 1, 'Cough': 1, 'Chills': 1}
)
print(q2)
# 3.
print("\nP(Fatigue=Yes | Disease=Flu(0))")
q3=inference.query(
    variables=['Fatigue'],
    evidence={'Disease': 0}
)
print(q3)
