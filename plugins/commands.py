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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
import asyncio
import sys
import os

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HOME_TEXT_OWNER=Config.HOME_TEXT_OWNER
HELP=Config.HELP


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
						InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites")
					],
                    [
                        InlineKeyboardButton("👾Report Errors👾", url="https://t.me/sthisara_favorites_disscussion"),
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
						InlineKeyboardButton("⚡️Updates Channel⚡️", url="https://t.me/sthisara_favorites")

                    ]
					
				]
			)
		)
	else:
		await cmd.reply_text(
			HOME_TEXT_OWNER.format(cmd.from_user.first_name, cmd.from_user.id), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
						InlineKeyboardButton("𝓔𝓹𝓵𝓲𝓼𝓸𝓷", url="https://t.me/eplison_bot"),
					],
                    [
                        InlineKeyboardButton("👾Report Errors👾", url=" https://t.me/sthisara_favorites_discussion")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
						InlineKeyboardButton("𝓔𝓹𝓵𝓲𝓼𝓸𝓷", url="https://t.me/eplison_bot")

                    ]
					
				]
			)
		)


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
	await cmd.reply_text(
		HELP,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
						InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
						InlineKeyboardButton("𝓔𝓹𝓵𝓲𝓼𝓸𝓷", url="https://t.me/eplison_bot"),
					],
                    [
                        InlineKeyboardButton("👾Report Errors👾", url=" https://t.me/sthisara_favorites_discussion")
					
				],
				[
					InlineKeyboardButton("λlρhα Mυsιc Plαγεr", url="https://t.me/st_alpha_bot"),
					InlineKeyboardButton("𝓔𝓹𝓵𝓲𝓼𝓸𝓷", url="https://t.me/eplison_bot")
				]
			]
			)
		)

@Client.on_message(filters.command("restart") & filters.private)
async def stop(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER), 
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("💃🏼 Developer 💃🏼", url='https://t.me/sthisara'),
						InlineKeyboardButton("𝓔𝓹𝓵𝓲𝓼𝓸𝓷", url="https://t.me/eplison_bot"),
					],
                    [
                        InlineKeyboardButton("👾Report Errors👾", url=" https://t.me/sthisara_favorites_discussion")
