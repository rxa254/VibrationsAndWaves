#!/usr/bin/make -f
.PHONY: all clean
all: quiz1 quiz2 quiz3

quiz1: %: %.tex
	latexmk -pdf $@

quiz2: %: %.tex
	latexmk -pdf $@

quiz3: %: %.tex
	latexmk -pdf $@


.PHONY: clean
clean:
	latexmk -C
