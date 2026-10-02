import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# =========================================================
# NEXUS CONFIGURATION
# =========================================================

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


# =========================================================
# SERVER STRUCTURE
# =========================================================

ROLE_CONFIG = {
    # STAFF
    "👑 Owner": ((241, 196, 15), True),
    "⚙️ Administrator": ((231, 76, 60), True),
    "🛡️ Manager": ((192, 57, 43), True),
    "🔨 Moderator": ((230, 126, 34), True),
    "🎫 Support": ((52, 152, 219), True),
    "🏆 Head Booster / Coach": ((142, 68, 173), True),
    "🚀 Booster / Coach": ((155, 89, 182), True),

    # CLIENTS
    "💎 Premium Client": ((255, 193, 7), True),
    "✅ Verified Client": ((46, 204, 113), False),
    "👤 Member": ((149, 165, 166), False),
    "🔒 Unverified": ((99, 110, 114), False),

    # RANKS
    "🏆 Challenger": ((244, 208, 63), False),
    "🔴 Grandmaster": ((231, 76, 60), False),
    "🟣 Master": ((155, 89, 182), False),
    "💎 Diamond": ((85, 170, 255), False),
    "💚 Emerald": ((46, 204, 113), False),
    "🔷 Platinum": ((72, 201, 176), False),
    "🥇 Gold": ((241, 196, 15), False),
    "🥈 Silver": ((189, 195, 199), False),
    "🥉 Bronze": ((205, 127, 50), False),
    "⚫ Iron": ((88, 101, 103), False),
    "❔ Unranked": ((127, 140, 141), False),

    # POSITIONS
    "⚔️ Top": ((88, 101, 103), False),
    "🌲 Jungle": ((88, 101, 103), False),
    "🧙 Mid": ((88, 101, 103), False),
    "🏹 ADC": ((88, 101, 103), False),
    "💚 Support": ((88, 101, 103), False),

    # REGIONS
    "🇺🇸 NA": ((88, 101, 103), False),
    "🇪🇺 EUW": ((88, 101, 103), False),
    "🇪🇺 EUNE": ((88, 101, 103), False),
    "🇰🇷 KR": ((88, 101, 103), False),
    "🌏 OCE": ((88, 101, 103), False),
    "🇧🇷 BR": ((88, 101, 103), False),
    "🌎 LAN": ((88, 101, 103), False),
    "🌎 LAS": ((88, 101, 103), False),
    "🇹🇷 TR": ((88, 101, 103), False),
    "🇯🇵 JP": ((88, 101, 103), False),
}

STAFF_ROLES = [
    "👑 Owner",
    "⚙️ Administrator",
    "🛡️ Manager",
    "🔨 Moderator",
    "🎫 Support",
    "🏆 Head Booster / Coach",
    "🚀 Booster / Coach",
]

MEMBER_ROLES = [
    "💎 Premium Client",
    "✅ Verified Client",
    "👤 Member",
    "🔒 Unverified",
]

RANK_ROLES = [
    "🏆 Challenger",
    "🔴 Grandmaster",
    "🟣 Master",
    "💎 Diamond",
    "💚 Emerald",
    "🔷 Platinum",
    "🥇 Gold",
    "🥈 Silver",
    "🥉 Bronze",
    "⚫ Iron",
    "❔ Unranked",
]

POSITION_ROLES = [
    "⚔️ Top",
    "🌲 Jungle",
    "🧙 Mid",
    "🏹 ADC",
    "💚 Support",
]

REGION_ROLES = [
    "🇺🇸 NA",
    "🇪🇺 EUW",
    "🇪🇺 EUNE",
    "🇰🇷 KR",
    "🌏 OCE",
    "🇧🇷 BR",
    "🌎 LAN",
    "🌎 LAS",
    "🇹🇷 TR",
    "🇯🇵 JP",
]

