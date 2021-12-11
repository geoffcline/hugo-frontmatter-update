import copy
from yaml import load, dump
from io import StringIO

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# help
def get_frontmatter(file):
    result = """title: "Documentation"
linkTitle: "Docs"
weight: 20
menu:
  main:
    weight: 20
    pre: <i class='fas fa-book'></i>"""
    return result


def parse_yaml(raw):
    return load(raw, Loader=Loader)


def dump_yaml(body):
    r = str(body)
    return r


def remove_nav(body):
    body.pop('menu', None)
    return body


def add_cascade(body):
    r = copy.copy(body)
    r['cascade'] = dict()
    r['cascade']['type'] = "docs"
    return r


# help
def remove_frontmatter(file):
    stream = ""
    inside_yaml = False
    lines = file.readlines()
    for line in lines:
        if line != "---\n" and not inside_yaml:
            stream = stream + line
        elif line != "---\n" and inside_yaml:
            pass
        elif line == "---\n" and inside_yaml:
            inside_yaml = False
        elif line == "---\n" and not inside_yaml:
            inside_yaml = True

    file.truncate(0)
    file.write(stream)

    return file


def insert_frontmatter(file, raw):
    content = file.read()
    file.seek(0)
    file.write("\n---\n")
    file.write(raw)
    file.write("\n---\n")
    file.write(content)
    return file


def driver():
    result = dump_yaml(add_cascade(remove_nav(parse_yaml(get_frontmatter(None)))))
    print(result)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
