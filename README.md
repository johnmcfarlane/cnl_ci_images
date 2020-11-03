# cnl_ci_images

Docker images used to perform [CNL](https://github.com/johnmcfarlane/cnl/)
integration. You are probably here by accident but welcome anyway!

## Instructions

Log in:

```sh
docker login
```

To build something, e.g. johnmcfarlane/cnl_ci:clang-6:

```sh
./build.py dockerfiles/2/clang-6
```

To build everything:

```sh
./build-all.sh
```
