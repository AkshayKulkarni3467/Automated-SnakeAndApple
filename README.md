The rules of snake and apple game are as follows:
If the snake eats an apple, its length increases.
If the snake crosses the boundary or touches itself, it dies.
The score is the amount of apples collected.

![image](https://github.com/AkshayKulkarni3467/Automated-SnakeAndApple/assets/129979542/7616c5fd-a8ce-4317-8d6d-d402f2fb4a4f)

Training an RL agent using stable-baselines3. Here a custom environment is created using openai-gym of snake and apple and the agent is trained on it. Tensorboard is used to check the logs of mean and reward.

Here the observation space (feature space) is given by:

Position of head of snake, position of apple, snake length, previous actions

The action space is given by:

UP, DOWN, LEFT, RIGHT

The reward is given by:

For each step taken : ((250 - euclidean distance to apple) + apple_reward)/100

Mean length increase of snake and mean total rewards after 1 million steps:

![len_and_rew_mean](https://github.com/AkshayKulkarni3467/Automated-SnakeAndApple/assets/129979542/42e17af3-c2fa-44fb-a680-de19c9e7c308)

Maximum reward achieved is between 800k-810k steps:

![max_rew](https://github.com/AkshayKulkarni3467/Automated-SnakeAndApple/assets/129979542/50a42fd2-c377-43f1-b33d-487b27136b76)

Visualization of training (about 800k steps in):

https://github.com/AkshayKulkarni3467/Automated-SnakeAndApple/assets/129979542/5f8637f0-4a0e-4291-b902-9f8abda6af79

