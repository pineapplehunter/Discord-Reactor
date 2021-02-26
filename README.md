# Reactor

This is a discord bot that sends you a reaction when someone makes a reaction on your post.

## Run

I used [poetry][] for this project.
The setup is simple. run the commands bellow and install poetry.

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# pip or pip3
```

Now clone this repo and setup this project.

```bash
$ git clone https://github.com/pineapplehunter/Discord-Reactor.git
$ cd Discord-Reactor
$ pipenv install
```

write your token into `/discord_reactor/config/token.py` with the ariable `TOKEN`. You can copy `/discord_reactor/config/token_sample.py` to make things simpler.

```bash
$ cp discord_reactor/config/token_sample.py discord_reactor/config/token.py
```

Now run your bot!!!
Run it with

```bash
$ poetry run reactor
```

[poetry]:https://python-poetry.org/