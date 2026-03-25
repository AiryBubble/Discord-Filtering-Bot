import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

BANNED_USER_IDS = {1286942627991781480, 987654321098765432}

@bot.event
async def on_member_join(member: discord.Member):
    if member.id in BANNED_USER_IDS:
        try:
            await member.guild.ban(user=member, reason="地球温暖化を阻止するため")
            print(f"[BAN] {member} ({member.id}) をBanしました。")
        except discord.Forbidden:
            print(f"[ERROR] ボットに {member.guild.name} でBAN権限がありません。")
        except discord.HTTPException as e:
            print(f"[ERROR] {member} のBanに失敗: {e}")
        except Exception as e:
            print(f"[ERROR] 予期しないエラー: {e}")

@bot.event
async def on_ready():
    print(f"Botが起動しました: {bot.user} (ID: {bot.user.id})")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
