from setuptools import setup

setup(name='awsnapshots',
      version='0.1',
      description='Simple tool to manage AWS Volume Snapshots using the AWS API',
      url='http://github.com/jrhames/AWSnapshots',
      author='Jr. Hames',
      author_email='jr@hames.com.br',
      license='MIT',
      packages=['awsnapshots'],
      install_requires=['boto'],
      zip_safe=False)