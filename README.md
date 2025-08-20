# AI Hello World
This is a **public repository** with a set of getting started guides that run completely in GitHub Codespaces. This repo calls public LLM's so <span style="color: red;">if you run this on your computer in a corporate be aware that **you will be sending data out to the public internet**.</span>

See the [notebooks](./notebooks/) folder there's a folder per technology/subject.

# Suggested Path 
1. Do [Setup Steps](#setup-steps) below to setup your environment
1. Run [openai_1_hello_world.ipynb](/notebooks/openai_notebooks/openai_1_hello_world.ipynb) to test connectivity. Most calls are into Open AI so do this first to sort out connectivity and api key isses.
1. Start exploring [notebooks](./notebooks/) folders
1. Keep an eye on [Monitor costs](#monitor-costs)

# Setup Steps
### Open AI Setup
#### How to create a new Open AI API Key
1. Goto API Keys: https://platform.openai.com/settings/organization/api-keys 
1. Create new secret key

#### How to add more models to call into
1. Go to Settings: https://platform.openai.com/settings/organization/general
1. Click SECOND "Limit" menu heading, there are two on the list in the RHS. 
1. On "Project limits" page...
1. Under "Model usage" > "Allowed models" click Edit
1. Select models you want to add/remove

### Codespaces Setup
NOTE: Running Codespaces has a cost implications that hits **the user running the application**. If your account is linked to a corporate account they will not necessarily pick up the cost. 
This cost is mininal and the Codespaces auto-turn themselves off. 
See [GitHub Codespaces billing
](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)

#### How too add an env secret
1. Browse to the code repo > settings > Secrets and variables > Codespaces: https://github.com/YOURREPOSITORYNAME/settings/secrets/codespaces
1. Click: Add new repository key
1. Create key, don't use quotes on value
1. If you have the Codespace running you may need to restart it and wait a couple of minutes

#### How to run a new Codespace in the browser
1. Browse to [GitHub Codespaces](https://github.com/codespaces)
1. Click "Use this template" under Jupyter Notbook
1. A new space will spin up that is a fork of Visual Studio Code
1. This runs in a container on GitHub Codespaces outside of corporate networks.

#### How to run a Codespace off a repository
1. Browse to a repo: https://github.com/gr-repo/ai-hello-world
1. Click the green "Code" button
1. Click "Codespaces" tab
1. Choose your Codespace option (i.e., + to create a new one)
1. This runs in a container on GitHub Codespaces outside of corporate networks.

#### How work in Visual Studio Code Desktop but run the Codespace from the cloud
1. You can edit code in VS Code but the app runs in the cloud
1. Browse to [Codespaces](https://github.com/codespaces)
1. Scroll down to existing Codespaces you have created
1. Click the "..."
1. Select "Open in Visual Studio Code"
1. This runs in a container on GitHub Codespaces outside of corporate networks.

### Development environment before running code
1. Go to [MySettings](./src/common/my_settings.py) to see what settings are required. You can override these manually in the [MySettings](./src/common/my_settings.py) class or setup your environment. The default is to pull from GitHub Codespaces dev env.
1. Run Editable Package Installation
    1. This makes files under "src" behave as packages so you can import them using
    1. Open Terminal
    1. Go to project rool /workspaces/ai-hell-world
    1. Run "pip install -e ."

# Monitor Costs
1. [OpenAI Usage](https://platform.openai.com/settings/organization/usage)
1. [Codespaces Usage](https://github.com/settings/billing/usage)











# 