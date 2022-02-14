set -eu

apt-get update

# system
apt-get install -y --fix-missing --no-install-recommends\
    build-essential ca-certificates sudo vim zsh curl tmux wget iputils-ping less software-properties-common ack rsync

# terminal enhance
apt-get install -y --fix-missing --no-install-recommends trash-cli ssh openssh-client

# powerline-gitstatus 
apt-get install -y --fix-missing --no-install-recommends\
    apt-file apt-rdepends aptitude powerline
apt-file update

# # install vim, if vim in apt repo is not update
# add-apt-repository -y ppa:jonathonf/vim
# apt-get update
# apt-get install -y --fix-missing --no-install-recommends vim
# add-apt-repository -r -y ppa:jonathonf/vim # remove the repo