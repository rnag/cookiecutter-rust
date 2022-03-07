# Examples

This folder contains example scripts that can be used to interact with
the `{{cookiecutter.project_name}}` crate.

## Quickstart

First, start out by cloning the GitHub project:

```shell
❯❯ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
```

When running the examples, we'll often want to see the DEBUG logs from the library under test,
`{{cookiecutter.project_name}}` in this case. Therefore, remember to ensure that the **RUST_LOG** env variable
is properly set.

For example, on *Mac/Linux*:

```shell
❯❯ export RUST_LOG='{{ cookiecutter.project_name.replace('-', '_') }}=TRACE'
```

On *Windows*:

```shell
❯❯ $env:RUST_LOG='{{ cookiecutter.project_name.replace('-', '_') }}=TRACE'
```

Next, simply just `cd` into the project folder:

```shell
❯❯ cd {{cookiecutter.project_name}}
```

From here, you can use `cargo` to build and run
any of the examples individually.

In particular, here's a sample usage of running `examples/my_example.rs`:

```shell
❯❯ cargo run --example my_example
```
