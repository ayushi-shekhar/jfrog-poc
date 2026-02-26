cmake_minimum_required(VERSION 3.15)
project(MyApp)

find_package(fmt REQUIRED)

add_executable(myapp src/main.cpp)
target_link_libraries(myapp fmt::fmt)
