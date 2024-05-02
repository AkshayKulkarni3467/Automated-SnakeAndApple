from stable_baselines3 import PPO
import os
from snake import SnekEnv
import time



models_dir = f"models/1714578800/"
# logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

# if not os.path.exists(logdir):
# 	os.makedirs(logdir)

env = SnekEnv()
env.reset()

model_path = f"{models_dir}/950000.zip"
model = PPO.load(model_path,env=env)


#### Training loop ####
# TIMESTEPS = 10000
# iters = 0
# while True:
# 	iters += 1
# 	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
# 	model.save(f"{models_dir}/{TIMESTEPS*iters}")

### Testing loop ###
episodes = 500
for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs,rewards,done,info = env.step(action)
        print(rewards)