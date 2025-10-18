# 👋 Welcome to Copier Generic Template

<!-- markdownlint-disable MD033-->
<center>

[![Licenses: (MIT OR BEERWARE)][license_badge]][license_url]
[![Changelog][changelog_badge]][changelog_badge_url]

</center>
<!-- markdownlint-enable MD033-->

[license_badge]: https://img.shields.io/badge/Licenses-MIT%20OR%20BEERWARE-blue
[license_url]: https://framagit.org/rdeville-public/programs/copier-generic-template/copier-generic-template/blob/main/LICENSE
[changelog_badge]: https://img.shields.io/badge/Changelog-Python%20Semantic%20Release-yellow
[changelog_badge_url]: https://github.com/python-semantic-release/python-semantic-release

---

## ℹ️ Description

This repository store aims to store generic template to be used with
[copier][copier] to automate and maintain common files I use in almost every
repository such as:

- LICENSE
- CONTRIBUTING
- Basic .gitignore (generated from template in [github/gitignore][gitignore]
- Basic README
- Base of CI (mainly Gitlab CI, I'll probably add more later)
- [Pre-commit][pre-commit] configurations
- Etc.

[gitignore]: https://github.com/github/gitignore
[pre-commit]: https://pre-commit.com/

## 🚀 Usage

### ✅ Pre-requisite

Depending on the usage chosen below, you'll need more or less dependencies.
In any case, you'll need at least following dependencies to be installed:

- Python (>=3.13, may be working with version below, but not tested)
- Pip (>=25.2, may be working with version below, but not tested)

### Basic usage with copier

For this basic usage using directly [copier][copier], you'll need to install
[copier][copier] and some other jinja2 extension.

Cleaner way to do this, especially for temporary installation (for instance, one
shot of repository creation), is to setup a python virtual environment and setup
dependencies within this environment:

```bash
# Create python virtual environment
python3 -m venv /tmp/copier
# Activate the virtual environment
source /tmp/copier/bin/activate
# Install uv to ease installation of dependencies
pip install uv
# Install required dependencies
uv install tool \
    --with jinja2-time \
    --with copier-template-extensions \
    --with jinja2-jsonschema \
    --with requests \
    copier
# Run copier
copier copy \
    -a \
    --trust \
    .copier.yaml \
    git+https://framagit.org/rdeville-public/programs/copier-generic-template \
    ./
# Deactivate python virtual environment
deactivate
```

A shorter to do use is to use `uv` to directly run copier:

```bash
# Create python virtual environment
python3 -m venv /tmp/copier
# Activate the virtual environment
source /tmp/copier/bin/activate
# Install uv to ease installation of dependencies
pip install uv
# Install required dependencies
uv run tool \
    --with jinja2-time \
    --with copier-template-extensions \
    --with jinja2-jsonschema \
    --with requests \
    copier copy \
    -a \
    --trust \
    .copier.yaml \
    git+https://framagit.org/rdeville-public/programs/copier-generic-template \
    ./
# Deactivate python virtual environment
deactivate
```

### Automatic repository initialization

If you are lazy (like me), there is two scripts that allow fully automate the
repository:

- [scripts/copierRun][copierRun]: Automatic commit based on copier action (copy
  or update) following gitmoji semantic commit
- [scripts/gitInit][gitInit]: Fully automatique git repository initialization,
  i.e. git init with first empty commit and tag `v0.0.0`, branch creation,
  templating rendering then automatic commit using above script (i.e.
  `copierRun`)

To use the fully automatic git repository automation, first **TAKE THE TIME TO
LOOK AT ABOVE SCRIPTS** since the command use `curl | bash`.

Then, simply use the following command:

<!-- markdownlint-disable MD013-->
```bash
curl \
  https://framagit.org/rdeville-public/programs/copier-generic-template/-/raw/main/scripts/gitInit \
  | bash -
```
<!-- markdownlint-enable MD013-->

You will be asked if you read the content of those scripts before continuing,
since using `curl | bash` can lead do desastrous behaviour.

Imagine someone with bad intention gaining access and modifying those scripts to
put the following command in the script: `sudo rm -rf /`. This will end with the
wipeout of your system!

**SO, ALWAYS BE CAREFUL WHEN USING COMMAND OF THE FORM `curl | bash`**

[copierRun]: ./scripts/copierRun
[gitInit]: ./scripts/gitInit
[copier]: https://copier.readthedocs.io/

<!--
### Demo

In both case above, this will run copier. The execution of copier will prompt
you questions to set variables that will be using to render files.

See below an example of the behaviour of the fully automated git repository
initialization:
-->

## 📝 License

Copyright © 2025, Romain Deville <code@romaindeville.fr>

This project is under following licenses (**OR**) :

- [MIT][main_license]
- [BEERWARE][beerware_license]

[main_license]: https://framagit.org/rdeville-public/programs/copier-generic-template/copier-generic-template/blob/main/LICENSE
[beerware_license]: https://framagit.org/rdeville-public/programs/copier-generic-template/copier-generic-template/blob/main/LICENSE.BEERWARE
