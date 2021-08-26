import os
from conans import ConanFile, tools
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class FooConan(ConanFile):
    name = "Foo"
    description = "Simple header-only C library (part of Conan demo)"
    version = "0.1.0"
    settings = "os", "compiler", "arch", "build_type"
    no_copy_source = True
    generators = "CMakeDeps", "virtualenv"

    def generate(self):
        # TODO: Why does Conan not pick up the environment variable by itself?
        tc = CMakeToolchain(self, generator=os.getenv("CONAN_CMAKE_GENERATOR", None))
        tc.preprocessor_definitions["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def source(self):
        git = tools.Git(verify_ssl=False)
        git.clone(
            url="https://github.com/kolekanos/conandemo-libfoo.git",
            branch="master",
            shallow=True)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.includedirs = ["include"]

