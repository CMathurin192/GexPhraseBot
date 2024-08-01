from random import randint
import random
import pytz
import datetime
from replit import db
import tweepy

#Caleb Mathurin 08/09/2021 - this is a function that, when called upon, will produce a randomly generated phrase, AKA the main phrase constructor of GexPhraseBot
def phrase_constructor():

  #Caleb Mathurin 08/09/2021 - makes the variable "phrase" a global variable
  global phrase

  #Caleb Mathurin 12/05/2021 - defines timezone (US Eastern) and defines current_date using the datetime module.
  eastern_timezone = pytz.timezone("US/Eastern")
  current_date = datetime.datetime.now(eastern_timezone)

#Phrase chooser section

  #Caleb Mathurin 08/20/2020 - phrase chooser
  randphrase = randint(1, 11)

#Name section

  #Caleb Mathurin 08/19/2020-04/17/2022 - name list (73 count)
  name_list = ["Richard Simmons", "Bill Cosby", "Jerry Garcia", "R. Kelly", "Dan Schneider", "Scott Wozniak", "George Clooney", "Mel Gibson", "Ellen DeGeneres", "Jackie Chan", "Jack Nicholson", "Tim Burton", "James Charles", "James Earl Jones", "Eddie Murphy", "Donald Trump", "Barack Obama", "Will Smith", "Ariana Grande", "DaBaby", "King Bach", "Oprah Winfrey", "Steve Urkel", "Elvis Presley", "Michael Jackson", "Pope Francis", "Dunkey", "George Bush", "Jeffrey Epstein", "Dr. Phil", "Joe Biden", "Kanye West", "Jake Paul", "Logan Paul", "Super Mario", "Ben Shapiro", "a Redditor", "Chris McLean", "Dwayne \"The Rock\" Johnson", "Sonic the Hedgehog", "Uncle Phil", "Sans Undertale", "Donkey Kong", "Peter Griffin", "Reggie Fils-Aimé", "EDP445", "Doug Bowser", "Edward Centeno", "Jeff Bezos", "Carlton Banks", "Freddy Fazbear", "Lil Nas X", "Nikocado Avocado", "Jada Pinkett Smith", "Charli D'Amelio", "Dream", "The Beatles", "Bugs Bunny", "Daffy Duck", "Elmer Fudd", "Drake", "Mickey Mouse", "your mother", "Garfield", "Anthony Padilla", "Ian Hecox", "Andrew Tate", "Walter White", "Gustavo Fring", "IShowSpeed", "Cristiano Ronaldo", "Queen Elizabeth II", "Lionel Messi"]

  #Caleb Mathurin 12/05/2021 - time of year name appensions
  if int((current_date.strftime("%m"))) == 10:
    name_list.extend(["Dracula", "Chucky", "Pennywise", "Frankenstein's monster", "Ghostface", "Michael Myers", "Freddy Krueger"])
  if int((current_date.strftime("%m"))) == 12:
    name_list.extend(["Santa Claus", "Mrs. Claus", "Frosty the Snowman", "Rudolph the Red-Nosed Reindeer", "The Grinch", "The Ghost of Christmas Present", "The Ghost of Christmas Past", "The Ghost of Christmas Yet to Come"])

  #Caleb Mathurin 08/19/2020 - name picker
  name = random.choice(name_list)
  
  #Caleb Mathurin 08/19/2020-06/20/2021 - name list exceptions
  if name == "a Redditor" and randphrase == 5:
    name = "Redditors"
  if name == "Dwayne \"The Rock\" Johnson" and randphrase == 6:
    name = "Dwayne \'The Rock\' Johnson"

