cmake_minimum_required(VERSION 3.28.1)

# Project description
project(AdvancedProgrammingExam
		VERSION 1.0
		DESCRIPTION "Advanced Programming Exam"
		LANGUAGES CXX
)

# C++ Standard
set(CMAKE_CXX_STANDARD 17)

# Compilation flags
set(CMAKE_CXX_FLAGSS "-${CMAKE_CXX_FLAGSS} -Wall -Werror -Wextra -Wpendantic")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

# Adding subdirectories
add_subdirectory(src)  
add_subdirectory(apps) 
