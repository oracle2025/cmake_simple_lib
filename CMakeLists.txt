cmake_minimum_required(VERSION 2.8.11)

project(simple_lib CXX)

if("${CMAKE_CXX_COMPILER_ID}" MATCHES "(GNU|Clang)")
    set(CMAKE_CXX_FLAGS "-std=c++11")
endif()

add_subdirectory(src)