SERVER_STRUCTURE = {
    "👋 START HERE": {
        "text": [
            "👋・welcome",
            "📜・rules",
            "📢・announcements",
            "❓・faq",
            "🎭・choose-roles",
            "✅・verify",
            "🎫・support",
        ],
        "voice": [],
    },

    "🛒 SERVICES": {
        "text": [
            "📋・services",
            "💰・pricing",
            "🎓・coaching",
            "🎥・vod-review",
            "🧠・improvement-plans",
            "👥・duo-coaching",
            "🛒・place-an-order",
        ],
        "voice": [],
    },

    "⭐ RESULTS": {
        "text": [
            "⭐・reviews",
            "🏆・results",
        ],
        "voice": [],
    },

    "💬 COMMUNITY": {
        "text": [
            "💬・general",
            "🎮・league-chat",
            "🔥・clips-and-plays",
            "📊・ranked-discussion",
            "🧠・builds-and-meta",
            "😂・memes",
            "🤖・bot-commands",
        ],
        "voice": [],
    },

    "🔎 LOOKING FOR GROUP": {
        "text": [
            "🇺🇸・na-lfg",
            "🇪🇺・euw-lfg",
            "🇪🇺・eune-lfg",
            "🌎・other-regions",
        ],
        "voice": [],
    },

    "🔊 VOICE": {
        "text": [],
        "voice": [
            "🔊 General",
            "🎮 Ranked",
            "🎮 Duo",
            "🎓 Coaching 1",
            "🎓 Coaching 2",
            "💤 AFK",
        ],
    },

    "🎓 COACHES": {
        "text": [
            "📋・coach-information",
            "📅・coach-availability",
            "📝・coach-applications",
            "💬・coach-questions",
        ],
        "voice": [],
    },

    "🛡️ STAFF": {
        "text": [
            "💬・staff-chat",
            "📋・staff-announcements",
            "🎫・ticket-logs",
            "📦・order-management",
            "⭐・review-management",
            "🚨・reports",
            "🤖・bot-logs",
        ],
        "voice": [
            "🔊 Staff VC",
        ],
    },
}

# =========================================================
# VERIFICATION CONFIGURATION
# =========================================================

SERVICE_OPTIONS = {
    "boosting": "🚀 Boosting",
    "coaching": "🎓 Live Coaching",
    "vod": "🎥 VOD Review",
    "improvement": "🧠 Ranked Improvement",
    "community": "🎮 Community",
    "staff": "❓ Talk to Staff",
}

REGION_OPTIONS = {
    "na": "🇺🇸 NA",
    "euw": "🇪🇺 EUW",
    "eune": "🇪🇺 EUNE",
    "kr": "🇰🇷 KR",
    "oce": "🌏 OCE",
    "br": "🇧🇷 BR",
    "lan": "🌎 LAN",
    "las": "🌎 LAS",
    "tr": "🇹🇷 TR",
    "jp": "🇯🇵 JP",
}

RANK_OPTIONS = {
    "challenger": "🏆 Challenger",
    "grandmaster": "🔴 Grandmaster",
    "master": "🟣 Master",
    "diamond": "💎 Diamond",
    "emerald": "💚 Emerald",
    "platinum": "🔷 Platinum",
    "gold": "🥇 Gold",
    "silver": "🥈 Silver",
    "bronze": "🥉 Bronze",
    "iron": "⚫ Iron",
    "unranked": "❔ Unranked",
}

POSITION_OPTIONS = {
    "top": "⚔️ Top",
    "jungle": "🌲 Jungle",
    "mid": "🧙 Mid",
    "adc": "🏹 ADC",
    "support": "💚 Support",
}

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def find_role(guild, role_name):
    return discord.utils.get(guild.roles, name=role_name)


def find_category(guild, category_name):
    return discord.utils.get(guild.categories, name=category_name)


async def create_role_if_missing(guild, role_name):
    existing = find_role(guild, role_name)

    color_rgb, hoist = ROLE_CONFIG.get(
        role_name,
        ((149, 165, 166), False)
    )

    color = discord.Colour.from_rgb(*color_rgb)

    if existing:
        # Bots cannot edit roles at or above their highest role.
        if guild.me and existing >= guild.me.top_role:
            print(f"Skipping unmanageable role: {role_name}")
            return existing, False

        try:
            await existing.edit(
                colour=color,
                hoist=hoist,
                reason="Nexus role styling sync"
            )

        except discord.Forbidden:
            print(f"No permission to edit role: {role_name}")

        return existing, False

    role = await guild.create_role(
        name=role_name,
        colour=color,
        hoist=hoist,
        reason="Nexus server setup"
    )

    return role, True

