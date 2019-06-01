from setuptools import setup, find_packages

setup(name='confighelper',
      version='0.0.1',
      url='https://github.com/Sotaneum/ConfigHelper',
      license='MIT',
      author='Donggun LEE',
      author_email='gnyotnu39@gmail.com',
      description='Can use it to save or recall preferences from Python.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      test_suite='')