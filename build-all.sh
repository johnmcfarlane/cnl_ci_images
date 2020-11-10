#!/usr/bin/env bash

set -euo pipefail

# Unless building in the pipeline, dockerfiles/1/* don't depend on dockerfiles/0
./build.py dockerfiles/0/* dockerfiles/1/*

./build.py dockerfiles/2/*

./build.py dockerfiles/3/*
./build.py dockerfiles/4/*
./build.py dockerfiles/5/*
