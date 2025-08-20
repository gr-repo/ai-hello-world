# AI Hello World
This is a **public repository** with a set of "getting started" guides that run completely in GitHub Codespaces. This repo calls public LLM's so if you run this in a corporate be aware that you will be sending data out to the public internet.

See the [notebooks](./notebooks/) folder there's a folder per technology/subject.

# Setup Steps
1. Go to [MySettings](./src/common/my_settings.py) to see what settings are required. You can override these manually in the [MySettings](./src/common/my_settings.py) class or setup your environment. The default is to pull from GitHub Codespaces dev env.

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
#### How too add an env secret
1. Browse to the code repo > settings > Secrets and variables > Codespaces: https://github.com/YOURREPOSITORYNAME/settings/secrets/codespaces
1. Click: Add new repository key
1. Create key, don't use quotes on value
1. If you have the Codespace running you may need to restart it and wait a couple of minutes






# 