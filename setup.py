from distutils.core import setup

version = '0.1.7.2'

setup(name='mdx_video',
    version=version,
    description="Markdown 2.0 extension for easy video embedding",
    author="Italo Maia",
    url="https://github.com/italomaia/mdx-video",
    py_modules = ["mdx_video"],
    requires=['markdown (>=2.0) (<=2.0.9)',],
)
