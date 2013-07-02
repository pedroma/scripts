#!/bin/bash

rm -rf .ssh/
ln -s ~/Dropbox/confs/.ssh ~/.ssh
#ln -s ~/Dropbox/confs/.subversion/ ~/.subversion
ln -s ~/Dropbox/scripts ~/scripts
rm -rf Documents
ln -s ~/Dropbox/Documents ~/Documents
ln -s ~/Dropbox/confs/.synergy.conf ~/.synergy.conf
rm ~/.bashrc
ln -s ~/Dropbox/confs/.bashrc ~/.bashrc
ln -s ~/Dropbox/confs/.python.py ~/.python.py
ln -s ~/Dropbox/confs/.vimrc ~/.vimrc
ln -s ~/Dropbox/confs/.vim_runtime ~/.vim_runtime
ln -s ~/Dropbox/confs/.xbindkeysrc ~/.xbindkeysrc
#ln -s ~/Dropbox/Projects/ ~/Projects
