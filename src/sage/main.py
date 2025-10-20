from .core.llm_provider import LLMProvider

def main():
    print("Welcome to SAGE!")
    print("Testing LLM Provider...")

    # Instantiate the provider with the command for the Gemini CLI
    gemini_provider = LLMProvider(provider_cli_command="gemini")

    # Ask a simple question
    prompt = "What is the speed of light?"
    print(f"Asking: {prompt}")
    response = gemini_provider.ask(prompt)

    # Print the response
    print("\nResponse from Gemini:")
    print(response)

if __name__ == "__main__":
    main()
