#from wxpy import api
#from wxpy import *
import wxpy.api.bot as bot
import wxpy.utils as utils


bot = bot.Bot()

friends_list =bot.friends()
Amy = friends_list.search("Miya")[0]
print (Amy)
utils.embed()
