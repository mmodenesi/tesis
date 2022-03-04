build_image:
	docker build -t tesis-latex:latest .

shell:
	docker run \
		-ti --rm \
		-v $(PWD)/src:/tesis \
		-v $(PWD)/build:/build \
		-w /tesis \
		tesis-latex:latest \
		bash

build:
	docker run \
		-ti --rm \
		-v $(PWD)/src:/tesis \
		-v $(PWD)/build:/build \
		-w /tesis \
		tesis-latex:latest \
		pdflatex -shell-escape -output-directory=/build tesis.tex

bib:
	docker run \
		-ti --rm \
		-v $(PWD)/src:/tesis \
		-v $(PWD)/build:/build \
		-w /tesis \
		tesis-latex:latest \
		biber /build/tesis.bcf

clean:
	rm -rf build/*

.PHONY: build
