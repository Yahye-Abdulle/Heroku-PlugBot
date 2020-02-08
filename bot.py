import backend as be
import sys
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import smtplib
import os
import discord
from collections import defaultdict
from datetime import datetime

bot = commands.Bot(command_prefix='!')

points = defaultdict(int)

def submit_details(ctx,emailTarget, emailFreq):
    
    server= "gmail"
    user= "mobilegameratyt@gmail.com"
    passwd= "Yahyeabdulle94"
    to= emailTarget
    subject= "You have won a package deal from O2!"
    body= "Click here to claim Unlimited Text, Call and Data"
    
    
    if len(server)==0 or len(user)==0 or len(passwd)==0 or len(to)==0 or len(subject)==0 or len(body)==0:
        print("Please Fill ot all the Details,Correctly")
    else:
        try :
            if int(emailFreq) == 1:
                freq= 75
            elif int(emailFreq) == 2:
                freq= 40
            else:
                freq = 25
            print("Details submitted Successfully")
            be.bomb_email(server,user,passwd,to,subject,body,freq)
        except ValueError:
            print("Please Provide Frequency in Natural Numbers")
'''            
@bot.command(pass_context=True)
async def ar(ctx, role: discord.Role, member: discord.Member=None):
    member = member
    await bot.add_roles(member, role)
'''

@bot.command(pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def give(ctx, member: discord.Member, arg):
    points[member.id] += int(arg)
    await ctx.send("{} now has {} points".format(member.mention, points[member.id]))

@bot.command(pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def min(ctx, member: discord.Member, arg):
    points[member.id] -= int(arg)
    await ctx.send("{} now has {} points".format(member.mention, points[member.id]))

@bot.command(pass_context=True)
async def balance(ctx, member: discord.Member):
    await ctx.send("{} has {} points remaining".format(member.mention, points[member.id]))

@bot.command()
async def bomb(ctx, member: discord.Member,*arg):
    startTime = datetime.now()
    if points[member.id] > 0:
        points[member.id] -= 1
        emailTarget = arg[0]
        #emailDomain = arg[1]
        emailFreq = arg[1]
        submit_details(ctx,emailTarget, emailFreq)
        await ctx.send("Task submitted by {} is completed, took {}".format(member.mention, datetime.now() - startTime))
    else:
        await ctx.send("Please purchase more credits!")

bot.run(TOKEN)
