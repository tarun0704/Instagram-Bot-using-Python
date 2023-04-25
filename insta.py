from instabot import Bot
bot=Bot()
bot.login(username="scps143",password="sujitha@1234")
bot.follow('actorvijay')
bot.upload_photo("C:/Users/prath/OneDrive/Desktop/daisys_flowers_bloom.jpg",caption="flower")
bot.unfollow('actorvijay')
bot.send_message("Flowers are beautiful",["actorvijay","atharvaamurali"])
followers=bot.get_user_followers("scps143")
for follower in followers:
    print(bot.get_user_info(follower))

following=bot.get_user_following("scps143")
for Following in following:
    print(bot.get_user_info(Following))