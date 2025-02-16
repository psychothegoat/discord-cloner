from nexxclone import Clone
import discord

def main():
    # Get token from environment variables
    import os
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: Please set the DISCORD_TOKEN in Secrets")
        exit(1)
    input_guild_id = input('Enter source guild ID: ')
    output_guild_id = input('Enter destination guild ID: ')

    # Initialize the Discord client
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"Logged in as: {client.user}")
        print("Cloning Server")

        # Get source and destination guilds
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))

        # Prompt user for cloning options
        all_in_one = input('Do you want to perform an all-in-one clone? [y/n] > ').lower() == 'y'

        if all_in_one:
            await Clone.all(guild_from, guild_to)
        else:
            # Perform individual cloning steps
            await Clone.roledelete(guild_to)
            await Clone.chdelete(guild_to)
            await Clone.rolecreate(guild_to, guild_from)
            await Clone.catcreate(guild_to, guild_from)
            await Clone.chcreate(guild_to, guild_from)
            await Clone.guedit(guild_to, guild_from)

        clone_template = input('Do you want to clone the template of the server? [y/n] > ').lower() == 'y'
        if clone_template:
            await Clone.gutemplate(guild_to)

        print("Cloning completed. Exiting in 5 seconds.")
        await asyncio.sleep(5)
        exit()

    # Run the bot with the provided token
    client.run(token, bot=False)

if __name__ == "__main__":
    main()
