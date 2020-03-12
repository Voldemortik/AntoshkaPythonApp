import discord
from discord.exe import commands
TOKEN = 'NjcwMDE1NzM4NjQ3NDEyNzM2.XitUxA.OWovLdjlQ-JIVR2IZPsyspXsAXE'
bot = commands.Bot(command_prefix = '!')#Иниацилизация бота 
@bot.commands(pass_context=True)
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент
bot.run(TOKEN)