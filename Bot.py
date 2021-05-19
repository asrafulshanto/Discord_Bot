import discord
import random 
from discord.ext import commands


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
	print('Bot is ready.')
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Google Hacks!')) #This code for status and activity of bot .
	


@client.command() #this code for ping test. Type (.ping) and it wll show your client latency .
async def ping(ctx):
	await ctx.send(f'ping! {round(client.latency * 1000)}ms')




@client.command(aliases=['8ball', 'test']) #this code is for using question and answer of random question. Just type (.8ball/.test) and your question and it will answer your ques randomly.
async def _8ball(ctx, *, question):
	responses =["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful."]	
	await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}') 

#---------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Invalid command used.')

@client.command() 
#@commands.has_permissions(manage_messages=True) #This code for permited person to use this command. if u need this just delete '#' save and run it and give people to manage message for use this command.
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit=amount)                       #this command for deleting messege from channel. Just type (.clear _anything_like_1,2,4 ) and it will delete specifice message .


@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please specify an amount of message to delete.')


#----------------------------------------------------------------------------------------------------------------------------------

@client.command() #this code for kick someone by using bot. Type (.kick _username type_reason_anything_u_want) and it will kick member from server.
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)


@client.command() #this code for ban someone by using bot. Type (.ban _username type_reason_anything_u_want) and it will kick member from server.
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')



@client.command() #this code for unban member from ban list. Type (.uban _username) and it will unban member 
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')


	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return










client.run('Paste Your Token Here') #PASTE YOUR TOKEN HERE
