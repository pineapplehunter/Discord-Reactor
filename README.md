# Reactor

This is a discord bot that sends you a reaction when someone makes a reaction on your post.

## Run

I used pip env for this project.
The setup is simple. run the commands bellow and install pipenv.

```bash
$ sudo -H pip install pipenv
# pip or pip3
```

Now clone this repo and setup this project.

```bash
$ git clone https://github.com/peshogo/Discord-Reactor.git
$ cd Discord-Reactor
$ pipenv install
```

copy your token into `/config/token.py`. You can copy `/config/token_sample.py` to make things simpler.

```bash
$ cp config/token_sample.py config/token.py
```

Now run your bot!!!
Run it with

```bash
$ pipenv run python main.py
```

OR

```bash
$ pipenv shell
(pipenvshell)$ python main.py
```