#MIT License

#Copyright (c) 2021 subinps

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import re
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import *
from instaloader import Profile

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HELP=Config.HELP
session=f"./{USER}"

STATUS=Config.STATUS

insta = Config.L


@Client.on_message(filters.command("account") & filters.private)
async def account(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/subinps'),
						InlineKeyboardButton("🤖Other Bots", url="https://t.me/subin_works/122"),
                        
					],
                    [
        [
            InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/sthisara_favorites/6")
        ],
        [
            InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites"),
            InlineKeyboardButton("⚡️Disscussion Group⚡️", url="https://t.me/sthisara_favorites_disscussion")
        ],
        [
            InlineKeyboardButton("👾Report Errors👾", callback_data="help#subin")
        ]
					
				]
			)
		)
        return
    if 1 in STATUS:
        m=await message.reply_text("Getting Your data")
        try:
            profile = Profile.own_profile(insta.context)
            mediacount = profile.mediacount
            name = profile.full_name
            bio = profile.biography
            profilepic = profile.profile_pic_url
            username = profile.username
            igtvcount = profile.igtvcount
            followers = profile.followers
            following = profile.followees
            reply_markup=InlineKeyboardMarkup(
                [
                    [
        [
            InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/sthisara_favorites/6")
        ],
        [
            InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites"),
            InlineKeyboardButton("⚡️Disscussion Group⚡️", url="https://t.me/sthisara_favorites_disscussion")
        ],
        [
            InlineKeyboardButton("👾Report Errors👾", callback_data="help#subin")
        ]

                ]
                )
            await m.delete()
            await bot.send_photo(
                        chat_id=message.from_user.id,
                        photo=profilepic,
                        caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝**Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                        reply_markup=reply_markup
                    )
        except Exception as e:
            await m.edit(e)

    else:
        await message.reply_text("You must login first by /login")


@Client.on_message(filters.text & filters.private & filters.incoming)
async def _insta_post_batch(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
					[
        [
            InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/sthisara_favorites/6")
        ],
        [
            InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites"),
            InlineKeyboardButton("⚡️Disscussion Group⚡️", url="https://t.me/sthisara_favorites_disscussion")
        ],
        [
            InlineKeyboardButton("👾Report Errors👾", callback_data="help#subin")
        ]
					
				]
			)
		)
        return
    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    m = await message.reply_text("Fetching data from Instagram🔗")
    chat_id= message.from_user.id
    username=message.text
    if "https://instagram.com/stories/" in username:
        await m.edit("Stories from links are not yet supported🥴\n\nYou can download stories from Username.")
        return

    link = r'^https://www\.instagram\.com/([A-Za-z0-9._]+/)?(p|tv|reel)/([A-Za-z0-9\-_]*)'
    result = re.search(link, username)
    
    if result:
        Post_type = {
            'p': 'POST',
            'tv': 'IGTV',
            'reel': 'REELS'
        }
        supported = Post_type.get(result.group(2))
        if not supported:
            await m.edit('Unsupported Format')
            return
        sent = await m.edit(f'`Fetching {supported} Content from Instagram.`')
        shortcode = result.group(3)
        try:
            userid=str(message.from_user.id)
            dir=f"{userid}/{shortcode}"
            chat_id=message.from_user.id
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", f"-{shortcode}"
                ]
            await download_insta(command, sent, dir)
            await upload(sent, bot, chat_id, dir)
        except Exception as e:
            print(e)
            await bot.send_message(chat_id=message.from_user.id, text=e)
            pass
    elif "https://" in username:
        await m.edit('Unsupported Format')
        return

    else:
        await m.edit(f"Fetching details for <code>@{username}</code>")
        try:
            profile = Profile.from_username(insta.context, username)
            mediacount = profile.mediacount
            name = profile.full_name
            profilepic = profile.profile_pic_url
            igtvcount = profile.igtvcount
            bio = profile.biography
            followers = profile.followers
            following = profile.followees
            is_followed = yes_or_no(profile.followed_by_viewer) 
            is_following = yes_or_no(profile.follows_viewer)
            type = acc_type(profile.is_private)
            if type == "🔒Private🔒" and is_followed == "No":
                print("reached")
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Download Profile Pic", callback_data=f"ppic#{username}"),
                        ]
                    ]
                )
            else:
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
        [
            InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/sthisara_favorites/6")
        ],
        [
            InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites"),
            InlineKeyboardButton("⚡️Disscussion Group⚡️", url="https://t.me/sthisara_favorites_disscussion")
        ],
        [
            InlineKeyboardButton("👾Report Errors👾", callback_data="help#subin")
        ]
                    ]
                )
            await m.delete()
            try:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=profilepic,
                    caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝 **Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n**👤 Is {name} Following You?**: {is_following}\n**👤 Is You Following {name} **: {is_followed}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                    reply_markup=reply_markup
                    )
            except Exception as e:
                print(e)
                await bot.send_message(chat_id, e)
        except Exception as e:
            print(e)
            await m.edit(e)
            pass