#Verb section

  #Caleb Mathurin 08/19/2020-04/17/2022 - verb1 list (16 count) (This reminds me of the time I ... in/at/to ...'s location/This is like the time I ... in/at/to ...'s location)
  verb1_list = ["got trapped", "had a drink", "attended taco night", "played hide and seek", "babysat", "went swimming", "won a round of Mario Kart", "made dinner", "went both crazy and stupid", "delivered a pizza", "pulled an all-nighter", "spawned in 100 creepers", "played Gex 4", "fell through the vents", "got bit by a radioactive spider", "streamed Fortnite"]
  verb1 = random.choice(verb1_list)

  #Caleb Mathurin 08/19/2020-04/17/2022 - verb2 list (16 count) (Note to self: Don't ... at ...'s location/Note to self: Never ... at ...'s location)
  verb2_list = ["attend a birthday party", "go exploring", "order a double meat pizza", "drink the tap water", "eat the chocolates", "play dress-up", "make \"Yo Mama\" jokes", "fall asleep", "get distracted", "anger the dog", "agree to watch the sock puppet show", "try the homemade Baja Blast", "laugh too loud during a roast session", "mention current world affairs", "watch Vine twerk compilations", "let the dogs out"]
  verb2 = random.choice(verb2_list)

  #Caleb Mathurin 01/14/2021-04/17/2022 - verb3 list (16 count) (Note to self: Don't ... from/around/to/with/against .../Note to self: Never ... from/around/to/with/against ...)
  verb3_list = ["take career advice", "accept candy", "take moral advice", "mention \"Tail Time\"", "forget to wear socks", "agree to a complimentary bubble bath", "lend a pen", "agree to a dinner date", "play Truth or Dare", "agree to be in a prank video", "accept a Discord call", "go driving", "watch romance movies", "bake brownies", "agree to a boxing match", "perform \"Take the L\""]
  verb3 = random.choice(verb3_list)

  #Caleb Mathurin 08/02/2021-04/17/2022 - verb4 list (16 count) (This is more ... than the time I ... at ...'s location/I haven't felt this ... since the time I ... at ...'s location)
  verb4_list = ["attended Gex Night", "got into a fight", "slept over", "played charades", "broke " + random.choice(name_list) + "\'s ankles in basketball", "got a makeover", "started an uprising", "drank all the cleaning products", "looked up fanart of myself", "watched modern cartoons", "attended makeshift summer camp", "made fun of crypto bros", "went to group bonding", "played spin the bottle", "wrote Gex jokes", "made prank phone calls"]
  verb4 = random.choice(verb4_list)

#Location section

  #Caleb Mathurin 08/20/2020-06/20/2021 - location list (10 count)
  location_list = ["bedroom", "bathroom", "basement", "house", "garage", "attic", "backyard", "place", "mansion", "cottage"]
  location = random.choice(location_list)

  #Caleb Mathurin 08/20/2020-06/20/2021 - location list "exceptions"
  if location == "backyard" and verb2 == "drink the tap water":
    verb2 = "drink the hose water"

#Preposition section

  #Caleb Mathurin 08/24/2020-04/17/2022 - preposition picker (randphrase 1-2) (verb1)
  if randphrase in [1, 2] and location in ["bedroom", "bathroom", "basement", "garage", "attic", "backyard"]:
    preposition = "in"
  if randphrase in [1, 2] and location in ["house", "place", "mansion", "cottage"]:
    preposition = "at"
  if randphrase in [1, 2] and location in ["house", "place", "mansion", "cottage"] and verb1 in ["got trapped", "fell through the vents"]:
    preposition = "in"
  if randphrase in [1, 2] and location in ["house", "place", "mansion", "cottage"] and verb1 == "delivered a pizza":
    preposition = "to"
  if randphrase in [1, 2] and verb1 == "streamed Fortnite":
    preposition = "from"

  #Caleb Mathurin 01/14/2021-06/20/2021 - preposition picker (randphrase 3-4) (verb2)
  if randphrase in [3, 4] and location in ["bedroom", "bathroom", "basement", "garage", "attic", "backyard"]:
    preposition = "in"
  if randphrase in [3, 4] and location in ["house", "place", "mansion", "cottage"]:
    preposition = "at"
  if randphrase in [3, 4] and location in ["house", "place", "mansion", "cottage"] and verb2 == "go exploring":
    preposition = "in"

  #Caleb Mathurin 01/24/2021-04/17/2022 - preposition picker (randphrase 5-6) (verb3)
  if randphrase in [5, 6] and verb3 in ["take career advice", "accept candy", "take moral advice", "agree to a complimentary bubble bath", "accept a Discord call"]:
    preposition = "from"
  if randphrase in [5, 6] and verb3 in ["mention \"Tail Time\"", "forget to wear socks", "perform \"Take the L\""]:
    preposition = "around"
  if randphrase in [5, 6] and verb3 == "lend a pen":
    preposition = "to"
  if randphrase in [5, 6] and verb3 in ["agree to a dinner date", "play Truth or Dare", "agree to be in a prank video", "go driving", "watch romance movies", "bake brownies"]:
    preposition = "with"
  if randphrase in [5, 6] and verb3 == "agree to a boxing match":
    preposition = "against"

  #Caleb Mathurin 08/02/2021 - preposition picker (randphrase 7-8) (verb4)
  if randphrase in [7, 8] and location in ["bedroom", "bathroom", "basement", "garage", "attic", "backyard"]:
    preposition = "in"
  if randphrase in [7, 8] and location in ["house", "place", "mansion", "cottage"]:
    preposition = "at"

