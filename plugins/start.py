from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)

async def start(client, message):

    # return

    joinButton = InlineKeyboardMarkup([

        [InlineKeyboardButton(

            "✈ Support Me on Youtube ✈", url="https://youtube.com/c/HKNPlayz")]

    ])

    welcomed = f"""ʜᴇʏ {message.from_user.first_name}
ɪᴀᴍ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ..
sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴜʀʟ(ʟɪɴᴋ) ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ..

➪ Bot Name : HK YT BOT
➪ Author : [HK MIRROR](https://telegram.me/mirrorgrou)
➪ Mirror Group : [Join](https://telegram.me/mirrorgro)
➪ Language : Python
➪ License Type : GNU(GPL)"""

    await message.reply_text(welcomed, reply_markup=joinButton)

    raise StopPropagation

