# cookiecutter-rust

[![Build Status](https://travis-ci.org/rnag/cookiecutter-rust.svg?branch=master)](https://travis-ci.org/rnag/cookiecutter-rust)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Rust is a framework for jumpstarting production-ready rust projects quickly.

## Features

- Choice of setting up a *library* or *service* (binary with a `src/main.rs`)
- Generation of `examples/` and `tests/` folders

## Optional Integrations

- Option of [GitHub Actions] or None

[GitHub Actions]: https://github.com/features/actions

## Usage

Let's pretend you want to create a project called "echoserver". Rather than starting from scratch maybe copying 
some files and then editing the results to include your name, email, and various configuration issues that always 
get forgotten until the worst possible moment, get cookiecutter to do all the work.

First, get Cookiecutter. Trust me, it's awesome:
```console
$ pip install cookiecutter
```

alternatively you can install `cookiecutter` with homebrew:
```console
$ brew install cookiecutter
```

finally to run it based on this template just:
```console
$ cookiecutter https://github.com/rnag/cookiecutter-rust.git
```

You will be asked about your basic info (name, project name, app name, etc.). This info will be used to customize your new project.

Warning: After this point, change 'Ritvik Nag', 'rnag', etc to your own information.

Answer the prompts with your own desired [options](). For example:
```console
full_name [Ritvik Nag]: Jon Smitty
email [rv.kvetch@gmail.com]: me@my-email.com
github_username [rnag]: jschmidt
project_name [my-rust-project]: echoserver
project_short_description [A Rust project.]: Rusty Echo Server
Select project_type:
1 - library
2 - service
Choose from 1, 2 [1]:
version [0.1.0]:
Select use_ci:
1 - gh-actions
2 - None
Choose from 1, 2 [1]:
create_author_file [y]: n
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

Enter the project and take a look around:
```console
$ cd echoserver/
$ ls
```

Run `cargo test` to run unit tests, or just run `cargo build` to build your project.
```console
$ cargo test
$ cargo build --release
$ ./target/release/echoserver
```
