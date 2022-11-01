#!/bin/bash
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #

# Creates cmdutils symlink files into your target directory

TARGETDIR=~/bin

mkdir -p $TARGETDIR

CURRDIR=$(pwd)

for i in *
do
    if [[ $i == "LICENSE" ]] || [[ $i == "INFO.md" ]] || [[ $i == "README.md" ]] || [[ $i == "Makefile" ]]; then continue; fi
    NAME=$(echo $i | cut -f 1 -d.)
    ln -Fsv $CURRDIR/$i $TARGETDIR/$NAME
done
