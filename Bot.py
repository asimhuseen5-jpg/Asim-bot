import os
import discord
from discord.ext import commands

# إعداد الصلاحيات والبادئة
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح كـ {bot.user}")


# 1. أمر الترحيب السوداني
@bot.command()
async def حبابك(ctx):
    await ctx.send("حبابك ألف! أهلاً بيك في السيرفر، أنورت الدار! 🇸🇩✨")


# 2. أمر النكتة السودانية
@bot.command()
async def نكتة(ctx):
    await ctx.send(
        "مسطول سألوه: الفرق شنو بين التلفزيون والراديو؟ قال ليهم: التلفزيون في زول بيكلمك وش وش، أما الراديو بيكلمك وهو زعلان ومقفي! 😂"
    )


# 3. أمر مثل سوداني
@bot.command()
async def مثل(ctx):
    await ctx.send("من أمثالنا السودانية: **«الجاب جابو والما جاب خلو»** 🇸🇩")


# تشغيل البوت باستخدام التوكن من متغيرات البيئة (الأكثر أماناً)
TOKEN = os.environ.get("DISCORD_TOKEN")

# إذا أردت تجربة التوكن مباشرة (ضع التوكن الخاص بك بين التنصيص أسفله)
# TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"

if TOKEN:
    bot.run(TOKEN)
else:
    print("خطأ: لم يتم العثور على التوكن!")
