# Definitions
build_output = runtime/glenn2vcf
runtime_fullpath = $(realpath runtime)
build_tool = runtime-container.DONE
git_commit ?= $(shell git log --pretty=oneline -n 1 -- ../glenn2vcf | cut -f1 -d " ")
name = quay.io/ucsc_cgl/glenn2vcf
tag = 2bb4bc2cf161bd2a2ef6047750b79cdda6a6408c--${git_commit}

# Steps
build: ${build_output} ${build_tool}

${build_output}: build/Dockerfile
	cd build && docker build -t glenn2vcf-build .
	docker run -v ${runtime_fullpath}:/data glenn2vcf-build cp /home/glenn2vcf/glenn2vcf /data

${build_tool}: ${build_output} runtime/Dockerfile
	cd runtime && docker build -t ${name}:${tag} .
	docker tag -f ${name}:${tag} ${name}:latest
	docker rmi -f glenn2vcf-build
	touch ${build_tool}

push: build
	# Requires ~/.dockercfg
	docker push ${name}:${tag}
	docker push ${name}:latest

test: build
	python test.py

clean:
	-rm ${build_tool}
	-rm ${build_output}
	docker rmi -f ${name}:${tag}
