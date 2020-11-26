# python-exercises

Created by: [Aaron Imbrock](https://www.linkedin.com/in/aaron-imbrock/)

## Description

**Python refresher** Various excercises and code styles implemented in Python3 and Django.

## Installation

If you need help installing Python, visit https://installpython3.com/.

Install Pipenv:
* Debian: `sudo apt install python3-pip python3-setuptools && python3 -m pip install --user pipenv` [Full Steps Here](https://phoikoi.io/2018/04/03/bootstrap-pipenv-debian.html)
* Mac: `brew install pipenv`
* Fedora: `sudo dnf install pipenv`
* Windows: `python -m pip install pipenv` [Full Steps Here](https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows)

Clone this repo:
```console
git clone git@github.com:aaron-imbrock/python-exercises.git
```
Create project virtualenv and install module requirements:
```console
cd python-exercises
pipenv install --dev
pipenv lock --pre
pipenv shell
```
## Usage

Each program can be found in `src`. To run:
```console
python ./src/snakes-cafe.py
```

## Authors

* Aaron Imbrock - https://github.com/aaron-imbrock/

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
