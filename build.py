#!/usr/bin/env python3

from multiprocessing import Pool
from os.path import basename, dirname
from subprocess import CalledProcessError, check_output
from sys import argv


def run_subprocess(args):
    print("running '{}'...".format(' '.join(args)))
    try:
        print(check_output(args).decode('utf-8'))
        print("... '{}' succeeded".format(' '.join(args)))
    except CalledProcessError as e:
        print(e.output.decode('utf-8'))
        print("... '{}' failed".format(' '.join(args)))
        raise


def build(filename, path, tag):
    # Work in cycles of build/push, build/push, build/push.
    # That way, all the base images are uploaded ready to pull again for each compiler image.
    run_subprocess(["docker", "build", "-f", filename, "--tag", tag, path])
    run_subprocess(["docker", "push", tag])


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

    with Pool() as p:
        p.map(build_image, plan)
