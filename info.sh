#!/bin/bash
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #

# Creates the INFO.txt file for cmdutils

inf=INFO.md
temp=/tmp/info

printf "# Information file for cmdutils\n\n" > $inf
echo "Copyright (C) 2022 Fede Camara Halac" >> $inf
date >> $inf
printf "\n%9s %7s %s" "Name" "Env" "Description" >> $inf
printf "\n%s %s %s" "---------" "-------" "--------------------------------------------------------------" >> $inf

echo > $temp

for i in src/*
do
    name=$(echo $i | cut -f 1 -d.)
    env=$(basename $(head -n1 $i))
    text=$(head -n7 $i | tail -n1 | sed 's/^#//;s/\"\"\"$//;s/^\"\"\"//;s/^ //;s/ $//')
    printf "%9s %7s %s\n" ${name/src\//} $env "$text" >> $temp
done

sort -k2 $temp >> $inf