async def organize_roles(guild):
    bot_member = guild.me

    if bot_member is None:
        return

    bot_top_role = bot_member.top_role

    ordered_names = (
        STAFF_ROLES
        + MEMBER_ROLES
        + RANK_ROLES
        + POSITION_ROLES
        + REGION_ROLES
    )

    # Get all Nexus-managed roles that Nexus is allowed to manage
    roles = []

    for role_name in ordered_names:
        role = find_role(guild, role_name)

        if role is None:
            continue

        if role >= bot_top_role:
            print(f"Skipping role above Nexus: {role_name}")
            continue

        roles.append(role)

    if not roles:
        print("No manageable Nexus roles found.")
        return

    try:
        # Work from bottom to top.
        # Each role gets placed directly below the role above it.
        previous_role = None

        for role in reversed(roles):

            if previous_role is None:
                # Keep the lowest managed role safely above @everyone
                await role.edit(position=1)
            else:
                await role.move(above=previous_role)

            previous_role = role

        print(f"Successfully organized {len(roles)} Nexus roles.")

    except discord.Forbidden:
        print(
            "Nexus cannot organize these roles. "
            "Make sure the Nexus bot role is above all managed roles."
        )

    except discord.HTTPException as error:
        print(f"Discord role organization error: {error}")

    # We cannot fit more roles underneath Nexus than there are
    # available positions.
    max_roles = highest_available

    if len(managed_roles) > max_roles:
        print(
            f"Warning: Nexus can only organize {max_roles} roles "
            f"at its current hierarchy position."
        )
        managed_roles = managed_roles[:max_roles]

    # Bulk role positioning is more reliable than moving
    # every role individually.
    positions = {}

    for index, role in enumerate(managed_roles):
        target_position = highest_available - index

        if target_position < 1:
            break

        positions[role] = target_position

    if positions:
        try:
            await guild.edit_role_positions(
                positions=positions,
                reason="Nexus role hierarchy sync"
            )

            print(f"Organized {len(positions)} roles.")

        except discord.Forbidden:
            print(
                "Nexus does not have permission to organize roles. "
                "Move the Nexus role higher in Server Settings > Roles."
            )

        except discord.HTTPException as error:
            print(f"Role organization error: {error}")

    for role_name in ordered_names:
        role = find_role(guild, role_name)

        if role is None:
            continue

        # Nexus cannot manage roles equal to or above its own role.
        if role >= bot_top_role:
            print(f"Skipping role above Nexus: {role_name}")
            continue

        try:
            await role.edit(
                position=target_position,
                reason="Nexus role hierarchy sync"
            )

            target_position -= 1

        except discord.Forbidden:
            print(f"Nexus cannot move role: {role_name}")

        except discord.HTTPException as error:
            print(f"Could not move {role_name}: {error}")


async def create_category_if_missing(guild, category_name):
    existing = find_category(guild, category_name)

    if existing:
        return existing, False

    category = await guild.create_category(
        category_name,
        reason="Nexus server setup"
    )

    return category, True


async def create_text_channel_if_missing(guild, category, channel_name):
    existing = discord.utils.get(
        guild.text_channels,
        name=channel_name
    )

    if existing:
        return existing, False

    channel = await guild.create_text_channel(
        channel_name,
        category=category,
        reason="Nexus server setup"
    )

    return channel, True


async def create_voice_channel_if_missing(guild, category, channel_name):
    existing = discord.utils.get(
        guild.voice_channels,
        name=channel_name
    )

    if existing:
        return existing, False

    channel = await guild.create_voice_channel(
        channel_name,
        category=category,
        reason="Nexus server setup"
    )

    return channel, True

# =========================================================
# VERIFICATION GUI
# =========================================================

