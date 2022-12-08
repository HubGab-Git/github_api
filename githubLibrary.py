from github import Github,GithubException


class GithubLibrary:
    user = None
    repoName = None
    def __init__(self, token):
        self.user = Github(token).get_user()

    def create_repo(self,repoName):
        try:
            self.user.create_repo(
            name=repoName,
            private=False,
            )
        except GithubException as err:
            print(err.data['message'])
            for error in err.data['errors']:
                print(error['message'])
            print(f"Repository '{repoName}' alredy exists no need to create, skiping...")
        else:
            print(f"Repository '{repoName}' was created")
        self.repoName = repoName
    
    def create_branch(self,branchName,tag):
        repo = self.user.get_repo(self.repoName)
        file_name       = 'test.txt'
        file_content    = 'Hello World'

        # Create file
        try:
            repo.create_file(file_name, 'commit', file_content)
        except:
            file = repo.get_contents(file_name)
            repo.update_file(file_name, "first_commit", "Hello World+", file.sha)
        finally:
            print(f"Commit complete!")

        target_branch = branchName
        sb = repo.get_branch(repo.default_branch)
        if tag != '':
            try:
                repo.create_git_ref('refs/tags/' + tag, sha=sb.commit.sha)
                print(f"Tag: '{tag}' issued")
            except:
                print(f"Already there is tag: '{tag}' in latest commit, so this action will be ommited")
    
        try:
            repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)
            print(f"Created branch {target_branch}")
        except:
            print(f"Already there is branch: '{branchName}' with this commit, so this action will be ommited")