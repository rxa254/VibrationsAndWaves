#!/usr/bin/make -f
.PHONY: all clean
all: Lecture01 Lecture02 Lecture03

Lecture01: %: %.tex
	latexmk -pdf Lecture01.tex

Lecture02: %: %.tex
	latexmk -pdf Lecture02.tex

Lecture03: %: %.tex
	latexmk -pdf Lecture03.tex

.PHONY: clean
clean:
	latexmk -C
