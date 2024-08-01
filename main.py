#Caleb Mathurin 08/19/2020-09/03/2021 - imports
import tweepy
import time
from random import randint
#from keep_alive import keep_alive
import datetime
import pytz
import random
from phrase_constructor import phrase_constructor
from replit import db

#Caleb Mathurin 08/19/2020 - keys (generated 11/15/2023)
CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_KEY = "XXXX-XXXX"
ACCESS_SECRET = "XXXX"

#Caleb Mathurin 03/27/2024 - Authenticate to "X" (Elon's Twitter)
client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY, access_token_secret=ACCESS_SECRET)

#Caleb Mathurin 09/03/2021-01/22/2022 - the screen names of users who will be replied to
screen_name_1 = "vgdunkey"
screen_name_2 = "NintendoAmerica"
screen_name_3 = "NintendoEurope"
screen_name_4 = "CrystalDynamics"
screen_name_5 = "ScottTheWoz"
screen_name_6 = "PlayStation"
screen_name_7 = "realDonaldTrump"
screen_name_8 = "kirawontmiss"

#Caleb Mathurin 09/03/2021 - the number of tweets to be retrieved from each person
count = 1

#try:
		#api.verify_credentials()
		#print("Authentication OK")
#except:
		#print("Error during authentication")

#Caleb Mathurin 08/11/2021 - defines the function tweets(), which just pulls phrases from phrase_constructor.py as well as having the milestone counter and birthday announcer because they should only be tweets
def tweets():
	phrase = phrase_constructor()
	client.create_tweet(text=phrase)

"""
	#Caleb Mathurin 07/11/2022 - creates replit database that keeps track of which milestones have been cleared
	db["cleared_milestones"] = db["cleared_milestones"]
	
	#Caleb Mathurin 07/11/2022 - acquires GexPhraseBot's follower count
	gex_user = api.get_user("GexPhraseBot")
	gex_followers_count = gex_user.followers_count
	
	#Caleb Mathurin 07/11/2022 - tracks milestones
	if gex_followers_count >= 10 and "10" not in db["cleared_milestones"]:
		db["cleared_milestones"] = "10" + "\n"
		milestone_number = "10"
	if gex_followers_count >= 50 and "50" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "50" + "\n"
		milestone_number = "50"
	if gex_followers_count >= 100 and "100" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "100" + "\n"
		milestone_number = "100"
	if gex_followers_count >= 500 and "500" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "500" + "\n"
		milestone_number = "500"
	if gex_followers_count >= 1000 and "1,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "1,000" + "\n"
		milestone_number = "1,000"
	if gex_followers_count >= 2000 and "2,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "2,000" + "\n"
		milestone_number = "2,000"
	if gex_followers_count >= 3000 and "3,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "3,000" + "\n"
		milestone_number = "3,000"
	if gex_followers_count >= 4000 and "4,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "4,000" + "\n"
		milestone_number = "4,000"
	if gex_followers_count >= 5000 and "5,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "5,000" + "\n"
		milestone_number = "5,000"
	if gex_followers_count >= 6000 and "6,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "6,000" + "\n"
		milestone_number = "6,000"
	if gex_followers_count >= 7000 and "7,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "7,000" + "\n"
		milestone_number = "7,000"
	if gex_followers_count >= 8000 and "8,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "8,000" + "\n"
		milestone_number = "8,000"
	if gex_followers_count >= 9000 and "9,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "9,000" + "\n"
		milestone_number = "9,000"
	if gex_followers_count >= 10000 and "10,000" not in db["cleared_milestones"]:
		db["cleared_milestones"] = db["cleared_milestones"] + "10,000" + "\n"
		milestone_number = "10,000"
		
	try:
		milestones_phrase_list = ["I haven't seen something this Gextraordinary since the time I hit " + milestone_number + " followers on Twitter!", "I haven't seen something this Gexquisite since the time I hit " + milestone_number + " followers on Twitter!", "I haven't felt this Gexcited since the time I hit " + milestone_number + " followers on Twitter!", "I haven't felt this Gexcellent since the time I hit " + milestone_number + " followers on Twitter!"]

		phrase = (random.choice(milestones_phrase_list))
		
	except:
		pass
		
	#Caleb Mathurin 07/11/2022 - Makes Gex announce it's his birthday at noon of August 19.
	if int((current_date.strftime("%m"))) == 8 and int((current_date.strftime("%d"))) == 19 and int((current_date.strftime("%H"))) == 12 and int((current_date.strftime("%M"))) == 0 and int((current_date.strftime("%S"))) == 0:
		phrase = "Well, Happy Birthday to me!"
"""  
	#move client.create_tweet(phrase) here when above code is fixed
	#print(phrase)
