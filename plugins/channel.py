# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    media = getattr(message, message.media.value, None)
    # Check if the media is a document and if it has an APK, ZIP or RAR extension
    if message.media == enums.MessageMediaType.DOCUMENT:
        # Define the MIME types for APK, ZIP, and RAR
        mime_types = {
            'application/vnd.android.package-archive': 'apk',
            'application/zip': 'zip',
            'application/x-rar-compressed': 'rar',
            'application/octet-stream': 'rar'  # This may cover some rar files as well
        }

        if media.mime_type in mime_types:
            media.caption = message.caption
            await save_file(media)
            
