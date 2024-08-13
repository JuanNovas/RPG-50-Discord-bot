from discord import Embed, Color

def get_help_embed(command_id: int):
    if command_id == 0: # Introduction
        embed = Embed(title="✨ **Welcome to RPG 50** ✨", color=Color.blue())
        embed.add_field(name="🛡️ **About**", value="Dive into an epic adventure where you’ll become a hero, battle fierce enemies, and uncover hidden secrets alongside your Discord mates.\n**Your journey awaits—prepare for battle!** ⚔️", inline=False)
        embed.add_field(name="📜 **How to Use**", value="👇 Select the type of commands you want to learn about.\n**Combat** would be a good start. 🗡️", inline=False)
        embed.add_field(name="📖 **Story**", value="This game was created as the **final project** for CS50 Python. 🎓\nThanks for playing. ❤️", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272664340142489600/DALLE_2024-08-12_18.13.40_-_A_fantasy_RPG_style_image_of_a_hero_standing_on_a_mountain_seen_from_the_back_holding_a_sword_and_looking_out_towards_a_distant_castle._The_hero_has.webp?ex=66bbcc87&is=66ba7b07&hm=aa8882e4b47cb20fbadfbad4164037a80bb696bb77776d0e7fba77daaea715a7&")
    
    elif command_id == 1: # Combat
        embed = Embed(title="⚔️ Combat Commands", color=Color.blue())
        embed.add_field(name="/fight", value="Start a battle in the current area. 🗡️", inline=False)
        embed.add_field(name="/dungeon (level 5 required)", value="Enter a dungeon with multiple fights and a final boss. No healing allowed. 🏰", inline=True)
        embed.add_field(name="/raid (level 10 required)", value="Team up with others to take on a tough enemy. 🛡️", inline=False)
        embed.add_field(name="/pvp", value="Challenge another player to a duel. 🤺", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272678835913232457/DALLE_2024-08-12_19.11.14_-_A_fantasy_RPG_style_image_of_a_bow_and_arrow._The_bow_has_a_semi-realistic_appearance_with_a_slightly_curved_wooden_body_and_a_taut_string._The_arrow_.webp?ex=66bbda07&is=66ba8887&hm=d78688518fa8994708e9fcd44dc01a59432539df2147be40dd0bf3d7c0c06721&")
        
    elif command_id == 2: # Stats
        embed = Embed(title="📊 Stats Commands", color=Color.blue())
        embed.add_field(name="/stats", value="View your hero’s stats, gear, and abilities. 🧙‍♂️", inline=False)
        embed.add_field(name="/advancements", value="Check your hero's progress and achievements. 🏆", inline=False)
        embed.add_field(name="/dex", value="See information about encountered enemies. 📚", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272674936749822045/DALLE_2024-08-12_18.55.45_-_A_fantasy_RPG_style_image_of_a_sword_resting_on_a_treasure_chest._The_sword_has_a_semi-realistic_appearance_with_a_sharp_blade_and_ornate_hilt_while_.webp?ex=66bbd666&is=66ba84e6&hm=fad4e8ce1d7ee1d952e519dd7c27831797cdf816b10a730d2e66b62a90111efb&")
        
    elif command_id == 3: # Zones
        embed = Embed(title="🌍 Zones Commands", color=Color.blue())
        embed.add_field(name="/zone", value="Get details about the current area and enemies. 🗺️", inline=False)
        embed.add_field(name="/change_zone", value="Move to a new area based on your level. 🚶‍♂️", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272676356756607036/DALLE_2024-08-12_19.01.27_-_A_fantasy_RPG_style_image_of_a_sky_with_the_sun_visible._The_sky_has_a_semi-realistic_appearance_with_soft_clouds_and_a_warm_glow_from_the_sun_but_no.webp?ex=66bbd7b8&is=66ba8638&hm=6e775e4e6d06eba760add37c811a55c833f443a87aa92c8bc4187f4050fd2b94&")
        
    elif command_id == 4: # Equipment
        embed = Embed(title="🛡️ Equipment Commands", color=Color.blue())
        embed.add_field(name="/inventory", value="View your equipment and stats. 🎒", inline=False)
        embed.add_field(name="/equip_weapon", value="Equip a weapon from your inventory. ⚔️", inline=False)
        embed.add_field(name="/equip_armor", value="Equip armor from your inventory. 🛡️", inline=False)
        embed.add_field(name="/forge", value="Upgrade your equipment at the forge. 🔨", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272676579297988638/DALLE_2024-08-12_19.02.19_-_A_fantasy_RPG_style_image_of_a_shield._The_shield_has_a_semi-realistic_appearance_with_a_slightly_worn_surface_detailed_edges_and_a_central_emblem_.webp?ex=66bbd7ed&is=66ba866d&hm=53fa2fc7a5482ed747e9081349ae3f367fc3108f9571094f72cecb623234c7df&")
        
    elif command_id == 5: # Heroes
        embed = Embed(title="🦸 Heroes Commands", color=Color.blue())
        embed.add_field(name="/new_hero (level 20 required)", value="Create a new hero with a new class. 🌟", inline=False)
        embed.add_field(name="/change_hero", value="Switch to a different hero. 🔄", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272677780353716254/DALLE_2024-08-12_19.07.07_-_A_fantasy_RPG_style_image_of_a_helmet._The_helmet_has_a_semi-realistic_appearance_with_a_slightly_worn_surface_detailed_edges_and_a_visor_but_not_o.webp?ex=66bbd90c&is=66ba878c&hm=2e9750c6e13022050007b0177478abbef26bce94b15a3a90b04e0a7d62f22f72&")
        
    elif command_id == 6: # Commerce
        embed = Embed(title="💰 Commerce Commands", color=Color.blue())
        embed.add_field(name="/shop", value="Open the shop to browse items. 🛒", inline=False)
        embed.add_field(name="/buy [item] [amount]", value="Purchase an item from the shop. 🛍️", inline=False)
        embed.add_field(name="/trade [give_item] [give_amount] [receive_item] [receive_amount]", value="Trade items with another player. 🤝", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/474702643625984021/1272675246918336532/DALLE_2024-08-12_18.57.02_-_A_fantasy_RPG_style_image_of_logs_placed_side_by_side._The_logs_have_a_semi-realistic_appearance_with_rough_bark_and_visible_wood_grain_but_not_overl.webp?ex=66bbd6b0&is=66ba8530&hm=00f16d18e828e6543018165ae80d81276b5644c3d9c946934a8e62bc8dfa4300&")
        
    return embed
