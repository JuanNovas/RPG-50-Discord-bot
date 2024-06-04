def same_user(original_func):
    def decorator(*args, **kwargs):
        global ctx
        if args[0].user != ctx.author:
            return
        result = original_func(*args, **kwargs)
        return result
    return decorator