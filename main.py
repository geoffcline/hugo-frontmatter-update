from yaml import load, dump

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
    return dump(body)


def remove_nav(body):
    body.pop('menu', None)
    return body


def add_cascade(body):
    body['cascade'] = dict()
    body['cascade']['type'] = "docs"
    return body


# help
def remove_frontmatter(file):
    content = file.read()
    file.seek(0)
    file.write(content)
    return file


def insert_frontmatter(file, raw):
    content = file.read()
    file.seek(0)
    file.write(raw + content)
    return file


def driver():
    result = dump_yaml(add_cascade(remove_nav(parse_yaml(get_frontmatter(None)))))
    print(result)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
