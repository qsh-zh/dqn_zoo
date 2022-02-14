set -eu

if [ "$#" -ne 1 ]; then
    port=https://gitlab.com/zqsh419/dotfiles.git
else
    port=git@gitlab.com:zqsh419/dotfiles.git
fi


ensure_installed() {
  if ! dpkg -s "$1" > /dev/null ; then
    sudo apt update
    sudo apt-get -y install "$@"
  fi
}

ensure_installed powerline
ensure_installed vim
ensure_installed tmux
ensure_installed xclip
ensure_installed g++
ensure_installed python3-dev
ensure_installed silversearcher-ag
ensure_installed python3-venv
ensure_installed git-extras


cd $HOME
git clone $port

cd dotfiles
git checkout container
bash install

