# iccsh

`iccsh` for **Information Codes and Ciphers Shell**. Yes I know, what an ugly name. I don't even know how to pronounce it. Let's just say it's "itch".

`iccsh`is a shell to run common algorithms for:

* error detecting and correcting codes
* compression codes
* information theory
* algebra number theory
* algebraic coding
* cryptography

## Requirements

* Python3 (specifically Python 3.8)
* [`pipenv`](https://pypi.org/project/pipenv/)

## Local Development Setup

1. Clone the repository
2. Install dependencies

    ``` sh
    pipenv install --dev
    ```

To actually run the shell:

``` sh
pipenv run python run.py
```

Running tests:

``` sh
pipenv run pytest
```

## Documentation

See [wiki](https://github.com/hillaryychan/iccsh/wiki).
