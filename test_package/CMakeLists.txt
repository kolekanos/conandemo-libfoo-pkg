cmake_minimum_required(VERSION 3.20)
project(PackageTest C)

set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_BINARY_DIR}")

find_package("Foo" REQUIRED)

add_executable(example example.c)

target_compile_options(example
    PRIVATE 
        $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>>:-W>
        $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>>:-Wall>
        $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>>:-Wextra>
        $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>>:-pedantic>
)

target_link_libraries(example Foo::Foo)

