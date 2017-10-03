#!/usr/bin/make -f
.PHONY: all

all: September November

September: %: %.tex
	latexmk -pdf $@
	pdfcrop September.pdf September.pdf

November: %: %.tex
	latexmk -pdf $@
	pdfcrop November.pdf November.pdf

.PHONY: clean

clean:
	latexmk -C
