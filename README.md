# Azure AI-102 Repo

This repository will contain practice code in C# and Python for the purpose of passing Azure AI-102 exam. 
The code is a sample only and is not intended to be a full fledge application.

[Azure AI API Documentation](https://eastus.dev.cognitive.microsoft.com/)

## Development tools
- Visual Studio Code
- .NET 8 framework
- Python 3.x
- Git

## Development environment

### Environment variables
For .NET applicaitons, environment variables are stored in `appsettings.json` file where as for the python version they are installed in `.env` file.
Aternatives, environment variables can be installed in the current console session or in the `~/.bashrc` or `~/.zshrc` files.
- For linux/macos use the command `export`
    example: `export API_KEY=your-api-key`
- For Windows use the command `setx`
    example: `export API_KEY=your-api-key`
    
## Installation

Python packages:
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
