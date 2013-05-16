# -*- coding:utf-8 -*-

import os
import markdown
import unittest
from mdx_video import VideoExtension

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TESTS_DIR = os.path.join(BASE_DIR, 'tests')

PROVIDERS = {
    "dailymotion": "http://www.dailymotion.com/video/xostx9_nyan-cat-original_music?search_algo=2#.UYMMO0kyY0g",
    "metacafe": "http://www.metacafe.com/watch/9168343/playstation_3_super_slim_250gb_game_of_the_year_edition_unboxing_unbox_therapy_extras/",
    "veoh": "http://www.veoh.com/watch/v352792842YDSmD5N",
    "vimeo": "http://vimeo.com/43332921",
    "yahoo": "http://screen.yahoo.com/mansome-169-ultimate-dj-party-040000302.html",
    "youtube": "http://www.youtube.com/watch?v=mFi2B8nYdhc",
    "youtube_short": "http://youtu.be/QH2-TGUlwu4",
}

if not os.path.exists(TESTS_DIR):
    os.mkdir(TESTS_DIR)


class MDTestCase(unittest.TestCase):
    def test_providers(self):
        for name, url in PROVIDERS.items():
            filename = name + '.html'
            output = markdown.markdown(url, extensions=[VideoExtension({})])

            with open(os.path.join(TESTS_DIR, filename), 'w') as f:
                f.write(output)


if __name__ == '__main__':
    unittest.main()
