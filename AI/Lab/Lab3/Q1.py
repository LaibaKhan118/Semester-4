#Task 1
class Environment:
  def __init__(self, traffic="Heavy"):
    self.traffic = traffic

  def get_percept(self):
    return self.traffic


class ReflexAgent:
  def __init__(self):
    pass
  def act(self, percept):
    if percept == "Heavy":
      return "Extend Green Time"
    else:
      return "Normal Green Time"

def program(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} Traffic, Action: {action}")

agent = ReflexAgent()
environment = Environment("Heavy")
program(agent, environment)
environment1 = Environment("Light")
program(agent, environment1)
