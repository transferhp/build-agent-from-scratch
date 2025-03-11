# Building Agent without Frameworks (e.g. LangChain, CrewAI)

The limitions of using exsiting frameworks (LangChain, CrewAI) to build an agent:

* They introduce an **extra layer of abstraction**, hiding crucial details from the developer.
* They make you **dependent on their ecosystem**, **updates**, and **potential limitations**.
* They **limit flexibility**, forcing you to work within their predefined structures rather than tailoring solutions to your exact needs.

The repo contains examples of building effective agents with *ONLY* LLM API and Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

To install and run this application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/transferhp/build-agent-from-scratch.git
   ```

2. Navigate to the project directory:
```bash
cd build-agent-from-scratch
```

3. Create the virtual environment for the project and install the required Python packages via [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

## Usage

Example to run the agent work powered by Bedrock Claude model
```bash
uv run code/agent_bedrock_anthropic.py
```