import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="nameko_services",
    version="0.1.0",
    url="https://github.com/GTedHa/nameko_ros_demo",
    license='MIT',

    author="G.Ted",
    author_email="gted221@gmail.com",

    description="Nameko services with ROS node demo",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        'nameko==2.11.0',
    ],

    classifiers=[
        'Development Status :: 0 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
