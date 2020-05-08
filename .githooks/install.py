# Standard Library
import os
from glob import glob

# Third party
import fire

githooks_dir = os.path.dirname(os.path.realpath(__file__))


def install_hooks(force=False):
    """
    symlink every file from .githooks to .git/hooks and make them executable

    Args:
        force (bool): force the symlink to overwrite existing files in .git/hooks
    """
    ln_args = "--symbolic"
    if force:
        ln_args += " --force"

    for filepath in glob(f"{githooks_dir}/*"):
        if filepath.endswith("install.py"):
            continue

        filename = os.path.basename(filepath)
        new_path = os.path.join(githooks_dir, "..", ".git", "hooks", filename)
        os.system(f"ln {ln_args} {filepath} {new_path}")
        os.system(f"sudo chmod +x {new_path}")


if __name__ == "__main__":
    fire.Fire(install_hooks)
