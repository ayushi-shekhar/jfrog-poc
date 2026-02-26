from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
import os

class MyApp(ConanFile):
    name = "myapp"
    version = "0.1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    requires = "fmt/10.1.1"

    exports_sources = "*"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(
            self,
            pattern="myapp*",
            dst=os.path.join(self.package_folder, "bin"),
            src=os.path.join(self.build_folder)
        )

    def package_info(self):
        self.cpp_info.bindirs = ["bin"]