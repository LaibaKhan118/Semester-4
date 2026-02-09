class UtilityAgent:
  def __init__(self, restaurants):
    self.restaurants = restaurants
  def action(self):
    utilities = {}
    for name, values in self.restaurants.items():
      utility = values["Rating"] - values["Distance"]
      utilities[name] = utility
      print(f"Restaurant {name}: Utility = {utility}")

    best = max(utilities, key=utilities.get)
    print(f"Selected Restaurant: {best}")

rest = {"A": {"Rating": 7, "Distance": 3}, "B": {"Rating": 9, "Distance": 5}}
agent = UtilityAgent(rest)
agent.action()
