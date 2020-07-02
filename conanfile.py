from conans import ConanFile, CMake, tools


class CmakeSimpleLibConan(ConanFile):
    name = "cmake_simple_lib"
    version = "0.1"
    license = "unlicense"
    author = "Richard Spindler <richard.spindler@gmail.com>"
    url = "https://github.com/oracle2025/cmake_simple_lib"
    description = "Demo for including a lib with CMake and Conan.io"
    topics = ("conan", "cmake", "example")
    generators = "cmake"
    exports_sources = "*", "!build/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["simple"]

