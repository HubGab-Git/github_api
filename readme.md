# PyGithub Script

## Description

This is example script using PyGithub library for create repository, create feature branch and add tag to commit

## Usage

First you have to generate GitHub Token here: https://github.com/settings/tokens

Export your token in your machine:

```md
export GITHUB_TOKEN=<YOUR GITHUB TOKEN>
```

you can check Script help typing "-h" on the end of command:

```md
python3 git_hub.py -h
```

example use:

```md
python3 git_hub.py -r test2 -b new_branch -t 2.0.0
```