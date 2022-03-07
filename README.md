# cookiecutter-rust

[![Build Status](https://travis-ci.org/rnag/cookiecutter-rust.svg?branch=master)](https://travis-ci.org/rnag/cookiecutter-rust)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Rust is a framework for jumpstarting production-ready rust projects quickly.

## Features

- TODO

## Optional Integrations

- Option of GitHub Actions or None

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
project_name [myrustproject]: echoserver
full_name [Ritvik Nag]: Ritvik Nag
email [rv.kvetch@gmail.com]: rv.kvetch@gmail.com
git_root [github.com]: github.com
github_username [rnag]: rnag
project_short_description [A Rust project.]: Rusty Echo Server
use_git [y]: y
Select use_ci:
1 - github
2 - none
Choose from 1, 2 [1]: 1
```

Enter the project and take a look around:
```console
$ cd echoserver/
$ ls
```

Run `make help` to see the available management commands, or just run `make build` to build your project.
```console
$ make help
$ make build
$ ./bin/echoserver
```
