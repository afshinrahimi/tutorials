#aggrevate imitation learning
#based on ICML2015 Tutorial http://hunch.net/~l2s/merged.pdf

observations, actions = load_data()
def expert_action(obs):
  return action

class Model:
  def predict(observation):
    return action
  def train(observations, actions):
    pass #train the model
Model.train(observations, actions)

time_steps = 10
for i in range(agrgrevate_iters):
  obs = reset_game()
  for t in range(time_steps):
    obs = model.predict(obs)
    obs_models = []
    for action in all_possible_actions:
      obs_model = play(action)
      obs_models.append(obs_model)
    #play with expert policy
    all_action_loss = {}
    for i, obs_model in enumerate(obs_models):
       _obs = obs_model
       while not finished:
         act_gold = expert_action(_obs)
         _obs, loss = play(act_gold)
      all_action_loss[obs_model] = loss
    add cost sensitive sample obs, all_action_loss.values() to dataset D_i
  Model.train(D_i)
  
        
