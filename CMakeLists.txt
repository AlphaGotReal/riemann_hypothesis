cmake_minimum_required(VERSION 3.28)
project(cheat)
add_subdirectory(utils/pybind11)
pybind11_add_module(cheat src/cheat.cpp)
