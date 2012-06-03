# -*- coding:utf-8 -*-

import os
import markdown
from mdx_video import VideoExtension
import unittest

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
base_filename = os.path.join(BASE_DIR, 'output/base.html')

youtube_example = {
    "name":"youtube",
    "text":"http://www.youtube.com/watch?v=mFi2B8nYdhc",
}

vimeo_example = {
    "name":"vimeo",
    "text":""
}

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

with open(base_filename) as file:
    html_text = file.read()

class MDTestCase(unittest.TestCase):
    def build_example(self, data):
        filename = "output/%s.html" % data['name']
        output = markdown.markdown(data['text'], extensions=['mdx_video'])

        with open(os.path.join(BASE_DIR, filename), 'w') as file:
            file.write(html_text % {'content':output})

class TestYoutube(MDTestCase):
    def test_youtube_render(self):
        self.build_example(youtube_example)


if __name__ == '__main__':
    unittest.main()