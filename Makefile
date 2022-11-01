#!/usr/bin/make
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #

# Makefile for cmdutils

DESTDIR ?= ~/bin

install:
	./linker.sh $(DESTDIR)

info:
	./info.sh

all:
	make info
	make install
