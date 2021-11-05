# Sparsekit

## Building Sparsekit using CMake

### Step-1: Specify the location of installation

This will be by defining `CMAKE_INSTALL_PREFIX` on CLI:

```make
  cmake -DCMAKE_INSTALL_PREFIX:PATH=${EASIFEM_EXTPKGS} -S . -B ./build
```

### Step-2: Specify location of BLAS and LAPACK

There are two ways to do this: In the first approach, environment variable is defined,  these variables are `CMAKE_LAPACK_ROOT` and `CMAKE_BLAS_ROOT`, for examples:

```bash
export CMAKE_LAPACK_ROOT="/usr/local/opt/openblas/"
export CMAKE_BLAS_ROOT="/usr/local/opt/openblas/"
```

In the second approach define `CMAKE_LAPACK_ROOT` and `CMAKE_BLAS_ROOT` on CLI:

```bash
  cmake -DCMAKE_INSTALL_PREFIX:PATH=${EASIFEM_EXTPKGS}
  -DCMAKE_LAPACK_ROOT:PATH=/usr/local/opt/openblas/
  -DCMAKE_BLAS_ROOT:PATH=/usr/local/opt/openblas/
  -S . -B ./build
```

If the above two apporaches are not employed then define `USE_BLAS` on CLI:

```bash
  cmake -DCMAKE_INSTALL_PREFIX:PATH=${EASIFEM_EXTPKGS}
  -DUSE_BLAS="Netlib"
  -S . -B ./build
```

> `USE_BLAS` can take any value from the list: `Netlib` `OpenBLAS` `Atlas` `MKL`

### Step-3: Installation

```bash
  cmake --build ./build --target install
```

- This will install `/include` `/lib` `/share/cmake/Sparsekit` at `CMAKE_INSTALL_PREFIX`.
- `libSparsekit.dylib` or `libSparsekit.a` will be located at `/lib`
- `/share` contains cmake configuration file

### Step-4: Usage

- For cmake to find Sparsekit one need to define `CMAKE_PREFIX_PATH` on CLI.
- For linking use `Sparsekit::Sparsekit`

## Todo

- Build fortran flag for `Intel` and `PGI` fortran-compilers.
- Design test program
