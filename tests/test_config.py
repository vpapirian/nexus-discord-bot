"""Consistency checks for the server layout and verification configuration.

Nexus silently skips roles it cannot find when verifying a member, and treats
channels with the same name as one channel, so mistakes in these tables show
up as missing roles or channels in a live server rather than as errors. These
tests catch them without needing a Discord connection.
"""
import pytest

import bot

ROLE_LISTS = {
    "staff": bot.STAFF_ROLES,
    "member": bot.MEMBER_ROLES,
    "rank": bot.RANK_ROLES,
    "position": bot.POSITION_ROLES,
    "region": bot.REGION_ROLES,
}

# Discord limits: https://discord.com/developers/docs/resources/guild
MAX_ROLES = 250
MAX_CHANNELS_PER_CATEGORY = 50
MAX_NAME_LENGTH = 100
MAX_SELECT_OPTIONS = 25


def all_roles():
    return [role for roles in ROLE_LISTS.values() for role in roles]


def test_importing_bot_does_not_start_it():
    # `import bot` above must not have connected or raised for a missing token.
    assert callable(bot.main)


def test_role_lists_have_no_duplicates():
    roles = all_roles()
    assert len(roles) == len(set(roles))


def test_every_role_has_a_style_and_every_style_has_a_role():
    assert set(all_roles()) == set(bot.ROLE_CONFIG)


def test_role_colors_are_valid_rgb():
    for name, (rgb, hoist) in bot.ROLE_CONFIG.items():
        assert len(rgb) == 3, name
        assert all(0 <= channel <= 255 for channel in rgb), name
        assert isinstance(hoist, bool), name


def test_role_count_fits_discord_limit():
    assert len(all_roles()) <= MAX_ROLES


@pytest.mark.parametrize(
    "options, role_list",
    [
        (bot.REGION_OPTIONS, bot.REGION_ROLES),
        (bot.RANK_OPTIONS, bot.RANK_ROLES),
        (bot.POSITION_OPTIONS, bot.POSITION_ROLES),
    ],
    ids=["region", "rank", "position"],
)
def test_verification_options_map_to_created_roles(options, role_list):
    assert set(options.values()) == set(role_list)


def test_verification_roles_used_by_the_modal_exist():
    assert "👤 Member" in bot.MEMBER_ROLES
    assert "🔒 Unverified" in bot.MEMBER_ROLES


@pytest.mark.parametrize(
    "options",
    [
        bot.SERVICE_OPTIONS,
        bot.REGION_OPTIONS,
        bot.RANK_OPTIONS,
        bot.POSITION_OPTIONS,
    ],
    ids=["service", "region", "rank", "position"],
)
def test_option_labels_split_into_emoji_and_label(options):
    assert len(options) <= MAX_SELECT_OPTIONS
    for key, name in options.items():
        emoji, _, label = name.partition(" ")
        assert emoji and label, f"{key!r} needs an 'emoji label' display name"
        assert len(label) <= MAX_NAME_LENGTH


def test_service_select_is_built_from_service_options():
    select = bot.ServiceSelect()
    assert [option.value for option in select.options] == list(
        bot.SERVICE_OPTIONS
    )
    for option in select.options:
        emoji, _, label = bot.SERVICE_OPTIONS[option.value].partition(" ")
        assert option.label == label
        assert str(option.emoji) == emoji


def test_category_names_are_unique_and_fit_limits():
    names = list(bot.SERVER_STRUCTURE)
    assert len(names) == len(set(names))
    assert all(len(name) <= MAX_NAME_LENGTH for name in names)


def test_channel_names_are_unique():
    # create_text_channel_if_missing / create_voice_channel_if_missing look
    # channels up by name across the whole server, so a repeated name would
    # be created once and skipped everywhere else.
    text = [
        name
        for channels in bot.SERVER_STRUCTURE.values()
        for name in channels["text"]
    ]
    voice = [
        name
        for channels in bot.SERVER_STRUCTURE.values()
        for name in channels["voice"]
    ]
    assert len(text) == len(set(text))
    assert len(voice) == len(set(voice))


def test_channels_fit_discord_limits():
    for category, channels in bot.SERVER_STRUCTURE.items():
        assert set(channels) == {"text", "voice"}, category
        assert (
            len(channels["text"]) + len(channels["voice"])
            <= MAX_CHANNELS_PER_CATEGORY
        ), category
        for name in channels["text"] + channels["voice"]:
            assert 0 < len(name) <= MAX_NAME_LENGTH, name
