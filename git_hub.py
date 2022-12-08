from githubLibrary import GithubLibrary
from argparse import ArgumentParser
from os import environ

parser = ArgumentParser(
    description='Script to maintain GitHub repositories',
    prog='git_hub'
)
tokenAvalible= None
if 'GITHUB_TOKEN' in environ:
    git = GithubLibrary(environ['GITHUB_TOKEN'])
    tokenAvalible = True
else:
    print("There is no environment Variable like 'GITHUB_TOKEN' please export this variable with value of your github token\n")
    print("Please generate Token here: https://github.com/settings/tokens\n")
    tokenAvalible = False

def main():
    parser.add_argument(
        '-r', 
        '--repo', 
        help="Repository name to be created"
    )
    parser.add_argument(
        '-b', 
        '--branch', 
        help="Branch name to be created"
    )
    parser.add_argument(
        '-t', 
        '--tag', 
        help="Tag name to current commit"
    )

    args = parser.parse_args()
    if args.repo != "":
        git.create_repo(args.repo)

    if args.branch != "":
        git.create_branch(args.branch,args.tag)

if __name__ == "__main__" and tokenAvalible:
    main()