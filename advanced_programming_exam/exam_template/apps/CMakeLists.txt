# Setting the name for the C++ library
set(LIBRARY_NAME your_cpp_library_name) # <--- CHANGE THIS

# Setting executables output
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)

# Finding third party libraries paths
# find_package(third_library_name REQUIRED) # <--- CHANGE THIS IF NEEDED

# Including directories
set(INCLUDE_DIRS
	${CMAKE_SOURCE_DIR}/include
    # ${third_library_name_INCLUDE_DIRS} # <--- CHANGE THIS IF NEEDED
)

include_directories(${INCLUDE_DIRS})

# Adding executables
add_executable(main main.cpp)

# Linking executables
target_link_libraries(main ${LIBRARY_NAME})
