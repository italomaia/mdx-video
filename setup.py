from distutils.core import setup
from mdx_video import version

setup(name='mdx_video',
    version=version,
    description="Markdown 2.0 extension for easy video embedding",
    author="Tyler Lesmann",
    author_email="redhatcat@gmail.com",
    url="http://code.tylerlesmann.com/mdx_video2",
    py_modules = ["mdx_video"],
    )