class ChampionModal(discord.ui.Modal, title="League Profile"):

    champions = discord.ui.TextInput(
        label="Who are your main champions?",
        placeholder="Example: Katarina, Akali, Zed",
        max_length=150,
        required=True
    )

    goals = discord.ui.TextInput(
        label="What are you looking for?",
        placeholder="Tell us what you want help with...",
        style=discord.TextStyle.paragraph,
        max_length=500,
        required=False
    )

    def __init__(self, answers):
        super().__init__()
        self.answers = answers

    async def on_submit(self, interaction: discord.Interaction):

        if interaction.guild is None:
            await interaction.response.send_message(
                "Verification must be completed inside the server.",
                ephemeral=True
            )
            return

        member = interaction.user

        self.answers["champions"] = str(self.champions)
        self.answers["goals"] = str(self.goals)

        # Find roles
        member_role = find_role(interaction.guild, "👤 Member")
        unverified_role = find_role(interaction.guild, "🔒 Unverified")

        region_role = find_role(
            interaction.guild,
            self.answers["region"]
        )

        rank_role = find_role(
            interaction.guild,
            self.answers["rank"]
        )

        position_role = find_role(
            interaction.guild,
            self.answers["position"]
        )

        roles_to_add = [
            role for role in [
                member_role,
                region_role,
                rank_role,
                position_role
            ]
            if role is not None
        ]

        try:
            if roles_to_add:
                await member.add_roles(
                    *roles_to_add,
                    reason="Nexus verification completed"
                )

            if unverified_role and unverified_role in member.roles:
                await member.remove_roles(
                    unverified_role,
                    reason="Nexus verification completed"
                )

        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Nexus couldn't assign your roles. "
                "Please contact a server administrator.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="✅ Verification Complete",
            description=(
                f"Welcome to **{interaction.guild.name}**, "
                f"{member.mention}!\n\n"
                "Your League profile has been saved and "
                "your server roles have been assigned."
            )
        )

        embed.add_field(
            name="What brings you here?",
            value=self.answers["service"],
            inline=False
        )

        embed.add_field(
            name="Region",
            value=self.answers["region"],
            inline=True
        )

        embed.add_field(
            name="Rank",
            value=self.answers["rank"],
            inline=True
        )

        embed.add_field(
            name="Position",
            value=self.answers["position"],
            inline=True
        )

        embed.add_field(
            name="Main Champions",
            value=self.answers["champions"],
            inline=False
        )

        if self.answers["goals"]:
            embed.add_field(
                name="What you're looking for",
                value=self.answers["goals"],
                inline=False
            )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# ---------------------------------------------------------
# POSITION
# ---------------------------------------------------------

class PositionSelect(discord.ui.Select):

    def __init__(self, answers):

        self.answers = answers

        options = [
            discord.SelectOption(
                label=name.split(" ", 1)[1],
                value=key,
                emoji=name.split(" ", 1)[0]
            )
            for key, name in POSITION_OPTIONS.items()
        ]

        super().__init__(
            placeholder="Select your main position...",
            options=options
        )

    async def callback(self, interaction):

        key = self.values[0]

        self.answers["position"] = POSITION_OPTIONS[key]

        await interaction.response.send_modal(
            ChampionModal(self.answers)
        )


class PositionView(discord.ui.View):

    def __init__(self, answers):
        super().__init__(timeout=300)
        self.add_item(PositionSelect(answers))


# ---------------------------------------------------------
# RANK
# ---------------------------------------------------------

class RankSelect(discord.ui.Select):

    def __init__(self, answers):

        self.answers = answers

        options = [
            discord.SelectOption(
                label=name.split(" ", 1)[1],
                value=key,
                emoji=name.split(" ", 1)[0]
            )
            for key, name in RANK_OPTIONS.items()
        ]

        super().__init__(
            placeholder="Select your current rank...",
            options=options
        )

    async def callback(self, interaction):

        key = self.values[0]

        self.answers["rank"] = RANK_OPTIONS[key]

        await interaction.response.edit_message(
            content="### ⚔️ What's your main position?",
            view=PositionView(self.answers)
        )


class RankView(discord.ui.View):

    def __init__(self, answers):
        super().__init__(timeout=300)
        self.add_item(RankSelect(answers))


# ---------------------------------------------------------
# REGION
# ---------------------------------------------------------

