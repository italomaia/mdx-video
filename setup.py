from setuptools import setup, find_packages

version = '0.1.7.6'

setup(
    name='mdx_video',
    version=version,
    description="Python-Markdown extension for easy video embedding",
    author="Tyler Lesmann, Italo Maia, Rafael Canovas",
    py_modules=["mdx_video"],
    install_requires=['markdown>=2.2'],
)
