#Task 4

import numpy as np

#states and matrix
states=["Sunny", "Cloudy", "Rainy"]
transition_matrix=np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

#markov model
def simulate_process(initial_state, days):
  current_state=states.index(initial_state)
  state_sequence=[states[current_state]]
  for _ in range(days):
    next_state=np.random.choice(
        [0, 1, 2], 
        p=transition_matrix[current_state]
    )
    state_sequence.append(states[next_state])
    current_state=next_state
  return state_sequence

#simulate
initial_state="Sunny"
days = 10
sequence=simulate_process(initial_state, days)

#output
print(f"Weather sequence for {days} days starting from {initial_state}:")
print(" -> ".join(sequence))

#rainy days
print(f"\nRainy days in this sequence: {sequence.count("Rainy")}")

# prob
def estimate_prob(trials=10000):
  count=0
  for _ in range(trials):
    seq=simulate_process("Sunny", 10)
    if seq.count("Rainy") >= 3:
      count+=1
  return count/trials

prob=estimate_prob()
print(f"\nProbability of having at least 3 rainy days over the 10-day period is: {prob}")
