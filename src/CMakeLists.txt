
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

add_library(simple STATIC simple_lib.cpp)

install(TARGETS simple
	ARCHIVE DESTINATION ${PROJECT_BINARY_DIR}/lib)

