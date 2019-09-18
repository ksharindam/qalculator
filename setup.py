from setuptools import setup
from qalculator import __version__

def readme():
    with open('README.md') as f:
        return f.read()

setup(
      name='qalculator',
      version=__version__,
      description='A simple Calculator written in PyQt4',
      long_description=readme(),
      long_description_content_type = 'text/markdown',
      keywords='pyqt pyqt4 calculator',
      url='http://github.com/ksharindam/qalculator',
      author='Arindam Chaudhuri',
      author_email='ksharindam@gmail.com',
      license='GNU GPLv3',
#      install_requires=['PyQt4',      ],
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Environment :: X11 Applications :: Qt',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python :: 3.7',
      ],
      packages=['qalculator'],
      entry_points={
          'console_scripts': ['qalculator=qalculator.main:main'],
      },
      data_files=[
                 ('share/applications', ['files/qalculator.desktop']),
                 ('share/icons', ['files/qalculator.png'])
      ],
      include_package_data=True,
      zip_safe=False)
