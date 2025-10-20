import subprocess

class LLMProvider:
    def __init__(self, provider_cli_command):
        self.provider_cli_command = provider_cli_command

    def ask(self, prompt):
        try:
            # Execute the command and capture the output
            result = subprocess.run(
                f'{self.provider_cli_command} "{prompt}"',
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr}"
