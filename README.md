# Example package

This package demonstrates a packaging workflow

- source dependencies: `bar` from [`scm-dep`](../scm-dep)


## Development workflow

1. create environment

   ```shell
   python -m venv --prompt scm venv
   source venv/bin/activate
   ```

2. install build dependencies & package

   ```shell
   pip install -U pip
   pip install -r requirements.txt
   pip install -e .
   ```

3. run tests
   ```shell
   pytest
   ```
