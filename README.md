![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/fast-weather-api.svg?branch=master)](https://travis-ci.org/vyahello/fast-weather-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/fast-weather-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/fast-weather-api?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Fast weather REST API

> A simple tool that represents weather REST API based on **FAST API** async python web framework.

## Tools

### Production
- 3.7, 3.8, 3.9
- asyncIO
- [fastapi](https://fastapi.tiangolo.com/)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [flake8](http://flake8.pycqa.org/en/latest/)

## Usage

### Quick start

```bash
git clone git@github.com/vyahello/fast-weather-api.git
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m weather
```

**[⬆ back to top](#fast-weather-rest-api)**

## Development notes

### API endpoints

TBD

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `flake8`, `mypy`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

> Please move analyse-source-code.sh script into .git/hooks/pre-commit file to be able to check your code on every next commit.
```bash
mv analyse-source-code.sh .git/hooks/pre-commit
```

### Meta

Author – _Vladimir Yahello_.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/Vladimir Yahello](http://linkedin.com/in/volodymyr-yahello)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/fast-weather-api/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#fast-weather-rest-api)**
