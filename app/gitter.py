from app.config import Config
import shutil
from git import Repo

def clone_remote():
    print(Config.GIT_ROOT_PATH)
    shutil.rmtree(Config.GIT_ROOT_PATH)

    git_dir = Config.GIT_ROOT_PATH
    git_url = Config.GIT_URL
    git_branch = Config.GIT_BRANCH
    git_token = Config.GIT_TOKEN
    git_auth_url = Config.GIT_AUTH_URL

    git_url = git_url.replace("https://", "")
    git_url = git_url.replace("http://", "")
    git_auth_url = git_auth_url.replace("TOKEN", git_token)
    git_auth_url = git_auth_url.replace("URL", git_url)

    Repo.clone_from(git_auth_url, git_dir, branch=git_branch)

    return "jedi"

def commit_push(uuid):
    git_repo = Config.GIT_ROOT_PATH + "/.git"

    repo = Repo(git_repo)
    repo.git.add(uuid + "/")
    repo.index.commit(uuid)
    origin = repo.remote(name='origin')
    origin.push()

    return "jedi"
