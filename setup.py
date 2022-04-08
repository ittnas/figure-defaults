from setuptools import setup

setup(name='figure-defaults',
      version='1.1',
      description='A library for easy manipulation of matplotlib default settings.',
      author='Antti Vepsäläinen',
      author_email='apvepsala@gmail.com',
      packages=['figure_defaults'],
      install_requires=['packaging', 'matplotlib'],
      package_dir={'': 'src'},
      zip_safe=True)