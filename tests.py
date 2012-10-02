# -*- coding:utf-8 -*-

import os
import markdown
from mdx_video import VideoExtension
import unittest

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
base_filename = os.path.join(BASE_DIR, 'output/base.html')

video_providers = {
    "youtube": "http://www.youtube.com/watch?v=mFi2B8nYdhc",
    "vimeo": "http://vimeo.com/43332921",
    "bliptv": "http://blip.tv/play/AYOBwHQC.x",
    "veoh": "http://www.veoh.com/watch/v352792842YDSmD5N",
    "metacafe": "http://www.metacafe.com/watch/9168343/playstation_3_super_slim_250gb_game_of_the_year_edition_unboxing_unbox_therapy_extras/",
}

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

with open(base_filename) as file:
    html_text = file.read()

class MDTestCase(unittest.TestCase):
    def build_example(self, name, url):
        filename = "output/%s.html" % name
        output = markdown.markdown(url, extensions=['video'])

        with open(os.path.join(BASE_DIR, filename), 'w') as file:
            file.write(html_text % {'content':output})


class TestVideoRendering(MDTestCase):
    def test_build_examples(self):
        for name, url in video_providers.items():
            self.build_example(name, url)

if __name__ == '__main__':
    unittest.main()