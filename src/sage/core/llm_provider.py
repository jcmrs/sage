import asyncio

class LLMProvider:
    def __init__(self, provider_cli_command):
        self.provider_cli_command = provider_cli_command

    async def ask(self, prompt):
        # Create the shell command
        cmd = f'{self.provider_cli_command} "{prompt}"'
        
        # Create the subprocess
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        # Wait for the process to finish and get the output
        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            return stdout.decode().strip()
        else:
            return f"An error occurred: {stderr.decode()}"
