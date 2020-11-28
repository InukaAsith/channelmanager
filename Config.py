import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Channel Manageer Robot**\n__ඔයාගෙ ගෲප් එකේ මෙම්බර්ස්ල Channel එකක් හෝ කිහිපයක් Subscribe කරනකන් Message දාන එක නවත්තන්න මට පුලූවන්.\nසාමාජිකයන් ඔබේ Channel  එකට සම්බන්ධ නොවූයේ නම් මම ඔවුන්ව නිශ්ශබ්ද කර channel එකට සම්බන්ධ වන ලෙස පවසන්න සහ බොත්තමක් එබීමෙන් ඔවුන්ව නිශ්ශබ්ද කරන්න මට පුලුවන්.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @InukaASiTH**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__ඔයාගෙ ගෲප් එකේ මෙම්බර්ස්ල Channel එකක් හෝ කිහිපයක් Subscribe කරනකන් Message දාන එක නවත්තන්න මට පුලූවන්.\nLearn more at /help__"
