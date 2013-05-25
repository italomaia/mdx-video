from distutils.core import setup

version = '0.2.0'

setup(
    name='mdx_video',
    version=version,
    description="Python-Markdown extension for easy video embedding",
    author="Tyler Lesmann, Italo Maia, Rafael Canovas",
    py_modules=["mdx_video"],
    install_requires=['Markdown>=2.2'],
)
