import copy
import os
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def get_frontmatter(file):
    stream = ""
    inside_yaml = False
    first_yaml_finished = False
    lines = file.readlines()
    for line in lines:
        if line != "---\n" and not inside_yaml:
            pass
        elif line != "---\n" and inside_yaml:
            stream = stream + line
        elif line == "---\n" and inside_yaml:
            inside_yaml = False
            first_yaml_finished = True
        elif line == "---\n" and not first_yaml_finished and not inside_yaml:
            inside_yaml = True

    return stream


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
    file.seek(0)
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
    file.seek(0)
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
    os.system("cp -r content/ content-working/")

    base_path = "content-working/en/docs/"
    docs_index_path = base_path + "_index.md"
    getting_started_path = base_path + "getting-started/_index.md"

    with open(docs_index_path, "r+") as file:
        r = get_frontmatter(file)
        r = parse_yaml(r)
        r = remove_nav(r)
        r = add_cascade(r)
        r = dump(r)  # huh
        remove_frontmatter(file)
        insert_frontmatter(file, r)

    with open(getting_started_path, "r+") as file:
        r = get_frontmatter(file)
        r = parse_yaml(r)
        r = remove_nav(r)
        r = dump(r)  # huh
        remove_frontmatter(file)
        insert_frontmatter(file, r)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
