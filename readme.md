## ChatGPT in your shell

![](https://imgur.com/JphOx3D.png)

OpenAI's ChatGPT integrated into your shell.

![](https://imgur.com/J7YOzSz.png)

### Note ChatGPT4 - Limited Access Beta

I have changed the default model to ChatGPT 4 - I would recommend switching it to `gpt-3.5-turbo` for a more fluent experience. 

You can switch API model using the `model` argument (note that running without this argument will use gpt-4)

```$ genie --model gpt-3.5-turbo```

`model` will also accept *code-davinci-002* & *text-davinci-003* - other API models can be seen here [OpenAI ChatGPT API Models](https://platform.openai.com/docs/models) and added as required to the script.

### Description

Simple python implementation of OpenAI's ChatGPT intergrated into your shell, leveraging natural language processing and low temperature parameters for focused responses from ChatGPT.

The interaction can be either calling ChatGPT from shell for one off questions, or entering into an interactive chat with ChatGPT.

### Dependencies

* Install module dependencies using pip:
 ```pip install -r requirements.txt```

* OpenAI API key - you can get one [here](https://platform.openai.com/overview) - Dashboard - Settings - View API Keys - Generate


### Installing

* Clone the repo and copy *genie.py* to a permanent location.

* Open the script and amend `openai.api_key = "API_KEY"` with your aforementioned API key and save.

* Create an alias pointing at the script's location, either in your bash profile *~/.bash_profile* or *~/.bashrc* or *~/.zshrc* - i.e:
 ```alias genie='python3 /path/to/genie.py'```

### Usage

Using your chosen alias you can call it from shell and pass your question as an argument for one off questions:

```$ genie "What is the meaning of life?"```

![chatgpt](https://imgur.com/3lqDq7M.gif)

Or by calling the alias without argument to enter an interactive chat with ChatGPT:

```$ genie ```

![chatgpt-interactive](https://imgur.com/kJTBOPB.gif)


To end the interactive chat, use either `bye`,`quit`,`q` or `ctrl+c`.
