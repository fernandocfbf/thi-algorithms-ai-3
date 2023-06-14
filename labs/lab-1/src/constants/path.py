import git
repository = git.Repo('.', search_parent_directories=True)
ROOT_PATH = repository.working_tree_dir.replace("\\",'/')
LAB_1_ROOT = ROOT_PATH + '/lab-1'