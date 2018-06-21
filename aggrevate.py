#aggrevate imitation learning
#based on ICML2015 Tutorial http://hunch.net/~l2s/merged.pdf
'''
1.Let learned policy π drive for t timesteps to obs. o
2.For each possible action a:
● Take action a, and let expert πref drive the rest
● Record the overall loss, ca
3.Update π based on example:
(o, 〈c1, c2,..., cK〉)
4.Goto (1)
'''

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
  
  
 '''
 Aggrevate for sequence labelling e.g. pos tagging
 1- train a model/policy on training data
 2- given a sentence choose one word w_i randomly and consider all the pos tags
 3- for each pos tag use the reference policy/training gold labels to complete the sentence tag/trajectory
 4- compute the loss of each pos tag t_i
 5- add a cost sensitive example to a dataset D w_i, t_i_cost for all possibe pos tags
 6-train a cost sensitive classifier again and go to 2
 '''
