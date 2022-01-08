# SWIG Python and C++ Example

This repo is an example of bindings created via SWIG between C++ example. Code can
be used for both Mac and Linux.

## Requirements

- **swig** to generate language bindings (http://www.swig.org/svn.html)
- **python3** for running the shared library
- **c++ compiler** for creating the shared libraried (use `g++`)

## Generate SWIG bindings

```bash
swig -v -python -c++ -outdir pycpp pycpp/pycpp.i
```

Updates `pycpp/pycpp.py` and `pycpp/pycpp_wrap.cxx`.

This needs to be done every time the code for `pycpp.cpp` and `pycpp.h` changes. 

## Compiling python bindings - Manual

### Generate C++ Binary

Works for both MacOS and Linux.

```bash
cd pycpp
g++ -std=c++11 -fPIC -c pycpp.cpp pycpp_wrap.cxx $(python3-config --includes)
cd ../
```

### Generate lib file

Works for both MacOS and Linux.

```bash
g++ -shared $(python3-config --ldflags) -o pycpp/_pycpp.so pycpp/pycpp.o pycpp/pycpp_wrap.o
```

### Test library

```bash
pipenv run test -v
```

## Compiling python bindings - Auto

Two Options:

- 1.) You can run the `gen_lib` file locally and everything will be built
- 2.) Run `docker-compose up -d --build`
  - Creates a container that builds all the bindings, creates the c++ binary and creates the library file
  - Creates another container once the build one finishes that runs the tests