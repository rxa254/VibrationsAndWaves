#!/usr/bin/make -f
.PHONY: all

all: September

September: %: %.tex
	latexmk -pdf $@
	pdfcrop September.pdf September.pdf

.PHONY: clean

clean:
	latexmk -C
