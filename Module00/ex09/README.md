# ft_package

**ft_package** is a small sample package created for the Python Piscine for Data Science. It provides a single helper function, **count_in_list**, which counts how many times a given value appears in a list.

## Commands

- ### Build
  ```python3 -m build  ```

- ### Display the package list
  ```pip list```

- ### Installation
  ```pip install ./dist/ft_package-0.0.1.tar.gz```
or
  ```pip install ./dist/ft_package-0.0.1-py3-none-any.whl```

- ### Display the package's characteristics
  ```pip show -v ft_package```

### Test
To test the package, go out side of the project directory where you installed the package, and run this:

``` python3 -c "from ft_package import count_in_list; print(count_in_list(['toto','tata','toto'],'toto'))"```

This should return 2

## Files
- **`ft_package/`** — The package folder itself. Its name is the import name, so
  `from ft_package import ...` refers to this directory.

- **`ft_package/__init__.py`** — Marks the folder as an importable package and
  runs when the package is imported. It re-exports `count_in_list` so it can be
  imported directly with `from ft_package import count_in_list` instead of the
  longer `from ft_package.count_in_list import count_in_list`.

- **`ft_package/count_in_list.py`** — The module holding the actual code: the
  `count_in_list` function that counts how many times a value appears in a list.

- **`setup.py`** — The build script. When the build tool runs it, the `setup()`
  call registers the package metadata (name, version, author, license, URL) and
  `find_packages()` locates the code to include.

- **`config.toml`** — Declares which build system to use (setuptools) so the
  package can be built with `python -m build`.

- **`README.md`** — This file: describes the package and how to use it.

- **`LICENSE`** — The MIT license text covering the package.

## Function

### `count_in_list(lst, target)`

Returns the number of times `target` appears in `lst`.

- `lst`: the list to search through.
- `target`: the value to count.
- **Returns:** an integer count (0 if the value is not present).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.