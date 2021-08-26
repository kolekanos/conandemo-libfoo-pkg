# conandemo-libfoo-pkg
Conan recipe for packaging libfoo

## Build steps

```bash
$ CONAN_CMAKE_GENERATOR="MSYS Makefiles" conan create . kolekanos/testing -pr:h profile-k -pr:b profile-k
```

with `profile-k`:

```ini
[settings]
os=Windows
arch=x86_64
compiler=gcc
compiler.version=10
compiler.libcxx=libstdc++11
build_type=Release
[options]
[build_requires]
[env]
```

