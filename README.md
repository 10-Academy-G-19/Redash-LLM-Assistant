# Redash ChatGPT Plugin

## Introduction

The Redash ChatGPT Plugin is an integration designed to incorporate natural language conversation capabilities powered by ChatGPT into the Redash dashboard. This plugin enhances user experience by enabling interactive queries and data visualization directly within the chat interface.

## Features

### Conversational Queries
- Users can engage with Redash using natural language queries, making the process more intuitive and user-friendly.

### Interactive Responses
- ChatGPT generates human-like responses, providing informative and contextual feedback on user queries.

### Data Visualization
- The plugin facilitates visualization of query results within the chat interface, streamlining data exploration and analysis.

## Installation Guide

### Prerequisites

Before installation, ensure you have the following set up:

#### Local Development Setup
1. Install required packages:
    ```
    $ sudo apt -y install docker.io docker-buildx docker-compose-v2
    $ sudo apt -y install build-essential curl docker-compose pwgen python3-venv xvfb
    ```

2. Add your user to the "docker" group:
    ```
    $ sudo usermod -aG docker $USER
    ```

3. Install Node Version Manager (NVM) and NodeJS version 16:
    ```
    $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    $ nvm install --lts 16
    $ nvm alias default 16
    $ nvm use 16
    ```

4. Install Yarn 1.x:
    ```
    $ npm install --global yarn@1.22.19
    ```

#### Installation Steps

5. Clone the Redash source code and install NodeJS dependencies:
    ```
    $ git clone https://github.com/birehan/Redash-NLP-Chatbot-Analytics
    $ cd redash
    $ yarn
    ```

6. Generate your local environment variables file (`.env`):
    ```
    $ make env
    ```
    Add your OpenAI API key to the `.env` file:
    ```
    OPENAI_API_KEY=*****************************************
    ```

7. Compile and build:
    ```
    $ make build
    $ make compose_build
    ```

8. Verify the local docker images:
    ```
    $ docker image list
    ```

9. Start Redash locally:
    ```
    $ make create_database
    $ make up
    ```
    Access the Redash web interface at http://localhost:5001 for configuration.

### Shutdown
To stop the containers:
