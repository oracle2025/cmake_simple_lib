
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

add_library(simple STATIC simple_lib.cpp)

install(TARGETS simple
	ARCHIVE DESTINATION lib)

install(FILES ../include/simple_lib.h DESTINATION include)
