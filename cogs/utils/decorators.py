from discord.ext import commands
from cogs.utils.lock_manager import lock_manager

def same_user(original_func):
    def decorator(*args, **kwargs):
        global ctx
        if args[0].user != ctx.author:
            return
        result = original_func(*args, **kwargs)
        return result
    return decorator

def mana_ability(cost):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self.use_mana(cost):
                return False
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def health_ability(cost):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not self.use_health(cost):
                return False
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def lock_command(*args, **kwargs):
    def decorator(func):
        @commands.command(*args, **kwargs)
        async def wrapper(self, *args, **kwargs):
            if lock_manager.is_locked(args[0].author.id):
                await args[0].send("You are already in a combat.")
                return
            lock_manager.lock(args[0].author.id)
            try:
                return await func(self, *args, **kwargs)
            except:
                lock_manager.unlock(args[0].author.id)
        return wrapper
    return decorator
