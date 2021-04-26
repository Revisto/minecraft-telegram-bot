# MineCraft Telgram Bot
## _A Telegram Bot that can manage your mc server and inform you_

MTB is a fast, customizable, useful telegram bot for your Minecraft server.

![](https://revisto.ir/static/projects-cover/minecraft-telegram-bot.jpg)

## ✨ Features ( till now )

- Number of online users
- Usernames of online users

## ⚙️ Installation

MTB only and only requires [Docker](https://www.docker.com/) to run.

Install Docker and start the bot, docker takes care of other dependencies.

```sh
apt install docker-ce
```

Now clone the repo:
```sh
git clone https://github.com/revisto/minecraft-telegram-bot
cd minecraft-telegram-bot
```

Let's take care of .env files...

```sh
cp mc_bot/.env.example .env
```
.env file contains your minecraft server and your telegram bot data. fill it like this:
```
minecraft_server_ip = <IP>
minecraft_server_port = <PORT>
telegram_robot_access_token = <TELEGRAM_ACCESS_TOKEN>
```

## Docker

Make sure that you have done all installation steps and made .env files.
then, build it and run it.
```sh
docker build -t mc_bot .
docker run -d mc_bot
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/revisto/minecraft-telegram-bot/issues) if you want to contribute.<br /><br />


## Show your support

Please ⭐️ this repository if this project helped you!


## 📝 License

GNUv2

**Free Software, Hell Yeah!**
