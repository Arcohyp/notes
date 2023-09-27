# Glossary

## Strategies to find the optimal policy
- **Policy-based methods**. The policy is usually trained with a neural network to select what action to take given a state. In this case it is the neural network which outputs the action that the agent should take instead of using a value function. Depending on the experience received by the environment, the neural network will be re-adjusted and will provide better actions.
- **Value-based methods**. In this case, a value function is trained to output the value of a state or a state-action pair that will represent our policy. However, this value doesn’t define what action the agent should take. In contrast, we need to specify the behavior of the agent given the output of the value function. For example, we could decide to adopt a policy to take the action that always leads to the biggest reward (Greedy Policy). In summary, the policy is a Greedy Policy (or whatever decision the user takes) that uses the values of the value-function to decide the actions to take.

## Among the value-based methods, we can find two main strategies
- **The state-value function**. For each state, the state-value function is the expected return if the agent starts in that state and follows the policy until the end.
- **The action-value function**. In contrast to the state-value function, the action-value calculates for each state and action pair the expected return if the agent starts in that state, takes that action, and then follows the policy forever after.

## Epsilon-greedy strategy:
- Common strategy used in reinforcement learning that involves balancing exploration and exploitation.
- Chooses the action with the highest expected reward with a probability of 1-epsilon.
- Chooses a random action with a probability of epsilon.
- Epsilon is typically decreased over time to shift focus towards exploitation.

## Greedy strategy:
- Involves always choosing the action that is expected to lead to the highest reward, based on the current knowledge of the environment. (Only exploitation)
- Always chooses the action with the highest expected reward.
- Does not include any exploration.
- Can be disadvantageous in environments with uncertainty or unknown optimal actions.

## Off-policy vs on-policy algorithms
- **Off-policy algorithms**: A different policy is used at training time and inference time
- **On-policy algorithms**: The same policy is used during training and inference

## Monte Carlo and Temporal Difference learning strategies
- **Monte Carlo (MC)**: Learning at the end of the episode. With Monte Carlo, we wait until the episode ends and then we update the value function (or policy function) from a complete episode.

- **Temporal Difference (TD)**: Learning at each step. With Temporal Difference Learning, we update the value function (or policy function) at each step without requiring a complete episode.

## Deep Q-Learning
- **Tabular Method**: Type of problem in which the state and action spaces are small enough to approximate value functions to be represented as arrays and tables. Q-learning is an example of tabular method since a table is used to represent the value for different state-action pairs.

- **Deep Q-Learning**: Method that trains a neural network to approximate, given a state, the different Q-values for each possible action at that state. It is used to solve problems when observational space is too big to apply a tabular Q-Learning approach.

- **Temporal Limitation** is a difficulty presented when the environment state is represented by frames. A frame by itself does not provide temporal information. In order to obtain temporal information, we need to stack a number of frames together.

## Phases of Deep Q-Learning:

- **Sampling**: Actions are performed, and observed experience tuples are stored in a replay memory.
- **Training**: Batches of tuples are selected randomly and the neural network updates its weights using gradient descent.

## Solutions to stabilize Deep Q-Learning:

- **Experience Replay**: A replay memory is created to save experiences samples that can be reused during training. This allows the agent to learn from the same experiences multiple times. Also, it helps the agent avoid forgetting previous experiences as it gets new ones.

## Random sampling from replay buffer allows to remove correlation in the observation sequences and prevents action values from oscillating or diverging catastrophically.

- **Fixed Q-Target**: In order to calculate the **Q-Target** we need to estimate the discounted optimal **Q-value** of the next state by using Bellman equation. The problem is that the same network weights are used to calculate the **Q-Target** and the **Q-value**. This means that everytime we are modifying the **Q-value**, the **Q-Target** also moves with it. To avoid this issue, a separate network with fixed parameters is used for estimating the Temporal Difference Target. The target network is updated by copying parameters from our Deep Q-Network after certain C steps.

- **Double DQN**: Method to handle overestimation of **Q-Values**. This solution uses two networks to decouple the action selection from the target Value generation:

-- **DQN Network** to select the best action to take for the next state (the action with the highest **Q-Value**)

-- **Target Network** to calculate the target **Q-Value** of taking that action at the next state. This approach reduces the **Q-Values** overestimation, it helps to train faster and have more stable learning.