class RegionSelect(discord.ui.Select):

    def __init__(self, answers):

        self.answers = answers

        options = [
            discord.SelectOption(
                label=name.split(" ", 1)[1],
                value=key,
                emoji=name.split(" ", 1)[0]
            )
            for key, name in REGION_OPTIONS.items()
        ]

        super().__init__(
            placeholder="Select your region...",
            options=options
        )

    async def callback(self, interaction):

        key = self.values[0]

        self.answers["region"] = REGION_OPTIONS[key]

        await interaction.response.edit_message(
            content="### 🏆 What's your current rank?",
            view=RankView(self.answers)
        )


class RegionView(discord.ui.View):

    def __init__(self, answers):
        super().__init__(timeout=300)
        self.add_item(RegionSelect(answers))


# ---------------------------------------------------------
# SERVICE
# ---------------------------------------------------------

class ServiceSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(
                label="Boosting",
                value="boosting",
                emoji="🚀"
            ),
            discord.SelectOption(
                label="Live Coaching",
                value="coaching",
                emoji="🎓"
            ),
            discord.SelectOption(
                label="VOD Review",
                value="vod",
                emoji="🎥"
            ),
            discord.SelectOption(
                label="Ranked Improvement",
                value="improvement",
                emoji="🧠"
            ),
            discord.SelectOption(
                label="Community",
                value="community",
                emoji="🎮"
            ),
            discord.SelectOption(
                label="Talk to Staff",
                value="staff",
                emoji="❓"
            ),
        ]

        super().__init__(
            placeholder="What brings you here?",
            options=options
        )

    async def callback(self, interaction):

        answers = {
            "service": SERVICE_OPTIONS[self.values[0]]
        }

        await interaction.response.edit_message(
            content="### 🌎 What region do you play on?",
            view=RegionView(answers)
        )


class ServiceView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=300)
        self.add_item(ServiceSelect())


# ---------------------------------------------------------
# GET STARTED BUTTON
# ---------------------------------------------------------

