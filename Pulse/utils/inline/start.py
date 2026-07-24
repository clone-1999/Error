# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: sudeepgithub@gmail.com

from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

import config
from Pulse import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                icon_custom_emoji_id="5397733426654626788"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", icon_custom_emoji_id="5818802717455290572")],
        [
            InlineKeyboardButton(text="sυᴘᴘσʀᴛ", url="https://t.me/+JmZajlpyTJxlZTE1"),
            InlineKeyboardButton(text="υᴘᴅᴧᴛєs", url="https://t.me/+OqS-RsnNrMtjOTll"),
        ],
        [
            InlineKeyboardButton("❍ᴡηєʀ", url="https://t.me/+43lfMuxCp3I3ZDRl", icon_custom_emoji_id="5818802717455290572")            
        ],
    
    ]
    return buttons
