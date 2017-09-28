#!/usr/bin/make -f
.PHONY: all clean
all: Lecture01 Lecture02

Lecture01: %: %.tex
	latexmk -pdf Lecture01.tex

Lecture02: %: %.tex
	latexmk -pdf -pvc Lecture02.tex

.PHONY: clean
clean:
	latexmk -C
