#!/bin/bash

FILES=( merge.py )

TARGETDIR=~/bin

mkdir -p $TARGETDIR

CURRDIR=$(pwd)

for file in ${FILES[@]}
do
	ln -Fsv $CURRDIR/$file $TARGETDIR/$file
done
