import subprocess

class GitManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_status(self):
        try:
            result = subprocess.run(
                'git status',
                shell=True,
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repo_path
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr}"
