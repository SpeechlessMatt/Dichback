import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='dichback',
      version='0.0.7',
      description='二分回溯算法，通过逻辑和-逻辑函数单元在有效数据集中查找符合逻辑单元判别条件的数据子集',
      long_description=long_description,    #包的详细介绍，一般在README.md文件内
      long_description_content_type="text/markdown",
      url='https://github.com/SpeechlessMatt/Dichback',
      author='Czy_4201b',
      author_email='speechlessmatt@qq.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      zip_safe=False)