"""
#Caleb Mathurin 09/03/2021-11/25/2022 - defines the function replies(), which replies to specific users
def replies():
	global tweet_1
	global tweet_2
	global tweet_3
	global tweet_4
	global tweet_5
	global tweet_6
	global tweet_7
	global tweet_8
	
	tweets_1 = api.user_timeline(screen_name_1, count = count, tweet_mode = "extended")
	tweets_2 = api.user_timeline(screen_name_2, count = count, tweet_mode = "extended")
	tweets_3 = api.user_timeline(screen_name_3, count = count, tweet_mode = "extended")
	tweets_4 = api.user_timeline(screen_name_4, count = count, tweet_mode = "extended")
	tweets_5 = api.user_timeline(screen_name_5, count = count, tweet_mode = "extended")
	tweets_6 = api.user_timeline(screen_name_6, count = count, tweet_mode = "extended")
	tweets_7 = api.user_timeline(screen_name_7, count = count, tweet_mode = "extended")
	tweets_8 = api.user_timeline(screen_name_8, count = count, tweet_mode = "extended")
	
	#Caleb Mathurin 04/11/2021-11/25/2022 - prints latest statuses (Tweets) from specific users
	for tweet_1 in tweets_1:
		tweet_1 = tweet_1  
		#print("@" + screen_name_1 + " - " + tweet_1.full_text + " - " + str(tweet_1.id) + "\n\n")
	for tweet_2 in tweets_2:
		tweet_2 = tweet_2  
		#print("@" + screen_name_2 + " - " + tweet_2.full_text + " - " + str(tweet_2.id) + "\n\n")
	for tweet_3 in tweets_3:
		tweet_3 = tweet_3  
		#print("@" + screen_name_3 + " - " + tweet_3.full_text + " - " + str(tweet_3.id) + "\n\n")
	for tweet_4 in tweets_4:
		tweet_4 = tweet_4  
		#print("@" + screen_name_4 + " - " + tweet_4.full_text + " - " + str(tweet_4.id) + "\n\n")
	for tweet_5 in tweets_5:
		tweet_5 = tweet_5
		#print("@" + screen_name_5 + " - " + tweet_5.full_text + " - " + str(tweet_5.id) + "\n\n")
	for tweet_6 in tweets_6:
		tweet_6 = tweet_6
		#print("@" + screen_name_6 + " - " + tweet_6.full_text + " - " + str(tweet_6.id) + "\n\n")
	for tweet_7 in tweets_7:
		tweet_7 = tweet_7
		#print("@" + screen_name_7 + " - " + tweet_7.full_text + " - " + str(tweet_7.id) + "\n\n")
	for tweet_8 in tweets_8:
		tweet_8 = tweet_8
		#print("@" + screen_name_8 + " - " + tweet_8.full_text + " - " + str(tweet_8.id) + "\n\n")

	#Caleb Mathurin 09/03/2021 - Creates a replit database that reads the ids of the last tweet from all the specified users
	db["stored_tweet_ids"] = db["stored_tweet_ids"]

	#Caleb Mathurin 09/03/2021-11/25/2022 - Decides whether or not to reply to users based on if the tweet id of their last tweet is in the database and if the tweet is a retweet
	if str(tweet_1.id) not in db["stored_tweet_ids"] and not hasattr(tweet_1, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_1 + " " + phrase, tweet_1.id)
		#print("@" + screen_name_1 + " " + phrase, tweet_1.id)
	else:
		pass

	if str(tweet_2.id) not in db["stored_tweet_ids"] and not hasattr(tweet_2, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_2 + " " + phrase, tweet_2.id)
		#print("@" + screen_name_2 + " " + phrase, tweet_2.id)
	else:
		pass

	if str(tweet_3.id) not in db["stored_tweet_ids"] and not hasattr(tweet_3, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_3 + " " + phrase, tweet_3.id)
		#print("@" + screen_name_3 + " " + phrase, tweet_3.id)
	else:
		pass

	if str(tweet_4.id) not in db["stored_tweet_ids"] and not hasattr(tweet_4, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_4 + " " + phrase, tweet_4.id)
		#print("@" + screen_name_4 + " " + phrase, tweet_4.id)
	else:
		pass

	if str(tweet_5.id) not in db["stored_tweet_ids"] and not hasattr(tweet_5, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_5 + " " + phrase, tweet_5.id)
		#print("@" + screen_name_5 + " " + phrase, tweet_5.id)
	else:
		pass

	if str(tweet_6.id) not in db["stored_tweet_ids"] and not hasattr(tweet_6, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_6 + " " + phrase, tweet_6.id)
		#print("@" + screen_name_6 + " " + phrase, tweet_6.id)
	else:
		pass

	if str(tweet_7.id) not in db["stored_tweet_ids"] and not hasattr(tweet_7, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_7 + " " + phrase, tweet_7.id)
		#print("@" + screen_name_7 + " " + phrase, tweet_7.id)
	else:
		pass

	if str(tweet_8.id) not in db["stored_tweet_ids"] and not hasattr(tweet_8, 'retweeted_status'):
		phrase = phrase_constructor()
		api.update_status("@" + screen_name_8 + " " + phrase, tweet_8.id)
		#print("@" + screen_name_8 + " " + phrase, tweet_8.id)
	else:
		pass

	#Caleb Mathurin 09/03/2021-11/25/2022 - stores the ids of all Tweets seen into the database
	db["stored_tweet_ids"] = str(tweet_1.id) + "\n" + str(tweet_2.id) + "\n" + str(tweet_3.id) + "\n" + str(tweet_4.id) + "\n" + str(tweet_5.id) + "\n" + str(tweet_6.id) + "\n" + str(tweet_7.id) + "\n" + str(tweet_8.id)
"""
"""
#Caleb Mathurin 12/05/2021 - defines the function profile(), which changes Gex's profile picture throughout the year
def profile():

	#Caleb Mathurin 12/05/2021 - creates a Replit database that will hold the status (type) of pfp Gex currently has
	db["profile_status"] = db["profile_status"]

	#Caleb Mathurin 12/05/2021 - if it is a certain month of the year and the pfp/name is not the correct one, the pfp is changed accordingly
	if int((current_date.strftime("%m"))) not in [10, 12] and "reg" not in db["profile_status"] or int((current_date.strftime("%m"))) != 8 and int((current_date.strftime("%d"))) != 19 and "reg" not in db["profile_status"]:
		api.update_profile_image("gexphrasebot_reg_pfp.png")
		api.update_profile(name = "Gex")
		db["profile_status"] = "reg"
		
	if int((current_date.strftime("%m"))) == 10 and "oct" not in db["profile_status"]:
		api.update_profile_image("gexphrasebot_oct_pfp.png")
		api.update_profile(name = "Gex 🎃")
		db["profile_status"] = "oct"

	if int((current_date.strftime("%m"))) == 12 and "dec" not in db["profile_status"]:
		api.update_profile_image("gexphrasebot_dec_pfp.png")
		api.update_profile(name = "Gex 🎄")
		db["profile_status"] = "dec"

	if int((current_date.strftime("%m"))) == 8 and int((current_date.strftime("%d"))) == 19:
		api.update_profile_image("gexphrasebot_birthday_pfp.png")
		api.update_profile(name = "Gex 🎂")
		db["profile_status"] = "birthday"
"""
#Caleb Mathurin 05/30/2021 - calls on the keep_alive function to keep this script running 24/7
#keep_alive()

