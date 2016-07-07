import incor

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='incor',
      version=incor.__version__,
      install_requires=['watchdog>=0.8.2', 'psutil>=4.3.0'],
      description='INstant COde Runner compiles and executes the programs present in the mentioned folder '
                  'instantaneously as and when changes are saved.',
      url='https://github.com/lakshmanaram/Program-runner/',
      author='lakshmanaram, srivatsan-ramesh',
      author_email='lakshmanaram.n@gmail.com, sriramesh4@gmail.com',
      license='MIT',
      packages=['incor'],
      entry_points={
          'console_scripts': ['incor=incor.main:main'],
      },
      zip_safe=False)
