#!/usr/bin/env python3

from os.path import basename, dirname
from subprocess import check_call
from sys import argv


def build(filename, path, tag):
    # Work in cycles of build/push, build/push, build/push.
    # That way, all the base images are uploaded ready to pull again for each compiler image.
    check_call(["docker", "build", "-f", filename, "--tag", tag, path])
    check_call(["docker", "push", tag])


def build_image(step):
    print('=' * 70)
    print("{} -> {}".format(step[0], step[2]))
    build(*step)


if __name__ == "__main__":
    if len(argv) <= 1:
        print("Please provide dockerfile(s).")
        exit(1)

    # Base images are dependency of the other images, so build them first.
    filenames = sorted(argv[1:])

    # From full path, extract salient strings
    plan = [(filename, dirname(filename), "johnmcfarlane/cnl_ci:{}".format(basename(filename))) for filename in
            filenames]
    
    print('\n'.join([image for filename, dir, image in plan]))

    for step in plan:
        build_image(step);
