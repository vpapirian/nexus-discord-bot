<div align="center">

# 🌐 Nexus Discord Bot

**Build a complete League of Legends coaching/community Discord server with one command.**

Roles, categories, channels, permissions and a step-by-step verification flow are all generated automatically.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.x-5865F2?logo=discord&logoColor=white)
![Slash Commands](https://img.shields.io/badge/UI-Slash_Commands_%2B_Modals-5865F2)

</div>

---

## ✨ Features

- 🏗️ **`/setup-server`** creates every role, category, text channel and voice channel, colors included. It skips anything that already exists, so it's safe to run more than once.
- 🔐 **`/setup-permissions`** locks the server to verified members, gives staff private categories and keeps the welcome area public.
- ✅ **`/setup-verification`** posts an interactive onboarding panel where new members choose:
  - 🎯 What they're here for (coaching, boosting, community…)
  - 🌍 **Region:** NA, EUW, EUNE, KR, OCE, BR, LAN, LAS, TR, JP
  - 🏆 **Rank:** Iron through Challenger
  - ⚔️ **Position:** Top, Jungle, Mid, ADC, Support
  - 📝 **Main champions:** entered through a popup form
- 👋 **Auto-role on join:** new members start as `🔒 Unverified` until they finish onboarding.

## 🧱 Role layout

| Group | Roles |
|---|---|
| Staff | 👑 Owner · ⚙️ Administrator · 🛡️ Manager · 🔨 Moderator · 🎫 Support · 🏆 Head Booster / Coach · 🚀 Booster / Coach |
| Members | 💎 Premium Client · ✅ Verified Client · 👤 Member · 🔒 Unverified |
| Ranks | Challenger → Iron, plus Unranked |
| Positions | Top · Jungle · Mid · ADC · Support |
| Regions | 10 server regions |

## 🚀 Setup

1. Create an application at the [Discord Developer Portal](https://discord.com/developers/applications) and add a **Bot**.
2. Under **Privileged Gateway Intents**, turn on **Server Members Intent**.
3. Invite the bot with the `bot` and `applications.commands` scopes and **Administrator** permission.
4. Run it:

```bash
git clone https://github.com/vpapirian/nexus-discord-bot.git
cd nexus-discord-bot
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
copy .env.example .env    # paste your bot token into DISCORD_TOKEN
python bot.py
```

5. In your server, run `/setup-server`, then `/setup-permissions`, then `/setup-verification`.

> ⚠️ Never commit your `.env` file. Your bot token gives full control of the bot.

## 🛠️ Customizing

Everything is defined in plain dictionaries at the top of `bot.py`:

- `ROLE_CONFIG`: role names, colors and whether each role is hoisted
- `SERVER_STRUCTURE`: categories with their text and voice channels
- `STAFF_ROLES`, `RANK_ROLES`, `POSITION_ROLES`, `REGION_ROLES`

Edit them and run `/setup-server` again.

---

<div align="center">Built by <a href="https://github.com/vpapirian">Vatche Papirian</a></div>
