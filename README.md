# Demo Python Package

A Python package to demonstrate how to publish a package on GitHub and PyPI.

The package itself is just a very simple function that produces a classic magic 8-ball response.

## Pip Installation

GitHub doesn't have a package registry for Python. What you can do instead is to create a repository and use it as the source for your package. This way, you can allow others to install it using pip.

```bash
# with just pip:
pip install git+https://github.com/USERNAME/demo-python-package.git

# same thing with UV:
uv pip install git+https://github.com/USERNAME/demo-python-package.git
```

## PyPI Installation

To publish your package on PyPI, you can follow these steps:

> Read the official guide on [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) for more details.

But essentially it boils down to building the package, uploding to PyPI, and then installing it from there:

## The Docker Approach

Finally, most developers just end up pushing their bundled code to a registry. To do that here on GitHub, you can generate a personal access token and use it to authenticate with the GitHub Container Registry.:

```bash
# log in to GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin

# build and tag the Docker image
docker build -t ghcr.io/m-spangenberg/demo-python-package:latest .

# push the Docker image to GitHub Container Registry
docker push ghcr.io/m-spangenberg/demo-python-package:latest
```

This can be automated by turning it into a GitHub Action workflow in `.github/workflows/publish.yml`

## Running the Function

Docker will automatically run the function when you start the container, but locally you use the following command:

```python
# run the function from the cli
python -m python_demo_package_9999.demo
# result: "Ask again later"
```
