from discord.ext import commands
from enum import Enum

class Status(Enum):
    NOTHING = 1
    WAITING = 2
    PLAYING = 3

class GameStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

    @commands.command()
    async def create(self, ctx):
        """セッションを立てる"""

        if self.bot.game.status == Status.PLAYING:
            await ctx.send('セッション中です')
            return
        if self.bot.game.status == Status.WAITING:
            await ctx.send('セッション準備中')
            return
        
        self.bot.game.status = Status.WAITING
        self.bot.game.channel = ctx.channel
        print('セッションの準備を開始します')
        await ctx.send('セッションの準備を開始します')


    @commands.command()
    async def start(self, ctx):
        """セッション開始"""
        if self.bot.game.status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.game.status == Status.PLAYING:
            await ctx.send('セッション中です')
            return
        self.bot.game.status = Status.PLAYING
        await ctx.send('セッション開始しました')

    
    @commands.command()
    async def close(self, ctx):
        """セッション終了"""
        if self.bot.game.status == Status.NOTHING:
            await ctx.send('セッションが立ってません')
            return
        if self.bot.game.status == Status.WAITING:
            self.bot.game.status = Status.NOTHING
            await ctx.send('セッションをキャンセルします')
            return
        self.bot.game.status = Status.NOTHING
        await ctx.send('セッションを終了します')



def setup(bot):
    bot.add_cog(GameStatus(bot))
