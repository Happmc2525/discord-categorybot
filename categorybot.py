import discord
from discord import Option
from discord.utils import get

TOKEN = 'ここにbotのトークンを入れる'
DISCORD_SERVER_IDS = ここにサーバーのIDを入れる

client = discord.Bot()

@client.event
async def on_ready():
    print(f"{client.user} コマンド待機中...")

@client.slash_command(description="プライベートカテゴリーを追加するやつ", guild_ids=[DISCORD_SERVER_IDS])
async def pcategory(ctx,name: Option(description="名前を入れてね")
):
    CatName = name
    guild = ctx.guild
    member = ctx.author
    admin_role = get(guild.roles, name=CatName)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    category = await guild.create_category(CatName, overwrites=overwrites)
    await category.create_text_channel("テキストチャンネル", overwrites=overwrites)
    await category.create_voice_channel("ボイスチャンネル", overwrites=overwrites)
    await ctx.respond("プライベートカテゴリーを作成しました")

@client.slash_command(description="公開カテゴリーを追加するやつ", guild_ids=[DISCORD_SERVER_IDS])
async def tuisgoc(ctx,arg: Option(description="名前を入れてね")
):
    OcatName = arg
    Guild = ctx.guild

    Category = await Guild.create_category(OcatName)

    await Category.create_text_channel("テキストチャンネル")
    await Category.create_voice_channel("ボイスチャンネル")
    await ctx.respond("公開カテゴリーを作成しました")

client.run(TOKEN)
