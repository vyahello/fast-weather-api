#!/usr/bin/env bash

# specifies a set of variables to declare files to be used for code assessment
PACKAGE="weather"

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"


pretty-printer-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    echo "Start ${1} analysis ..."
}


remove-pycache() {
:<<DOC
    Removes python cache directories
DOC
    ( find . -depth -name __pycache__ | xargs rm -r )
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    pretty-printer-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
:<<DOC
    Runs "flake8" code analysers
DOC
    pretty-printer-box "flake" && ( flake8 ./ )
}

check-mypy() {
:<<DOC
    Runs "mypy" code analyser
DOC
    pretty-printer-box "mypy" && ( mypy --package "${PACKAGE}" )
}


check-unittests() {
:<<DOC
    Runs unittests using "pytest" framework
DOC
    pretty-printer-box "unitests" && pytest
}


main() {
:<<DOC
    Runs "main" code analyser
DOC
    (
      remove-pycache
      check-black && \
      check-mypy && \
      check-flake && \
      check-unittests
    )
    echo -e "${PASSED_OUT}Congratulations, code assessment is passed!${NONE_OUT}"
}

main