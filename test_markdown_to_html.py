import unittest
from io import StringIO
from unittest.mock import patch
import os

from markdown_to_html import convert_markdown_to_html

class TestMarkdownToHTMLConverter(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.md"  
        self.output_file = "test_output.html"

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_conversion_default_format(self):
        markdown_text = "**Hello** _world_"
        expected_output = "<p><b>Hello</b> <i>world</i></p>"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with open(self.input_file, 'w', encoding='utf-8') as f:
                f.write(markdown_text)
            convert_markdown_to_html(self.input_file)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_conversion_html_format(self):
        markdown_text = "**Hello** _world_"
        expected_output = "<p><b>Hello</b> <i>world</i></p>"
        
        convert_markdown_to_html(self.input_file, self.output_file, output_format="html")
        with open(self.output_file, 'r', encoding='utf-8') as f:
            output = f.read().strip()
            self.assertEqual(output, expected_output)

    def test_conversion_ansi_format(self):
        markdown_text = "**Hello** _world_"
        expected_output = "\033[7m<b>Hello</b> <i>world</i>\033[0m"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with open(self.input_file, 'w', encoding='utf-8') as f:
                f.write(markdown_text)
            convert_markdown_to_html(self.input_file, output_format="ansi")
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
