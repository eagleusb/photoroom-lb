SHELL 	:= /bin/bash
VERSION := $(shell git describe --tags --abbrev=5 --always)

.PHONY = devel tests

devel:
	cd api && pipenv run devel

tests:
	curl -XPOST -H 'Content-Type: application/json' -d@test/model.json 0:5000/inference
