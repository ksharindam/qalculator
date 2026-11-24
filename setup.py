from setuptools import setup
from setuptools.command.install import install
from setuptools.command.bdist_wheel import bdist_wheel
from subprocess import check_call

# allows to run commands before 'setup.py install' (used by dh-python)
class Install(install):
    def run(self):
        check_call("pyuic6 -o ./qalculator/ui_mainwindow.py ./data/window.ui".split())
        install.run(self)

# allows to run commands before building wheel
class BdistWheel(bdist_wheel):
    def finalize_options(self):
        check_call("pyuic6 -o ./qalculator/ui_mainwindow.py ./data/window.ui".split())
        bdist_wheel.finalize_options(self)


setup(
    name='qalculator',
    #version="6.0",
    packages=['qalculator'],
    entry_points={
        'gui_scripts': ['qalculator=qalculator.main:main'],
    },
    data_files=[
        ('share/applications', ['data/qalculator.desktop']),
        ('share/icons/hicolor/scalable/apps', ['data/qalculator.png'])
    ],
    cmdclass = {'bdist_wheel': BdistWheel, 'install': Install},
    include_package_data=True,
    zip_safe=False)
