# Installation

The fastest way of installing this package is through PyPI:

```shell
python3 -m pip install git+https://github.com/RUB-EP1/pawian-tools@main
```

This installs the latest version that you can find on the
[`main`](https://github.com/RUB-EP1/pawian-tools/tree/main) branch.

However, we highly recommend using the more dynamic,
{ref}`'editable installation' <compwa:develop:Editable installation>` instead. This
goes as follows:

1. Get the source code (see [the Pro Git Book](https://git-scm.com/book/en/v2)):

   ```shell
   git clone https://github.com/RUB-EP1/pawian-tools
   cd pawian-tools
   ```

2. **[Recommended]** Create a virtual environment (see
   {ref}`here <compwa:develop:Virtual environment>` or the tip below).

3. Install the project in
   {ref}`'editable installation' <compwa:develop:Editable installation>` with
   {ref}`additional dependencies <compwa:develop:Optional dependencies>` for the
   developer:

   ```shell
   python3 -m pip install -e .[dev]
   ```

That's all! Have a look at the {doc}`/usage` page to try out the package, and see
{doc}`compwa:develop` for tips on how to work with this 'editable' developer setup!

:::{tip}

It's easiest to install the project in a
[Conda](https://docs.conda.io/en/latest/miniconda.html) environment. In that case, to
install in editable mode, just run:

```shell
conda env create
conda activate pawian-tools
```

This way of installing is also safer, because it
{ref}`pins all dependencies <compwa:develop:Pinning dependency versions>`. Note you
can also pin dependencies with `pip`, by running:

```shell
python3 -m pip install -e .[dev] -c .constraints/py3.x.txt
```

where you should replace the `3.x` with the version of Python you want to use.

:::
