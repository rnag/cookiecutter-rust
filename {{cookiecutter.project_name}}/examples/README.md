# Examples

This folder contains example scripts that can be used to interact with
the `{{cookiecutter.project_name}}` crate.

## Quickstart

First, start out by cloning the GitHub project:

```shell
❯❯ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
```

Then, simply `cd` into the project folder:

```shell
❯❯ cd {{cookiecutter.project_name}}
```

From here, you can use `cargo` to build and run
any of the examples individually.

In particular, here's a sample usage of running `examples/my_example.rs`:

```shell
❯❯ cargo run --example my_example
```
