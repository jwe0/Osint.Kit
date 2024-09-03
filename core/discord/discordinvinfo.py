import tls_client
def DiscordInvInfo(args):
    session = tls_client.Session()
    invite = args.get("invite", "")

    if not invite:
        return {"message" : "error", "info" : "You did not supply invite information"}

    api = "https://discord.com/api/v10/invites/{}".format(invite)

    r = session.get(api)
    if r.status_code == 200:
        decode  = r.json()
        guild   = decode.get("guild")
        channel = decode.get("channel")
        log = {
            "type" : decode.get("type"),
            "code" : decode.get("code"),
            "expires_at" : decode.get("expires_at"),
            "flags" : decode.get("flags"),
            "guild_id" : guild.get("id"),
            "guild_name" : guild.get("name"),
            "splash" : guild.get("splash"),
            "banner" : guild.get("banner"),
            "icon" : guild.get("icon"),
            "description" : guild.get("description"),
            "verification_level" : guild.get("verification_level"),
            "vanity_url_code" : guild.get("vanity_url_code"),
            "nsfw_level" : guild.get("nsfw_level"),
            "nsfw" : guild.get("nsfw"),
            "boosted" : True if guild.get("premium_subscription_count") > 0 else False,
            "boosts" : guild.get("premium_subscription_count"),
            "channel_id" : channel.get("id"),
            "channel_name" : channel.get("name"),
            "channel_type" : channel.get("type"),
        }
        return {"message" : "success", "info" : log}
    else:
        return {"message" : "error", "info" : f"{str(r.status_code)} : {r.text if r.text else 'Unknown error'}"}