class VerificationView(discord.ui.View):

    def __init__(self):
        # None makes this persistent across normal bot uptime.
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Get Started",
        emoji="✅",
        style=discord.ButtonStyle.green,
        custom_id="nexus:get_started"
    )
    async def get_started(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if interaction.guild is None:
            return

        member_role = find_role(
            interaction.guild,
            "👤 Member"
        )

        if member_role and member_role in interaction.user.roles:
            await interaction.response.send_message(
                "You're already verified.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "### 👋 What brings you here?\n"
            "Choose the option that best matches what you're looking for.",
            view=ServiceView(),
            ephemeral=True
        )
# =========================================================
# BOT EVENTS
# =========================================================

@bot.event
async def on_ready():
    print("=" * 50)
    print("Nexus is online!")
    print(f"Logged in as: {bot.user}")
    print(f"Connected to {len(bot.guilds)} server(s)")
    print("=" * 50)

    bot.add_view(VerificationView())

    try:
        for guild in bot.guilds:
            bot.tree.copy_global_to(guild=guild)
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to {guild.name}")

    except Exception as error:
        print(f"Slash Command sync error: {error}")
@bot.event
async def on_member_join(member):
    unverified_role = find_role(
        member.guild,
        "🔒 Unverified"
    )

    if unverified_role is None:
        print("Unverified role was not found.")
        return

    try:
        await member.add_roles(
            unverified_role,
            reason="New member awaiting Nexus verification"
        )

        print(f"Added Unverified role to {member}")

    except discord.Forbidden:
        print(
            f"Could not give Unverified role to {member}. "
            "Check Nexus role permissions."
        )

# =========================================================
# /SETUP-SERVER
# =========================================================
@bot.tree.command(
    name="setup-verification",
    description="Post the Nexus verification interface."
)
@app_commands.checks.has_permissions(administrator=True)
async def setup_verification(interaction: discord.Interaction):

    if interaction.guild is None:
        await interaction.response.send_message(
            "This command can only be used inside a server.",
            ephemeral=True
        )
        return

    verify_channel = discord.utils.get(
        interaction.guild.text_channels,
        name="✅・verify"
    )

    if verify_channel is None:
        await interaction.response.send_message(
            "❌ I couldn't find #✅・verify. Run `/setup-server` first.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="⚔️ Welcome to Nexus",
        description=(
            "**Complete verification to unlock the server.**\n\n"
            "We'll ask you a few quick questions about your "
            "League profile and what you're looking for.\n\n"
            "**You'll choose:**\n"
            "• What brought you here\n"
            "• Your region\n"
            "• Your current rank\n"
            "• Your main position\n"
            "• Your main champions\n\n"
            "Click **Get Started** below to begin."
        )
    )

    embed.set_footer(
        text="Nexus • League Services & Community"
    )

    await verify_channel.send(
        embed=embed,
        view=VerificationView()
    )

    await interaction.response.send_message(
        f"✅ Verification interface posted in {verify_channel.mention}.",
        ephemeral=True
    )
    # =========================================================
# /SETUP-PERMISSIONS
# =========================================================

@bot.tree.command(
    name="setup-permissions",
    description="Configure Nexus verification and category permissions."
)
@app_commands.checks.has_permissions(administrator=True)
async def setup_permissions(interaction: discord.Interaction):

    if interaction.guild is None:
        await interaction.response.send_message(
            "This command can only be used inside a server.",
            ephemeral=True
        )
        return

    await interaction.response.defer(ephemeral=True)

    guild = interaction.guild

    everyone = guild.default_role
    member_role = find_role(guild, "👤 Member")
    unverified_role = find_role(guild, "🔒 Unverified")

    if member_role is None or unverified_role is None:
        await interaction.followup.send(
            "❌ I couldn't find the Member or Unverified role. "
            "Run `/setup-server` first.",
            ephemeral=True
        )
        return

    # Categories visible before verification
    start_here = discord.utils.get(
        guild.categories,
        name="👋 START HERE"
    )

    # Categories unlocked after verification
    locked_until_verified = [
        "🛒 SERVICES",
        "⭐ RESULTS",
        "💬 COMMUNITY",
        "🔎 LOOKING FOR GROUP",
        "🔊 VOICE",
        "🎓 COACHES",
    ]

    try:
        # ---------------------------------------------
        # START HERE
        # Everyone can see this category.
        # ---------------------------------------------
        if start_here:
            await start_here.set_permissions(
                everyone,
                view_channel=True,
                read_message_history=True
            )

            await start_here.set_permissions(
                unverified_role,
                view_channel=True,
                read_message_history=True
            )

            await start_here.set_permissions(
                member_role,
                view_channel=True,
                read_message_history=True
            )

        # ---------------------------------------------
        # MEMBER-ONLY CATEGORIES
        # ---------------------------------------------
        for category_name in locked_until_verified:

            category = discord.utils.get(
                guild.categories,
                name=category_name
            )

            if category is None:
                continue

            # Hide from normal/unverified users
            await category.set_permissions(
                everyone,
                view_channel=False
            )

            await category.set_permissions(
                unverified_role,
                view_channel=False
            )

            # Unlock for verified members
            await category.set_permissions(
                member_role,
                view_channel=True,
                read_message_history=True,
                send_messages=True,
                connect=True,
                speak=True
            )

        # ---------------------------------------------
        # STAFF CATEGORY
        # ---------------------------------------------
        staff_category = discord.utils.get(
            guild.categories,
            name="🛡️ STAFF"
        )

        if staff_category:
            await staff_category.set_permissions(
                everyone,
                view_channel=False
            )

            await staff_category.set_permissions(
                unverified_role,
                view_channel=False
            )

            await staff_category.set_permissions(
                member_role,
                view_channel=False
            )

            staff_role_names = [
                "⚙️ Administrator",
                "🛡️ Manager",
                "🔨 Moderator",
                "🎫 Support",
                "🏆 Head Booster / Coach",
                "🚀 Booster / Coach",
            ]

            for role_name in staff_role_names:
                role = find_role(guild, role_name)

                if role:
                    await staff_category.set_permissions(
                        role,
                        view_channel=True,
                        read_message_history=True,
                        send_messages=True,
                        connect=True,
                        speak=True
                    )

        await interaction.followup.send(
            "🔒 **Nexus permissions configured.**\n\n"
            "New members can see **START HERE** before verification.\n"
            "After verification, the **Member** role unlocks the server.\n"
            "The **STAFF** category remains restricted to staff.",
            ephemeral=True
        )

    except discord.Forbidden:
        await interaction.followup.send(
            "❌ Nexus doesn't have permission to modify one or more "
            "categories. Check the Nexus role and Manage Channels permission.",
            ephemeral=True
        )

    except Exception as error:
        print(f"Permission setup error: {error}")

        await interaction.followup.send(
            f"❌ Permission setup failed: `{error}`",
            ephemeral=True
        )
@bot.tree.command(
    name="setup-server",
    description="Build the Nexus server structure."
)
@app_commands.checks.has_permissions(administrator=True)
async def setup_server(interaction: discord.Interaction):

    if interaction.guild is None:
        await interaction.response.send_message(
            "This command can only be used inside a server.",
            ephemeral=True
        )
        return

    await interaction.response.defer(ephemeral=True)

    guild = interaction.guild

    roles_created = 0
    categories_created = 0
    text_channels_created = 0
    voice_channels_created = 0

    try:



        # -----------------------------------------
        # CREATE ROLES
        # -----------------------------------------

        all_roles = (
            STAFF_ROLES
            + MEMBER_ROLES
            + RANK_ROLES
            + POSITION_ROLES
            + REGION_ROLES
        )

        for role_name in reversed(all_roles):

            _, created = await create_role_if_missing(
                guild,
                role_name
            )

            if created:
                roles_created += 1

                        # Organize role hierarchy
        #await organize_roles(guild)

        # -----------------------------------------
        # CREATE CATEGORIES + CHANNELS
        # -----------------------------------------

        for category_name, channels in SERVER_STRUCTURE.items():

            category, created = await create_category_if_missing(
                guild,
                category_name
            )

            if created:
                categories_created += 1

            # TEXT CHANNELS

            for channel_name in channels["text"]:

                _, created = await create_text_channel_if_missing(
                    guild,
                    category,
                    channel_name
                )

                if created:
                    text_channels_created += 1

            # VOICE CHANNELS

            for channel_name in channels["voice"]:

                _, created = await create_voice_channel_if_missing(
                    guild,
                    category,
                    channel_name
                )

                if created:
                    voice_channels_created += 1

        # -----------------------------------------
        # COMPLETE
        # -----------------------------------------

        embed = discord.Embed(
            title="✅ Nexus Server Setup Complete",
            description=(
                "The base server structure has been created.\n\n"
                "Running `/setup-server` again will check for "
                "existing items instead of intentionally duplicating them."
            ),
        )

        embed.add_field(
            name="Roles Created",
            value=str(roles_created),
            inline=True
        )

        embed.add_field(
            name="Categories Created",
            value=str(categories_created),
            inline=True
        )

        embed.add_field(
            name="Text Channels",
            value=str(text_channels_created),
            inline=True
        )

        embed.add_field(
            name="Voice Channels",
            value=str(voice_channels_created),
            inline=True
        )

        await interaction.followup.send(
            embed=embed,
            ephemeral=True
        )

    except discord.Forbidden:

        await interaction.followup.send(
            "❌ Nexus doesn't have enough permissions to create "
            "one of the roles or channels.",
            ephemeral=True
        )

    except Exception as error:

        print(f"SETUP ERROR: {error}")

        await interaction.followup.send(
            f"❌ Setup encountered an error: `{error}`",
            ephemeral=True
        )


# =========================================================
# ERROR HANDLER
# =========================================================

@setup_server.error
async def setup_server_error(
    interaction: discord.Interaction,
    error: app_commands.AppCommandError
):

    if isinstance(error, app_commands.MissingPermissions):

        await interaction.response.send_message(
            "❌ You need Administrator permission to run `/setup-server`.",
            ephemeral=True
        )

    else:

        print(f"Command error: {error}")


# =========================================================
# START NEXUS
# =========================================================

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN was not found in .env")

bot.run(TOKEN)