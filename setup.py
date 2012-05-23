from distutils.core import setup
from mdx_video import version

setup(name='mdx_video',
    version=version,
    description="Markdown 2.0 extension for easy video embedding",
    author="Italo Maia",
    url="https://github.com/italomaia/mdx-video",
    py_modules = ["mdx_video"],
    requires = ['markdown>=2.0'],
    )
