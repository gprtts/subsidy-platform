import os
import asyncio
from telegram import Bot
from tg_bot.alerts import get_alert_users, get_new_programs

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

LAST_ID_FILE = "last_program_id.txt"


def load_last_id():
    try:
        with open(LAST_ID_FILE, "r") as f:
            return int(f.read())
    except:
        return 0


def save_last_id(pid: int):
    with open(LAST_ID_FILE, "w") as f:
        f.write(str(pid))


async def run():
    last_id = load_last_id()
    programs = get_new_programs(last_id)
    if not programs:
        return

    users = get_alert_users()
    for pid, title in programs:
        for tg_id, *_ in users:
            await bot.send_message(
                chat_id=tg_id,
                text=f"🆕 Новая программа:\n\n{title}",
            )
        last_id = max(last_id, pid)

    save_last_id(last_id)


asyncio.run(run())
