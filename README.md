# Example package

This package demonstrates a packaging workflow

- circular dependency: `bar` from [`scm-dep`](../../../scm-dep)
- regular dependency: `baz` from [`scm-base`](../../../scm-base)


## Development workflow

1. create environment
   ```shell
   python -m venv --prompt scm venv
   source venv/bin/activate
   ```

2. install dependencies (packages & from source)
   ```shell
   pip install -U pip
   pip install -r requirements.txt
   ```

3. run tests
   ```shell
   pytest
   ```

## Building wheels

1. The build environment technically doesn't need anything except
   `build`, so you could reuse the environment above or create a fresh
   one with only `build` installed.
   
   ```shell
   python -m venv --prompt build buildenv
   source buildenv/bin/activate
   pip install -U pip build
   ```

2. Build with:
   ```shell
   python -m build
   ```
