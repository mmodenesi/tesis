build_image:
	docker build -t tesis-latex:latest .

run:
	docker run \
		-ti --rm \
		-v $(PWD)/src:/tesis \
		-v $(PWD)/build:/build \
		-w /tesis \
		tesis-latex:latest bash

build:
	docker run \
		-ti --rm \
		-v $(PWD)/src:/tesis \
		-v $(PWD)/build:/build \
		-w /tesis \
		tesis-latex:latest \
		pdflatex -output-directory=/build pruebas/p1.tex

clean:
	rm -rf build/*

.PHONY: build
