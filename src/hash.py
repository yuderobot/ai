import git

def get_hash():
    try:
        repo = git.Repo(search_parent_directories=True)
        git_hash = repo.git.rev_parse(repo.head.object.hexsha, short=6)
    except:
        git_hash = "N/A"

    if git_hash is None:
        git_hash = "N/A"

    return git_hash
