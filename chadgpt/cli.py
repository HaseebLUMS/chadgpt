#!/usr/bin/env python3
import os
import subprocess
from typing import Optional
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key from .env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Rich console
console = Console()

def get_command_from_natural_language(user_input: str) -> Optional[str]:
    """Convert natural language to terminal command using OpenAI API."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a terminal command expert. Convert natural language requests into appropriate terminal commands. Only respond with the command, nothing else."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        console.print(f"[red]Error getting command: {str(e)}[/red]")
        return None

def execute_command(command: str) -> None:
    """Execute the terminal command and display the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout:
                console.print(Panel(result.stdout, title="Command Output", border_style="green"))
            else:
                console.print("[yellow]Command executed successfully but produced no output.[/yellow]")
        else:
            console.print(f"[red]Error executing command: {result.stderr}[/red]")
    except Exception as e:
        console.print(f"[red]Error executing command: {str(e)}[/red]")

def main():
    """Main entry point for the CLI."""
    console.print(Panel.fit(
        "[bold blue]Welcome to ChadGPT Terminal![/bold blue]\n"
        "Type your request in natural language and I'll convert it to a terminal command.\n"
        "Type 'exit' to quit.",
        title="ChadGPT Terminal",
        border_style="blue"
    ))

    while True:
        user_input = Prompt.ask("\n[bold]What would you like to do?[/bold]")
        
        if user_input.lower() in ['exit', 'quit']:
            console.print("[yellow]Goodbye![/yellow]")
            break

        command = get_command_from_natural_language(user_input)
        if command:
            console.print(f"[green]Executing command:[/green] {command}")
            execute_command(command)

if __name__ == "__main__":
    main() 