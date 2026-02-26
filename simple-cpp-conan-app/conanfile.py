from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class MyApp(ConanFile):
    name = "myapp"
    version = "0.1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    requires = "fmt/10.1.1"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("myapp*", dst="bin", src="build")

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
