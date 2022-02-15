# wandb

```shell
# can not find libdevice.10.bc
export XLA_FLAGS="--xla_gpu_cuda_data_dir=/usr/local/cuda-11.2"
echo 'export XLA_FLAGS="--xla_gpu_cuda_data_dir=/usr/local/cuda-11.2"' >> $HOME/dotfiles/zsh/machine_local_after
echo 'export WANDB_ENTITY=qinsheng' >> $HOME/dotfiles/zsh/machine_local_after
echo 'export WANDB_API_KEY=e63a92374c00b1da163fabe6331f38a8efa4fed0' >> $HOME/dotfiles/zsh/machine_local_after
```

# Run

```shell
# default setting
python3 -m dqn_zoo.prioritized.run_atari --results_csv_path=/tmp/results.csv

# test setting
python3 -m dqn_zoo.prioritized.run_atari --replay_capacity=1000 --target_network_update_period=40 --num_iterations=10 --num_train_frames=1000 --num_eval_frames=500 --eval_freq=5 --wandb=true

python3 -m dqn_zoo.exp.run_atari --replay_capacity=1000 --target_network_update_period=40 --num_iterations=10 --num_train_frames=1000 --num_eval_frames=500 --eval_freq=5

# baseline
python3 -m dqn_zoo.prioritized.run_atari --num_train_frames=100000 --num_iterations=2000 --num_eval_frames=200000 --eval_freq=10 --wandb=true
```