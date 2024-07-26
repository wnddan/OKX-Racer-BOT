import random
from utils.core import logger
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestWebView,RequestAppWebView
import asyncio
from urllib.parse import unquote
from data import config
import urllib.parse
import json
import jwt
import requests
import cloudscraper
from pyrogram.raw.types import InputBotAppShortName
class BlumBot:
    def __init__(self, thread, account, session, proxy):
        """
        Initialize the BlumBot with thread id, account name, and optional proxy.
        """
        self.proxy = f"socks5://{proxy}" if proxy is not None else None
        self.thread = thread
        logger.info(self.proxy)
        if proxy:
            parts = proxy.split(":")
            proxy = {
                "scheme": "socks5",
                "hostname": parts[0] if len(parts) == 2 else parts[1].split('@')[1],
                "port": int(parts[2]) if len(parts) == 3 else int(parts[1]),
                "username": parts[0] if len(parts) == 3 else "",
                "password": parts[1].split('@')[0] if len(parts) == 3 else ""
            }
            logger.info(proxy)
        self.client = Client(name=account, api_id=config.API_ID, api_hash=config.API_HASH, workdir=config.WORKDIR,
                             proxy=proxy)
        self.session = session
        self.refresh_token = ''
        self.user_id= ''
        self.address = ''

    async def get_tg_web_data(self):
        """
        Get the Telegram web data needed for login.
        """
        await self.client.connect()
        start_command_found = False

        async for message in self.client.get_chat_history('OKX_official_bot'):
            if (message.text and message.text.startswith('/start')) or (message.caption and message.caption.startswith('/start')):
                start_command_found = True
                break
        if not start_command_found:
            await self.client.send_message("OKX_official_bot", "/start linkCode_90905611")#ref_xavygoyfrvstgwv7gptymu
        web_view = await self.client.invoke(RequestWebView(
            peer=await self.client.resolve_peer('OKX_official_bot'),
            bot=await self.client.resolve_peer('OKX_official_bot'),
            platform='android',
            from_bot_menu=True,
        url='https://www.okx.com/mini-app/racer',
        start_param="linkCode_90905611"
    ))
        auth_url = web_view.url
        logger.info(auth_url)
        await self.client.disconnect()
        return unquote(string=auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0])
#https://tonstation.app/app/#tgWebAppData=query_id%3DAAHRUvoKAwAAANFS-grYNDJ_%26user%3D%257B%2522id%2522%253A6626628305%252C%2522first_name%2522%253A%2522Gssg%2522%252C%2522last_name%2522%253A%2522777%2522%252C%2522username%2522%253A%2522goonsomeway%2522%252C%2522language_code%2522%253A%2522zh-hant%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1721827219%26hash%3D6cf409d5a5e11989d75aa775763695a86667e79173f424df78e164d5d50d65a6&tgWebAppVersion=6.7&tgWebAppPlatform=android&tgWebAppSideMenuUnavail=1
