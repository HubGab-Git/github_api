from lib.githubLibrary import GithubLibrary
from argparse import ArgumentParser
from os import environ
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w')

logging.debug("initialization Argument Parser: START")
parser = ArgumentParser(
    description='Script to maintain GitHub repositories',
    prog='git_hub'
)
logging.debug("initialization Argument Parse: DONE")
logging.debug("set variable 'tokenAvalible' to none")
tokenAvalible= None
logging.info("check if envronment variable 'GITHUB_TOKEN' is set: START")
if 'GITHUB_TOKEN' in environ:
    logging.info("envronment variable 'GITHUB_TOKEN' is set: SUCCSESS!")
    logging.debug("initialization object GithubLiblary: START")
    git = GithubLibrary(environ['GITHUB_TOKEN'])
    logging.debug("initialization object GithubLiblary: DONE")
    logging.debug("set variable 'tokenAvalible' to True")
    tokenAvalible = True
else:
    logging.error("envronment variable 'GITHUB_TOKEN' is not set: Error!")
    print("There is no environment Variable like 'GITHUB_TOKEN' please export this variable with value of your github token\n")
    print("Please generate Token here: https://github.com/settings/tokens\n")
    logging.debug("set variable 'tokenAvalible' to False")
    tokenAvalible = False

logging.debug("start main function of aplication: START")
def main():
    logging.debug("add parsing argument 'repo'")
    parser.add_argument(
        '-r', 
        '--repo', 
        help="Repository name to be created"
    )
    logging.debug("add parsing argument 'branch'")
    parser.add_argument(
        '-b', 
        '--branch', 
        help="Branch name to be created"
    )
    logging.debug("add parsing argument 'tag'")
    parser.add_argument(
        '-t', 
        '--tag', 
        help="Tag name to current commit"
    )
    logging.debug("parsing arguments")
    args = parser.parse_args()
    logging.debug("check if repo argument is provided")
    if args.repo != "":
        logging.debug("repo argument provided creating repository: START")
        git.create_repo(args.repo)
        logging.debug("repo argument provided creating repository: DONE")

    logging.debug("check if branch argument is provided")
    if args.branch != "":
        logging.debug("branch argument provided creating branch: START")
        git.create_branch(args.branch,args.tag)
        logging.debug("branch argument provided creating branch: DONE")
    logging.debug("end of main function of aplication: DONE")

logging.debug("Start main aplication")
if __name__ == "__main__" and tokenAvalible:
    main()