from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Custom tool for creating a file with given content.
class FileCreationTool:
    name = "FileCreationTool"
    description = "Creates a file with the specified name and content."

    def run(self, file_name: str, content: str) -> str:
        try:
            with open(file_name, "w") as f:
                f.write(content)
            return f"File '{file_name}' created successfully."
        except Exception as e:
            return f"Error creating file: {e}"


# Initialize the agent with the FileCreationTool.
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[FileCreationTool()],
    markdown=True,
)

# Define a prompt that instructs the agent to generate a Python script for generating prime numbers using the Sieve of Eratosthenes.
prompt = (
    "Generate a Python script that implements the Sieve of Eratosthenes. "
    "The script should define a function that takes an integer 'n' and returns "
    "a list of all prime numbers up to 'n'. It should also include a main block "
    "that demonstrates this functionality. Also save file as prime_generator.py"
)

# Ask the agent's language model to generate the code.
# (Depending on your Agno setup, you may capture the output using a method like `agent.model.chat`.)
agent.print_response(prompt)

# Use the FileCreationTool to automatically create the Python script file.
# result = agent.tools[0].run("prime_generator.py", generated_code)
# print(result)