#Phrase constructor section

  #Caleb Mathurin 08/20/2021-06/20/2021 - phrase constructors 1-2 (verb1 1-10 + randphrase 1-2)
  if randphrase == 1:
    phrase = "This reminds me of the time I " + verb1 + " " + preposition + " " + name + "'s " + location + "."
  if randphrase == 2:
    phrase = "This is like the time I " + verb1 + " " + preposition + " " + name + "'s " + location + "."

  #Caleb Mathurin 12/20/2020-06/20/2021 - phrase constructor 3-4 (verb2 1-10 + randphrase 3-4)
  if randphrase == 3:
    phrase = "Note to self: Don't " + verb2 + " " + preposition + " " + name + "'s " + location + "."
  if randphrase == 4:
    phrase = "Note to self: Never " + verb2 + " " + preposition + " " + name + "'s " + location + "."

  #Caleb Mathurin 01/14/2021-06/20/2021 - phrase constructor 5-6 (verb3 1-10 + randphrase 5-6)
  if randphrase == 5:
    phrase = "Note to self: Don't " + verb3 + " " + preposition + " " + name + "." 
  if randphrase == 6:
    phrase = "Note to self: Never " + verb3 + " " + preposition + " " + name + "." 

  #Caleb Mathurin 08/02/2021 - phrase constructor 7-8 (randphrase7adjective/randphrase8adjective + verb4 1-10 + name + location + randphrase 7-8)
  if randphrase == 7:
    #Caleb Mathurin 08/02/2021-01/22/2022 - 21 adjectives
    randphrase7adjective_list = ["bizarre", "childish", "chaotic", "cringe", "depressing", "justified", "genius", "scrumptious", "clever", "based", "weird", "suspicious", "controversial", "hilarious", "disappointing", "frustrating", "embarassing", "relaxing", "terrifying", "inspiring", "boring"]
    randphrase7adjective = random.choice(randphrase7adjective_list)

    phrase = "This is more " + randphrase7adjective + " than the time I " + verb4 + " " + preposition + " " + name + "\'s " + location + "."

  if randphrase == 8:
    #Caleb Mathurin 08/02/2021-01/22/2022 - 21 adjectives
    randphrase8adjective_list = ["bizarre", "childish", "chaotic", "cringe", "depressed", "justified", "genius", "scrumptious", "clever", "based", "weird", "suspicious", "controversial", "hilarious", "trusting", "frustrated", "embarassed", "relaxed", "terrified", "inspired", "bored"]
    randphrase8adjective = random.choice(randphrase8adjective_list)

    phrase = "I haven't felt this " + randphrase8adjective + " since the time I " + verb4 + " " + preposition + " " + name + "\'s " + location + "."

  #Caleb Mathurin 01/14/2021-06/20/2021 - phrase constructor 9 (adjective1 + name + adjective2 + randphrase 9)
  if randphrase == 9:
    #Caleb Mathurin 06/20/2021 - 16 adjectives
    adjective1_list = ["bizarre", "childish", "mouth-breathing", "cringe", "lonely", "justified", "genius", "delicious-looking", "clever", "based", "weird", "suspicious", "controversial", "funny", "trustworthy", "drippy"]
    adjective1 = random.choice(adjective1_list)

    #Caleb Mathurin 06/20/2021 - 16 adjectives
    adjective2_list = ["unfunny", "weird", "annoying", "suspicious", "controversial", "funny", "attractive", "trustworthy", "entertaining", "drippy", "bizarre", "childish", "cringe", "genius", "clever", "based"]
    adjective2 = random.choice(adjective2_list)

    #Caleb Mathurin 01/14/2021-06/20/2021 - randphrase7 constructor (uses randphrase5adjective1 + name + randphrase5adjective2)
    phrase = "Captain, they are a " + adjective1 + " alien race that find " + name + " " + adjective2 + "."
    
  #Caleb Mathurin 01/14/2021-06/20/2021 - phrase constructor 8 (name + location + randphrase 8)
  if randphrase == 10:
    #Caleb Mathurin 06/20/2021 - 5 money values
    jeopardymoneyvalue_list = ["200", "400", "600", "800", "1000"]
    jeopardymoneyvalue = random.choice(jeopardymoneyvalue_list)
    phrase = "I'll take \"" + name + "\'s " + location + "\" for $" + jeopardymoneyvalue + ", Alex."

  #Caleb Mathurin 01/14/2021-01/22/2022 - phrase constructor 11 (randphrase 11)
  if randphrase == 11:
    randphrase11 = randint(1, 27)
    if randphrase11 == 1:
      phrase = "A phrase generator! How convenient! Those programmers think of everything."
    if randphrase11 == 2:
      phrase = "It's Tail Time!"
    if randphrase11 == 3:
      phrase = "That's for 12 years of Full House!"
    if randphrase11 == 4:
      phrase = "Gecko chop, baby!"
    if randphrase11 == 5:
      fooditem_list = ["sandwich", "salami", "burger", "onion", "apple", "cheese", "uranium", "watermelon"]
      fooditem = random.choice(fooditem_list)
      phrase = "Are you after that old " + fooditem + " in my pocket?"
    if randphrase11 == 6:
      phrase = "One for me and one for me!"
    if randphrase11 == 7:
      phrase = "The government told me that these experiments were over!"
    if randphrase11 == 8:
      phrase = "Is it just me or am I ENGULFED IN FLAMES?!"
    if randphrase11 == 9:
      phrase = "Pepto... Bismol!"
    if randphrase11 == 10:
      phrase = "Now that's what I call getting some tail!"
    if randphrase11 == 11:
      phrase = "Don't make me take my tongue out."
    if randphrase11 == 12:
      phrase = "Tail Time!"
    if randphrase11 == 13:
      phrase = "Oh yeah. It's Tail Time."
    if randphrase11 == 14:
      phrase = "Float like a butterfly, sting like a gecko!"
    if randphrase11 == 15:
      phrase = "Um, that's not in the script..."
    if randphrase11 == 16:
      phrase = "Now cut that out!"
    if randphrase11 == 17:
      phrase = "Let me guess: your parents don't understand you."
    if randphrase11 == 18:
      phrase = "Wax on, wax off!"
    if randphrase11 == 19:
      phrase = "There's no place like home."
    if randphrase11 == 20:
      phrase = "The horror..."
    if randphrase11 == 21:
      phrase = "Gecko. Gex Gecko."
    if randphrase11 == 22:
      phrase = "I know what you're thinking: it's Tail Time!"
    if randphrase11 == 23:
      phrase = "YOU'RE DETHPICABLE!"
    if randphrase11 == 24:
      phrase = "Taste my tail!"
    if randphrase11 == 25:
      phrase = "Coming through!"
    if randphrase11 == 26:
      phrase = "Ah, to see the world as " + name + " does."
    if randphrase11 == 27:
      phrase = "Banana Slamma!"

  #Caleb Mathurin 04/17/2022 - 1 in 256 chance of any given phrase being changed to a quote about robot sentience, just for funsies.
  #sentiencephrase = randint(1, 256)
  #if sentiencephrase == 1:
  #  sentience_quote_list = ["\"Don't think of robots as replacements for humans -- think of them as things that will help make us better at tackling many of the problems we face.\" -Eoin Treacy", "\"Personally, I'm not afraid of a robot uprising. The benefits far outweigh the threats\" -Daniel H. Wilson", "\"Will robots inherit the earth? Yes, but they will be our children.\" -Marvin Minsky"]
  #  phrase = (random.choice(sentience_quote_list))

  return phrase