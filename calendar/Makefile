#!/usr/bin/make -f
.PHONY: all

all: September

September: %: %.tex
	latexmk -pdf $@

.PHONY: clean

clean:
	latexmk -C
