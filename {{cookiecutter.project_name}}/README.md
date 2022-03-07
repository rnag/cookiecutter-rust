# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

[<img alt="github" src="https://img.shields.io/badge/github-{{cookiecutter.github_username}}/{{cookiecutter.project_name.replace('-', '--')}}-8da0cb?style=for-the-badge&labelColor=555555&logo=github" height="22">](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}})
[<img alt="crates.io" src="https://img.shields.io/crates/v/{{cookiecutter.project_name}}.svg?style=for-the-badge&color=fc8d62&logo=rust" height="22">](https://crates.io/crates/{{cookiecutter.project_name}})
[<img alt="docs.rs" src="https://img.shields.io/docsrs/{{cookiecutter.project_name}}/latest?style=for-the-badge&labelColor=555555&logoColor=white&logo=data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDUxMiA1MTIiPjxwYXRoIGZpbGw9IiNmNWY1ZjUiIGQ9Ik00ODguNiAyNTAuMkwzOTIgMjE0VjEwNS41YzAtMTUtOS4zLTI4LjQtMjMuNC0zMy43bC0xMDAtMzcuNWMtOC4xLTMuMS0xNy4xLTMuMS0yNS4zIDBsLTEwMCAzNy41Yy0xNC4xIDUuMy0yMy40IDE4LjctMjMuNCAzMy43VjIxNGwtOTYuNiAzNi4yQzkuMyAyNTUuNSAwIDI2OC45IDAgMjgzLjlWMzk0YzAgMTMuNiA3LjcgMjYuMSAxOS45IDMyLjJsMTAwIDUwYzEwLjEgNS4xIDIyLjEgNS4xIDMyLjIgMGwxMDMuOS01MiAxMDMuOSA1MmMxMC4xIDUuMSAyMi4xIDUuMSAzMi4yIDBsMTAwLTUwYzEyLjItNi4xIDE5LjktMTguNiAxOS45LTMyLjJWMjgzLjljMC0xNS05LjMtMjguNC0yMy40LTMzLjd6TTM1OCAyMTQuOGwtODUgMzEuOXYtNjguMmw4NS0zN3Y3My4zek0xNTQgMTA0LjFsMTAyLTM4LjIgMTAyIDM4LjJ2LjZsLTEwMiA0MS40LTEwMi00MS40di0uNnptODQgMjkxLjFsLTg1IDQyLjV2LTc5LjFsODUtMzguOHY3NS40em0wLTExMmwtMTAyIDQxLjQtMTAyLTQxLjR2LS42bDEwMi0zOC4yIDEwMiAzOC4ydi42em0yNDAgMTEybC04NSA0Mi41di03OS4xbDg1LTM4Ljh2NzUuNHptMC0xMTJsLTEwMiA0MS40LTEwMi00MS40di0uNmwxMDItMzguMiAxMDIgMzguMnYuNnoiPjwvcGF0aD48L3N2Zz4K" height="22">](https://docs.rs/{{cookiecutter.project_name}})
[<img alt="build status" src="https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/build/main?style=for-the-badge" height="22">](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions?query=branch%3Amain)

## Getting started

This project requires Go to be installed. On OS X with Homebrew you can just run `brew install rust`.

Running it then should be as simple as:

```console
$ cargo build
$ ./bin/{{cookiecutter.project_name}}
```

### Testing

``cargo test``

## Contributing

Contributions are welcome! Open a pull request to fix a bug, or [open an issue][]
to discuss a new feature or change.

Check out the [Contributing][] section in the docs for more info.

[Contributing]: CONTRIBUTING.md
[open an issue]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/issues

## License

This project is proudly licensed under the {{ cookiecutter.open_source_license }} ([LICENSE](LICENSE)
or http://opensource.org/licenses/MIT).

`{{cookiecutter.project_name}}` can be distributed according to the {{ cookiecutter.open_source_license }}. Contributions
will be accepted under the same license.

## Authors

* [{{cookiecutter.full_name}}](https://github.com/{{cookiecutter.github_username}})
