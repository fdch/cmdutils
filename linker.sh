#!/bin/bash
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #

# Creates cmdutils symlink files into your target directory

FILES=( merge.py )

TARGETDIR=~/bin

mkdir -p $TARGETDIR

CURRDIR=$(pwd)

for file in ${FILES[@]}
do
	ln -Fsv $CURRDIR/$file $TARGETDIR/$file
done
