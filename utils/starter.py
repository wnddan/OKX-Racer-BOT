from asyncio import sleep
from random import uniform
from time import time
from datetime import datetime, timedelta, timezone
import aiohttp
from aiocfscrape import CloudflareScraper
from .agents import generate_random_user_agent
import math
from data import config
from utils.blum import BlumBot
from utils.core import logger
from utils.helper import format_duration
import asyncio

async def start(thread: int, account: str, proxy: [str, None]):
    async with CloudflareScraper(headers={'User-Agent': generate_random_user_agent(device_type='android',
                                                                                    browser_type='chrome')},
                                    timeout=aiohttp.ClientTimeout(total=60)) as session:
        try:
            blum = BlumBot(account=account, thread=thread, session=session, proxy=proxy)
            await sleep(uniform(*config.DELAYS['ACCOUNT']))
            tg_web_data= await blum.get_tg_web_data()
            with open("data.txt","a") as f:
                f.write(tg_web_data)
                f.write("\n")
                
        except Exception as e:
            logger.error(account)
            logger.error(e)


