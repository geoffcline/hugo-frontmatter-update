import unittest
import os
from main import *
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class TestStringMethods(unittest.TestCase):
    yamlstring = """title: "Documentation"
linkTitle: "Docs"
weight: 20
menu:
  main:
    weight: 20
    pre: <i class='fas fa-book'></i>"""

    parsedyaml = {
            'title': 'Documentation',
            'linkTitle': 'Docs',
            'weight': 20,
            'menu': {
                'main': {
                    'weight': 20,
                    'pre': "<i class='fas fa-book'></i>"
                }
            }
        }

    def test_get_frontmatter(self):
        i_filename = "test-files/1-input.md"
        v = self.yamlstring
        with open(i_filename) as file:
            r = get_frontmatter(file)
        self.assertEqual(v, r)
        return

    def test_parse_yaml(self):
        v = self.parsedyaml
        i = self.yamlstring
        r = parse_yaml(i)
        self.assertEqual(v, r)
        return

    def test_dump_yaml(self):
        i = self.parsedyaml
        v = self.yamlstring
        r = dump_yaml(v)
        self.assertEqual(v, r)
        return

    def test_remove_nav(self):
        v = {
            'title': 'Documentation',
            'linkTitle': 'Docs',
            'weight': 20,
        }
        i = self.parsedyaml
        r = remove_nav(i)
        v = dump(v)
        r = dump(r)

        self.assertEqual(v, r)
        return

    def test_add_cascade(self):
        v = {
            'title': 'Documentation',
            'linkTitle': 'Docs',
            'weight': 20,
            'menu': {
                'main': {
                    'weight': 20,
                    'pre': "<i class='fas fa-book'></i>"
                }
            },
            'cascade': {
                'type': 'docs'
            }
        }
        i = self.parsedyaml

        r = add_cascade(i)
        self.assertEqual(v, r)
        return

    def test_remove_frontmatter(self):
        i_filename = "test-files/1-input.md"
        o_filename = "test-files/1-output.md"
        os.system("cp {} {}".format(i_filename, o_filename))
        v_filename = "test-files/1-target.md"

        try:
            with open(i_filename, "r+") as file:
                remove_frontmatter(file)

            with open(i_filename, "r") as file:
                r = file.read()

            with open(v_filename, "r") as file:
                v = file.read()

            self.assertEqual(v, r)
        finally:
            os.system("rm {}".format(o_filename))


        return

    def test_insert_frontmatter(self):
        i_filename = "test-files/2-input.md"
        o_filename = "test-files/2-output.md"
        os.system("cp {} {}".format(i_filename, o_filename))
        v_filename = "test-files/2-target.md"
        i = self.yamlstring

        try:
            with open(o_filename, "r+") as file:
                insert_frontmatter(file, i)

            with open(o_filename, "r") as file:
                r = file.read()

            with open(v_filename, "r") as file:
                v = file.read()

            self.assertEqual(v, r)
        finally:
            os.system("rm {}".format(o_filename))

        return


if __name__ == '__main__':
    unittest.main()