#Caleb Mathurin 05/30/2021 - infinite while loop
while True:

	#Caleb Mathurin 05/31/2021 - defines timezone (US Eastern) and defines current_date using the datetime module.
	eastern_timezone = pytz.timezone("US/Eastern")
	current_date = datetime.datetime.now(eastern_timezone)

	#Caleb Mathurin 08/11/2021 - TRANSLATION: if the hour is any hour, the minute is 0 or 30, and the second, is zero, Tweet phrase and sleep for 10 seconds. if not, pass.
	#This code makes GexPhraseBot Tweet every hour on the hour. If the Tweet is successful, he will sleep for two seconds to ensure he doesn't tweet immediately after the first tweet by mistake.  
	if (int((current_date.strftime("%M"))) == 0 and int((current_date.strftime("%S"))) == 0) or (int((current_date.strftime("%M"))) == 30 and int((current_date.strftime("%S"))) == 0):
		try:
			tweets()
			time.sleep(2)
		except tweepy.errors.TweepyException:
			pass
	else:
		pass
"""
	#Caleb Mathurin 09/03/2021 - this code makes GexPhraseBot reply to certain users' latest tweet if he has not already on the 15th second of every minute
	if int((current_date.strftime("%S"))) == 15:
		replies()
	else:
		pass
"""
"""
	#Caleb Mathurin 12/09/2021 - this code makes GexPhraseBot check if his profile (pfp + name) are correct given the time of year every midnight
	if int((current_date.strftime("%H"))) == 0 and int((current_date.strftime("%M"))) == 0 and int((current_date.strftime("%S"))) == 30:
		profile()
		time.sleep(2)
	else: 
		pass
"""
	#phrase = phrase_constructor()
	#print(phrase)
	#time.sleep(2)

