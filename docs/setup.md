# Run DQN

```shell
# tesst setting
python3 -m dqn_zoo.dqn.run_atari --replay_capacity=1000 --target_network_update_period=40 --num_iterations=10 --num_train_frames=1000 --num_eval_frames=500 --eval_freq=5

# baseline
python3 -m dqn_zoo.dqn.run_atari --num_train_frames=100000 --num_iterations=2000 --num_eval_frames=200000 --eval_freq=10 --wandb=true
```

# Run Priority

```shell
# default setting
python3 -m dqn_zoo.prioritized.run_atari --results_csv_path=/tmp/results.csv

# test setting
python3 -m dqn_zoo.prioritized.run_atari --replay_capacity=1000 --target_network_update_period=40 --num_iterations=10 --num_train_frames=1000 --num_eval_frames=500 --eval_freq=5 --wandb=true

# baseline
python3 -m dqn_zoo.prioritized.run_atari --num_train_frames=100000 --num_iterations=2000 --num_eval_frames=200000 --eval_freq=10 --wandb=true
```

## exp

```shell
python3 -m dqn_zoo.exp.run_atari --replay_capacity=1000 --target_network_update_period=40 --num_iterations=10 --num_train_frames=1000 --num_eval_frames=500 --eval_freq=5

python3 -m dqn_zoo.exp.run_atari --num_train_frames=100000 --num_iterations=2000 --num_eval_frames=200000 --eval_freq=10 --wandb=true
```