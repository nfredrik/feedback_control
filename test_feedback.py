import unittest
import pep8


class Pep8ConformanceTestCase(unittest.TestCase):
    """Test that all code conforms to PEP8!"""

    def test_pep8_conformance(self):
        self.pep8style = pep8.StyleGuide(show_source=True)
        files = (['first_example.py'])
        self.pep8style.check_files(files)
        self.assertEqual(self.pep8style.options.report.total_errors, 0)


if __name__ == "__main__":
	unittest.main()
