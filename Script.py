class script(object):  
    START_TXT = """<b>✨ Hello {user}.

My Name Is {bot}.

I Can Provide Movie For You Just Add Me In Your Group Or Join Our Group.</b>"""
    
    Help_TXT = "Hey {}\nHere Is My Help"

#     ABOUT_TXT = """<b>✯ My Name: {}
# ✯ Network: @TheMovieSharingNetwork
# ✯ My Database: Mongo-DB
# ✯ My Server: Hosted On @StealthRDP.</b>"""
   
#     SOURCE_TXT = """<b>NOTE:</b>
# - Source code here ◉› :<a href=https://github.com/MrMKN/PROFESSOR-BOT>PROFESSOR-BOT</a>

# <b>Dev: <a herf=https://t.me/Mr_MKN>Mr.MKN TG</a></b>"""

    FILE_TXT = """<b>➤ Help for File Store</b>

<i>By Using This Module You Can Store Files In My Database And I Will Give You A Permanent Link To Access The Saved Files. If You Want To Add Files From A Public Channel Send The File Link Only Or You Want To Add Files From A Private Channel You Must Make Me Admin On The Channel To Access Files</i>

<b>⪼ Command & Usage</b>
➪ /link › Reply To Any Media To Get The Link 
➪ /batch › To Create Link For Multiple Media

<b>⪼ EG:</b>
</code>/batch https://t.me/TheMovieSharing/1 https://t.me/TheMovieSharing/10</code>"""
  
    FILTER_TXT = "Select Which One You Want...✨"
    
    GLOBALFILTER_TXT = """<b>Help for Global Filters</b>

<i>Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot Will Respond Whenever A Keyword Is Found The Message</i>

<b>Note:</b>
This Module Only Works For My Admins

<b>Commands And Usage:</b>
• /gfilter - To Add Global Filters
• /gfilters - To View List Of All Global Filters
• /delg - To Delete A Specific Global Filter
• /delallg - To Delete All Global Filters

• /g_filter off Use This Command + on/off In Your Group To Control Global Filter In Your Group"""

    MANUELFILTER_TXT = """<b>Help for Filters</b>

<i>Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot Will Respond Whenever A Keyword Is Found The Message</i>

<b>Note:</b>
1. This Bot Should Have Admin Privilege.
2. Only Admins Can Add Filters In A Chat.
3. Alert Buttons Have A Limit Of 64 Characters.

<b>Commands And Usage:</b>
• /filter - Add A Filter In Chat
• /filters - List All The Filters Of A Chat
• /del - Delete A Specific Filter In Chat
• /delall - Delete The Whole Filters In A Chat (Chat Owner Only)

• /g_filter off Use This Command + on/off In Your Group To Control Global Filter In Your Group"""

    BUTTON_TXT = """<b>Help for Buttons</b>

<i>This Bot Supports Both URL And Alert Inline Buttons.</i>

<b>Note:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. This Bot Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed As Markdown Format

<b>URL Buttons:</b>
[Button Text](buttonurl:xxxxxxxxxxxx)

<b>Alert Buttons:</b>
[Button Text](buttonalert:This Is An Alert Message)"""

    AUTOFILTER_TXT = """<b>Help for AutoFilter</b>

<i>Auto Filter Is The Feature To Filter & Save The Files Automatically From Channel To Group. You Can Use The Following Command To on/off The AutoFilter In Your Group</i>

• /autofilter on - auto filter enable in your chat
• /autofilter off - auto filter disable in your chat

<Ob>Other Commands:</b>
• /set_template - Set IMDb Template For Your Group 
• /get_template - Get Current IMDb Template For Your Group"""

    CONNECTION_TXT = """<b>Help for Connections</b>

<i> Used To Connect Bot To Pm For Managing Filters. It Helps To Avoid Spamming In Groups</i>

<b>Note:</b>
• Only Admins Can Add A Connection.
• Send /connect For Connecting Me To Ur Pm

<Cb>Commands And Usage:</b>
• /connect - Connect A Particular Chat To Your Pm
• /disconnect - Disconnect from A Chat
• /connections - List All Your Connections"""

    ADMIN_TXT = """<b>Help for Admins</b>
    
<i>This Module Only Works For My Admins</i>

<b>Command & Usage</b>
• /logs - To Get The Recent Errors
• /delete - To Delete A Specific File From DB
• /deleteall - To Delete All Files From DB
• /users - To Get List Of My Users And Ids
• /chats - To Get List Of My Chats And Ids
• /channel - To Get List Of Total Connected Channels
• /broadcast - To Broadcast A Message To All Users
• /group_broadcast - To Broadcast A Message To All Connected Groups
• /leave  - With Chat Id To Leave From A Chat
• /disable  - With Chat Id To Disable A Chat
• /invite - With Chat Id To Get The Invite Link Of Any Chat Where The Bot Is Admin
• /ban_user  - With Id To Ban A User
• /unban_user  - With Id To Unban A User
• /restart - To Restart The Bot
• /clear_junk - Clear All Delete Account & Blocked Account In Database
• /clear_junk_group - Clear Add Removed Group Or Deactivated Groups On Db"""


    STATUS_TXT = """<b>◉ total files: <code>{}</code>
◉ total users: <code>{}</code>  
◉ total chats: <code>{}</code>
◉ used db size: <code>{}</code>
◉ free db size: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#new_group

◉ group: {a}
◉ g-id: <code>{b}</code>
◉ link: @{c}
◉ members: <code>{d}</code>
◉ added by: {e}

◉ by: @{f}</b>"""
  
    LOG_TEXT_P = """#new_user
    
◉ user-id: <code>{}</code>
◉ acc-name: {}
◉ username: @{}

◉ by: @{}</b>"""
  
    GROUPMANAGER_TXT = """<b>Help for GroupManager</b>

<i>This Is Help Of Your Group Managing. This Will Work Only For Group admins</i>

<b>Command & Usage:</b>
• /inkick - Command With Required Arguments And I Will Kick Members From Group.
• /instatus - To Check Current Status Of Chat Member From Group.
• /dkick - To Kick Deleted Accounts
• /ban - To Ban A User Form The Group
• /unban - Unban The Banned User
• /tban - Temporary Ban A User
• /mute - To Mute A User
• /unmute - To Unmute The Muted User
• /tmute - With Value To Mute Up To Particular Time Eg: <code>/tmute 2h</code> To Mute 2Hour Values Is (m/h/d)
• /pin - To Pin A Message On Your Chat
• /unpin - To Unpin The Message On Your Chat
• /purge - Delete All Messages From The Replied To Message, To The Current Message """

    EXTRAMOD_TXT = """<b>Help for Extra Module</b>

<i>Just Send Any Image To Edit Image ✨</i>

<b>Commands & Usage:</b>
• /id - Get Id Of A Specified User
• /info  - Get Information About A User
• /imdb  - Get The Film Information From IMDb Source
• /paste [text] - Paste The Given Text On Pasty
• /tts [text] - Convert Text To Speech
• /telegraph - Send Me This Command Reply With Picture Or Vide Under (5mb)
• /json - Reply With Any Message To Get Message Info (usefull for group)
• /written - Reply With Text To Get File (usefull for coders)
• /carbon - Reply With Text To Get Carbonated Image
• /font [text] - To Change Your Text Fonts To Fancy Font
• /share - Reply With Text To Get Text Sharable Link
• /song [name] - To Search The Song In YouTube
• /video [link] - To Download The YouTube Video"""    
    
    CREATOR_REQUIRED = "❗<b>You Have To Be The Group Creator To Do That</b>"
      
    INPUT_REQUIRED = "❗ **Argument Required**"
      
    KICKED = "✔️ Successfully Kicked {} Members According To The Arguments Provided"
      
    START_KICK = "Removing Inactive Members This May Take A While"
      
    ADMIN_REQUIRED = "❗<b>I am Not Admin In This Chat So Please Add Me Again With All Admin Permission</b>"
      
    DKICK = "✔️ Kicked {} Deleted Accounts Successfully"
      
    FETCHING_INFO = "<b>Wait I Will Take The All Info</b>"
   
    SERVER_STATS = """Server Stats:
 
Uptime: {}
CPU Usage: {}%
RAM Usage: {}%
Total Disk: {}
Used Disk: {} ({}%)
Free Disk: {}"""
    
    BUTTON_LOCK_TEXT = "Hey {query}\nThis Is Not For You. Search Your Self"
   
    FORCE_SUB_TEXT = "Sorry Bro Your Not Joined My Channel So Please Click Join Button To Join My Channel And Try Again"
   
    WELCOM_TEXT = """Hey {user} 💞

Welcome to {chat}.

Share & support, request you wanted movies"""
  
    IMDB_TEMPLATE = """<b>Query: {query}</b>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a>/10"""
