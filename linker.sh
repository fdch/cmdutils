#!/bin/bash
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #

# Creates cmdutils symlink files into your target directory

if [[ $1 ]]
then
    TARGETDIR="$1"
else
    echo "Provide a target directory"
    exit 1
fi

mkdir -p $TARGETDIR

CURRDIR=$(pwd)

cd src

for i in *
do
    NAME=$(echo $i | cut -f 1 -d.)
    echo Linking $i $CURRDIR/src/$i $TARGETDIR/$NAME
    ln -Fsv $CURRDIR/src/$i $TARGETDIR/$NAME
done

