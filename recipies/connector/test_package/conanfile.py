from conans import ConanFile, CMake
import os

class Sqlpp11ConnectorPostgresTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake", "virtualrunenv")

    def configure(self):
        self.options['sqlpp11-connector-postgres'].SHARED = True

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        #self.run(". .{0}activate_run.{1} && bin{0}connector_test".format(os.sep, "bat" if self.settings.os == "Windows" else "sh"))
        pass