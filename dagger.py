#dagger imitation learning based on https://github.com/avisingh599/imitation-dagger/blob/master/dagger.py
#paper: https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf related work lols searn by hal daume

def get_expert_label(observation):
  return action

class Model:
  def train(observations, actions)
  def predict(observations)

#load observations e.g. images and actions e.g. steer angle from an Atari car game
observations, actions = load_data()

#train the classifier that given an image predicts the next wheel angle
model.train(observations, actions)

dagger_iters = 5
for i in range(dagger_iters):
  new_obs = []
  new_gold_wheels = []
  obs = reset_game()
  while game is not done:
    wheel = model.predict(obs)
    obs = game_feedback(wheel) #act according to the predicted wheel and get the observations and possibly reward from the game
    gold_wheel = get_expert_label(obs)
    new_obs.append(obs)
    new_gold_wheels.append(gold_wheel)
  
  observations = concat(observations, new_obs)
  actions = concat(actions, new_gold_wheels)
  model.train(observations, actions)
