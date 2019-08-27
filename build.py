#!/usr/bin/env python3

from subprocess import call

dockerfiles = ["base-16.04", "base-18.04", "gcc-8", "gcc-7", "gcc-6", "gcc-5", "clang-6.0", "clang-5.0", "clang-4.0", "clang-3.9", "clang-3.8"]
for dockerfile in dockerfiles:
    image = "johnmcfarlane/cnl_ci:{}".format(dockerfile)
    call(["docker", "build", "-f", dockerfile, "--tag", image, "."])
    call(["docker", "push", image])
