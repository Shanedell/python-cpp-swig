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
g++ -std=c++11 -fPIC -c pycpp.cpp pycpp_wrap.cxx $(python3-config --include)
cd ../
```

### Generate lib file

Works for both MacOS and Linux.

```bash
g++ -shared $(python3-config --ldflags) -o pycpp/_pycpp.so pycpp/pycpp.o pycpp/pycpp_wrap.o
```

## Compiling python bindings - Auto

Using the `gen_lib` script you can easily generate the swig bindings, generate the c++ binary file and the library file.
