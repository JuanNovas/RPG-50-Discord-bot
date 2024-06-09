from discord import app_commands
from discord.ext import commands
from cogs.utils.lock_manager import lock_manager
from typing import Any

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


def lock_command(func):
    async def wrapper(*args, **kwargs):
        if lock_manager.is_locked(args[1].user.id):
            await args[1].response.send_message("You are already in a combat.")
            return
        lock_manager.lock(args[1].user.id)
        try:
            return await func(*args, **kwargs)
        except:
            lock_manager.unlock(args[1].user.id)
    return wrapper
