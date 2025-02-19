import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

message_count = {}  # Добавьте это для хранения количества сообщений пользователей

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Игнорируем сообщения от других ботов

    # Получим ID пользователя
    user_id = str(message.author.id)

    # Инициализируем счетчик сообщений пользователя, если его еще нет в словаре
    if user_id not in message_count:
        message_count[user_id] = 0

    # Увеличиваем счетчик сообщений пользователя
    message_count[user_id] += 1

    # Проверяем, достиг ли пользователь определенного уровня
    levels = [20, 40, 60, 100, 170, 280, 390, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700]

    for level in levels:
        if message_count[user_id] == level:
            await message.channel.send(f"{message.author.mention} {level//20}-Деңгейге жетті!")

    await bot.process_commands(message)

# Запускаем бота с его токеном
bot.run('')