#This script is run every hour on the hour through Replit.com and is supported by UptimeRobot.com

#Note: Below is the patch log for all GexPhraseBot updates, but more detailed changes can be seen by viewing the script history in the script on Replit.com

#PATCH LOG:
#08/19/2020-08/24/2020: GexPhraseBot was initially coded with the purpose of stitching together parts of speech to create random sentences. It started with 30 names, 8 verbs, 4 locations, and 6 total possibilities for phrase templates. (ver. 1)
#12/20/2020-12/25/2020: This patch focused on adding more variety to phrases. There are still 30 names and 4 locations, but verbs were split up to accomodate for the new phrase template system (4 and 4). The total number of possibilities for phrase templates was now 3 for the purpose of simplifying the code. (ver. 2)
#01/14/2021-01/26/2021: This patch focused on more total parts of speech. Name count was upped to 44, location count was bumped to 7, verbs were split into three categories based on the way they would fit into a sentence. Each section had 5 verbs each. By the way, the verb is more like a predicate, and always has been. And lastly, the total number of phrase templates has been bumped to 7. (ver. 3)
#04/07/2021-04/11/2021: GexPhraseBot Replies was programmed. It is an entirely different script from this one that makes the bot reply to Tweets of various users. It will be monitored over the next few days to ensure it works properly. Also, The name count of this script and the replies script was bumped up to 45. (Reggie Fils-Aimé was added.) This patch wasn't much of an update as it was an expansion. (ver. 4)
#04/18/2021: After malfunctioning, I finally got around to fixing GexPhraseBot replies. It should be working fine now. I also added expanded randphrase 7 (phrase constructor 5) in both GexPhraseBot and GexPhraseBot Replies. It now acts as a sub menu which can pull other phrases out from it. In other words, if randphrase 7 is chosen randomly, there are 9 possible phrases it can pick. These phrases are pulled directly from Gex: Enter the Gecko with some minor tweaks. More details about this update can be found in the GexPhraseBot Replies script. (ver. 5) 
#05/02/2021: This was just a small update. I changed a few of the weaker names like Rihanna and the Wright brothers, as well as some of the randverb3 verbs. Also, this script was changed from running through Wayscript loosely every hour to running exactly on the hour. (ver. 6)
#05/09/2021: Another small update. The original Gex Phrase Bot app got restricted on Twitter, so I made a new one (GexPhraseBot). The keys at the beginning of the script have been updated to account for that. (ver. 7)
#05/30/2021: Notable update. Since Wayscript.com changed their pricing policy, I was forced to migrate GexPhraseBot to a different site to be ran remotely. I found a YouTube video (https://youtu.be/S6pBLq8Jv_A) showing how I can use Repl.it (which I use to code anyway) and UptimeRobot.com to run GexPhraseBot remotely. In the keep_alive.py file, there is code creating a server which I can use to run both the normal Tweets and replies scripts. UptimeRobot "pings" this script every five minutes to ensure the server doesn't go down, but only for this script. GexPhraseBot Replies doesn't need it since it runs frequently enough to hold down the fort by itself. In the future, I have plans to make both scripts generate random-er phrases. That's all for this update. (ver. 8)
#05/31/2021: Small update. I did some testing with the datetime module and I figured out a way to have Gex tweet on the hour instead of just at some time during every hour. (ver. 9)
#06/17/2021-06/20/2021: This update is a very large one. This update focused on making GexPhraseBot make even more unique Tweets than before. The name count has gone up from 46 to 51. There are still 7 phrase templates that can be chosen via the "randphrase = randint(1, 7)" code towards the top of the script. All three verb categories have doubled in size for possible verbs. There are 10 possibilities for verb1, verb2, and verb3. This is a double in size from before, where they all had five. There are also more available locations now (7 to 10). What used to be phrase constructor 1 has now been relabeled as phrase constructor 1-2, meaning all following phrase constructors have their label numbers subtracted by 1. That being said, phrase constructor 5 has been overhauled to allow for more randomness. There are now two adjectives that appear in the sentence ("Captain, they are a /adjective1/ alien race that find /name/ /adjective2/.") Similarly, phrase constructor 6 now has the ability to choose between different money values in the question it asks ("I'll take /name/'s /location/ for $/jeopardymoneyvalue/, Alex.") And in phrase constructor 7, the phrase that has Gex ask about a sandwich in his pocket can now use a few different food items instead ("Are you after that old /fooditem/ in my pocket?") But that's not all. To save physical space and make this script easier to read, I have opted to ditch most of the randints at the top of the script. Only randphrase remains. Now, the items to be used in phrases are put into a list. Some code below that list from the "random" module chooses which item will be used (partofspeechtobeused = "random.choice(listname)") Every works exactly the same with this new method, but it saves about half the line space as the old method. Also, and this is fairly insignificant, I added dates to all the comments throughout this script to help my future self and potential other people if I decide to make this a group project. Also also, GexPhraseBot Replies got my Twitter application restricted again (it is now unrestricted), so I am debating whether or not I should bring him back. On one hand, he is effective at creating engagement, but on the other hand, he causes several issues. (ver. 10)
#06/28/2021: Relatively small update for today. I did some testing in my "Time & Datetime Test" Repl because Gex was not Tweeting occasionally. I found out I had a glitch that prevented the script from executing as planned at 12 AM, which I have fixed. Hopefully, this will solve any other problems it's having. Also, I decided to bring back GexPhraseBot Replies due to the bot account not gaining much attention since I took Replies offline. (ver. 11)
#06/30/2021: Small update. I added some code that should make GexPhraseBot continue running if a Tweepy Error occurs. (ver. 12)
#07/15/2021: Small update. This was done mostly to help GexPhraseBot Replies. Long story short, the original Twitter project for GexPhraseBot got restricted, so I had to make a new one. The app I created did not have access to the V2 Twitter API like the old one did. I realized the old one was unrestricted, then decided to switch back to using it and its api keys in hopes of stopping the glitch where GexPhraseBot Replies replies to Tweets twice. In conclusion, the keys for this script have been changed. (ver. 13)
#07/16/2021: Relatively small update for today. I added some more possibilities for phrases. Phrase constructors 3 and 4 have been expanded to Phrase constructors 3-4 and 5-6, similar to Phrase constructor 1-2. randphrase 9, formerly known as randphrase 7, has had the total amount of phrase possibilities upped from 9 to 25. That's all for this update. (ver. 14)
#07/17/2021: Very small update. There was a grammatical glitch that occurred because I changed the spelling of one of the phrase possibilities. It's fixed now. Also, all instances of "Tail Time" throughout this script have two uppercased T's making "Tail Time" a proper noun. (ver. 15)
#08/02/2021-08/03/2021: Pretty significant update for today + yesterday. I have added two new phrase constructors after 5-6: Phrase constructors 7-8. Because of this, the old Phrase constructor 7 is now Phrase constructor 9, 8 is 10, and 9 is 11. Basically, phrase constructors 7, 8, and 9 were shifted up two constructor numbers. Also, one more phrase possibility for Phrase constructor 11 (formerly known as phrase constructor 9 and before that, 7) has been added. Additionally, some variable names have been changed to be less confusing and more easily movable if I add more in the future. That's all for now. (ver. 16)
#08/09/2021-08/11/2021: A few things for this update. For starters, this Repl has been reworked to be more clean and user-friendly because the old layout was bothering me. Now, the main phrase constructor is in its own file called "phrase_constructor.py". The main.py file is now much cleaner and less confusing. In it, a new function has been added called tweets(). Basically, it just takes the phrase variable from phrase_constructor.py and tweets it out or prints it. I am very fond of how the Repl looks now. However, the reason I did this was to finally attempt to combine this Repl with the GexPhraseBot Replies one. While it certainly could have been done, I still haven't found out a solution for GexPhraseBot Replies's glitching. But I did figure out the cause. After doing some research, I found out that Repl has bugs when reading and writing files, which would explain why the bot would sometimes reply to Tweets twice. If this gets fixed in the future, I'll re-implement the feature, but until then, GexPhraseBot will no longer reply to any Tweets. That's all for now. (ver. 17)
#09/03/2021: Okay, so after contacting Replit support, I found out about Replit databases which can supposedly help me with the replying problem. I've implemented this now into this Repl. Also, Gex will now reply to @GenZMoments in place of @nintendofac. Not a lot left to say. I just hope this works. (ver. 18)
#09/07/2021: Removed one of the users Gex replies to (GenZMoments). Now, Gex will only reply to vgdunkey, NintendoAmerica, NintendoEurope, Crystal Dynamics, and ScottTheWoz. Also, the multi-reply glitching seems to have stopped, which is good. (ver. 19)
#12/05/2021: Small update for today. I added a feature where Gex will add more names to name_list during certain times of the year. These times are October (Halloween-themed names) and December (Christmas-themed names). Also, Gex will now change his name and profile picture accordingly during these months. Also, I think it is now safe to say that the multi-reply glitch has been completely taken care of. Also, I put a backup of this script in the documents of my computer, just in case. (ver. 20)
#12/09/2021: Small bug fix. Gex was experiencing an issue where he would stop running unexpectedly. I read the error and concluded that it must be because he was using the profile() function too often (it was left alone under the while loop). So I decided that the best way to fix this was to have Gex use the profile() function only every midnight as opposed to every second. (ver. 21)
#12/20/2021: Small update for today. Gex got restricted on Twitter (yet again) and I think it might be because of the profile() function glitch I dealt with in ver. 21. Even though I eradicated it, it might have still contributed to a high rate limit, causing Gex to lose permissions from Twitter. We'll just have to wait and see with that. Also, I realized that the timing of profile() going off at midnight may be clashed by the tweets() function which also goes off at midnight and sleeps for 2 seconds. To fix this, I just made the profile() function go off 30 seconds after midnight, then sleep for 2 seconds. (ver. 22)
#01/22/2022-01/23/2022: Significant content update for today. Also, for the record, I'm going to start doing more straightforward patch notes instead of giving my life story every time. Added "Freddy Fazbear" to names list. Added 5 new verbs to every one of the verbs (20 new total, 15 total each). Edited the preposition section to account for the new verbs. Added 5 new adjectives each to randphrase7 and randphrase8 (10 new total, 21 total each). Added "Banana Slamma!" as an option for randphrase11 (27th option). Commented sections in phrase_constructor.py to make the file easier to read for future editing. Added PlayStation as a 6th account to reply to. (ver. 23)
#01/28/2022-01/29/2022: Small update for today. In the replies() function, tweet_1, tweet_2, tweet_3, tweet_4, tweet_5, and tweet_6 have been made into global variables because the script would frequently fail with this (UnboundLocalError: local variable 'X' referenced before assignment). "Lil Nas X" has been added to the name_list seen in phrase_constructor.py (53 total names). Changed the verb3_list verb "watch movies" to "watch romance movies." (ver. 24)
#04/17/2022: Content update for today. Added 14 names to name_list. Added one verb to each of the four verb categories (verb1, verb2, verb3, verb4). Added a few lines of code at the end of phrase_constructor.py that, on a 1 in 256 chance, has the phrase change to become a quote about the future of robots + Gex acknowledging his own sentience. For funsies. (ver. 25)
#07/11/2022-07/12/2022: A more aesthetical update for today. I added two features: one where Gex will Tweet out an announcement of his Twitter birthday on August 19, and one where Gex will Tweet out special Tweets when follower milestones have been reached. (ver. 26)
#08/18/2022-08/19/2022: Took the milestone counter and the birthday message and put them in the tweets function so they would never send as replies about a week ago. Added a birthday pfp to the profile function and replaced all the pfps with png versions (they were jpegs before). (ver. 27)
#11/25/2022: Added 7 names to name_list in phrase_constructor.py. Made Gex reply to @realDonaldTrump and @elonmusk. Commented out the sentiencephrase section of phrase_constructor.py; will likely think of new dialogue for it. (ver. 28)
#11/15/2023: Hi. Been a while. Gex got restricted in April 2023, so I'm trying to get the bot up again. All I did was change the keys and and edit the comment explaining them. Actually, I have just found out that the Twitter API and its allowed usage has been updated since Elon Musk took over, meaning that if I wanted to get Gex back up, he wouldn't be able to reply to any tweets. Only tweet independently. Unless I paid for more API access. And I have too much self respect to do that. I'll think about running a Gex with less capability but I'm leaning toward leaving him dormant. (ver. 29) 
