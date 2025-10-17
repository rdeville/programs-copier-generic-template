# Taken from https://github.com/copier-org/copier-template-extensions?tab=readme-ov-file#usage
import requests

from jinja2.ext import Extension


# taken from Django
# https://github.com/django/django/blob/main/django/utils/text.py
def gitignore(value):
    """
    Create a the content of .gitignore based on the following community manage
    repo https://github.com/github/gitignore
    """
    base_url = "https://raw.githubusercontent.com/github/gitignore/refs/heads/main/"
    content = """\
## BEGIN
## Below are generated content from repo github.com/github/gitignore
## Please add your project specific ignored files above or below
## generated content
"""
    for tpl in value:
        with requests.get(f"{base_url}{tpl}.gitignore") as req:
            req.raise_for_status()
            content += req.text

    content += "## END"
    return content


class GitignoreExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["gitignore"] = gitignore
