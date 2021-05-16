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
- [nginx](https://www.nginx.com/)
- [gunicorn](https://gunicorn.org/)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [flake8](http://flake8.pycqa.org/en/latest/)

## Usage

### Quick start

```bash
git clone git@github.com:vyahello/fast-weather-api.git
cd fast-weather-api
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m weather
```

The please open a home page in your browser - [0.0.0.0:4444](http://0.0.0.0:4444)

**[⬆ back to top](#fast-weather-rest-api)**

## Development notes

### API endpoints

Please refer to the full documentation tree via [0.0.0.0:4444/docs](http://0.0.0.0:4444/docs)

- GET **/api/weather/{city}**:
  ```bash
  curl 'http://0.0.0.0:4444/api/weather/lviv?country=UA'  
  ```
  _Response_: JSON
  ```json
  {
    "temp":10.78,
    "feels_like":9.43,
    "temp_min":10.56,
    "temp_max":11,
    "pressure":1021,
    "humidity":58
  }
  ```

- GET **/api/reports**:
  ```bash
  curl http://0.0.0.0:4444/api/reports
  ```
  _Response_: JSON
  ```json
  [
    {
      "description":"Clouds over downtown.",
      "location":{"city":"Lviv","country":"UA"},
      "id_":"1bf17ed8-e0cb-4087-824b-ddfec0fb61ea",
      "created_date":"2021-05-09T22:39:49.712594"},
    {
      "description":"Misty sunrise today, beautiful!",
      "location":{"city":"Kyiv","country":"UA"},
      "id_":"03cfa435-0b4d-4824-81ea-2a314d6d9196",
      "created_date":"2021-05-09T22:39:49.711899"}
  ]
  ```
- POST **/api/report**:
  ```bash
  curl -X POST http://0.0.0.0:4444/api/reports \
        --header "Content-Type: application/json"  \
        --data '{"description":"Frost on the roads", "location":{"city": "Portland", "country": "US"}}'
  ```
  _Response_: JSON
  ```json
  {
    "description":"Frost on the roads",
    "location":{"city":"Kyiv","country":"UA"},
    "id_":"c1ce55ec-e7ea-49ef-9f35-62e176bae83d",
    "created_date":"2021-05-09T22:51:57.822789"
  }
  ```

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
