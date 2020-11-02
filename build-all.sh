#!/usr/bin/env bash

set -euo pipefail

# Unless building in the pipeline, dockerfiles/1/* don't depend on dockerfiles/0
./build.py dockerfiles/0/* dockerfiles/1/*

# Technically, 3/*-head don't depend on dockerfiles/1 but they are parallel and sloooow!
./build.py dockerfiles/2/*

./build.py dockerfiles/3/clang-10-libstdcpp
./build.py dockerfiles/3/clang-11
./build.py dockerfiles/3/clang-head
./build.py dockerfiles/3/gcc-head
