#!/usr/bin/make -f
.PHONY: all
all: Lecture01

Lecture01: %: %.tex
	latexmk -pdf $@

.PHONY: clean
clean:
	latexmk -C
