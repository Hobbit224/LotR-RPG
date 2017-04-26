import random
import time
from Herosheet import Hobbit
from Herosheet import Dwarf
from Herosheet import Rohan
from Herosheet import Gondor
from Herosheet import Rivendell
from Herosheet import Lothlorien

startup = True
while startup == True:
	new_game = raw_input("Start a new game? Y/N \n")
	if new_game == "Y":
		print "Splendid! I wish thee well on thy quest.\n"
		startup = False
	elif new_game == "N":
		print "What a shame. Perhaps one day thou wilst become a hero.\n"
		
	else:
		print "That is not a valid input.\n"

time.sleep (1.5)
print "You're sitting in the Prancing Pony in the town of Bree, when a bearded old man in a gray hat approaches you. \n"
time.sleep (1.5)

print "                         ,---."
print "                        /    |"
print "                       /     |"
print "                      /      |"
print "                     /       |"
print "                ___,'        |"
print "              <  -'          :"
print "               `-.__..--'``-,_\_"
print "                  |o/ <o>` :,.)_`>"
print "                  :/ `     ||/)"
print "                  (_.).__,-` |\ "
print "                  /( `.``   `| : "
print "                  \'`-.)  `  ; ;"
print "                 | `       /-<"
print "                  |     `  /   `."
print "  ,-_-..____     /|  `    :__..-'\ "
print " /,'-.__\\  ``-./ :`      ;       \ "
print " `\ `\  `\\  \ :  (   `  /  ,   `. \ "
print "   \` \   \\   |  | `   :  :     .\ \ "
print "    \ `\_  ))  :  ;     |  |      ): :"
print "   (`-.-'\ ||  |\ \   ` ;  ;       | |"
print "    \-_   `;;._   ( `  /  /_       | |"
print "     `-.-.// ,'`-._\__/_,'         ; |"
print "        \:: :     /     `     ,   /  |"
print "         || |    (        ,' /   /   |"
print "         ||                ,'   /    |"

         
         
          
          
         
           
            
             
              
               
                
                
             
                
                
                
                


print "'I say, I haven't seen you here before,' he says, 'and I know nearly everybody who comes to this inn. What is your name?'"
hero_name = raw_input("> ")
print ('\n')
time.sleep (1.5)
print "'Hmm, %s, not what I'd have chosen to call you but it's your name after all. Now, if you don't mind me asking, where do you call home?'" % (hero_name)
print "\n"
time.sleep (1.5)
print "1. The Shire: You are a hobbit, one of the wee folk of Middle Earth. Your kind are wary of the big folk of the world, and have become very good at hiding."
print "2. The Misty Mountains: You are a dwarf. Taller than hobbits yet smaller than men, your people are hardy mountain dwellers. You have an eye for treasure and are not easily hurt."
print "3. Rohan: You are a man of Rohan, the land of the horselords. Since you were a child you've been in the saddle. Your mounted combat skill is outstanding, and you can travel swiftly on horseback."
print "4. Gondor: You are a man of Gondor, the last great kingdom of Middle Earth. Your kinsmen have held back the forces of Mordor for centuries. You are a jack of all trades, and master of none."
print "5. Rivendell: You are an elf of the clan of Noldor, immortal and fair. Elrond Half-elven is your lord. Your people are excellent healers."
print "6. Lothlorien: You are an elf of the clan of Telerin, immortal and fair. Celeborn and Galadriel are your king and queen. Your people have more magical ability than any other race in Middle Earth."
race_choice = raw_input("> ")

if race_choice == "1":
	hero_race = "Hobbit"
	hero_class = Hobbit(hero_name)
if race_choice == "2":
	hero_race = "Dwarf"
	hero_class = Dwarf(hero_name)
if race_choice == "3":
	hero_race = "Man of Rohan"
	hero_class = Rohan(hero_name)
if race_choice == "4":
	hero_race = "Man of Gondor"
	hero_class = Gondor(hero_name)
if race_choice == "5":
	hero_race = "Elf of Rivendell"
	hero_class = Rivendell(hero_name)
if race_choice == "6":
	hero_race = "Elf of Lothlorien"
	hero_class = Lothlorien(hero_name)
time.sleep (1.5)

print "'%s you say? It's been many long years since I traveled that way, but I remember it fondly.' \n" % (hero_class.home)
time.sleep (1.5)

print "'Anyway, I hate to be so forward, but there's no use in wasting our breath. I have something that I need delivered to a friend of mine, and I get the feeling that you just might be the one for the job. \nYou'll be handsomely rewarded. What do you say, yes or no?'"
answer_to_gandalf = raw_input("> ")
gandalf_unanswered = True
while gandalf_unanswered == True:
	if answer_to_gandalf == "Yes":
		print "'Wonderful! I'll pay for you to stay here tonight, and you can set out in the morning.'"
		gandalf_unanswered = False
	elif answer_to_gandalf == "No":
		print "'Oh come now, it won't be so bad. What do you say, yes or no?'"
		gandalf_unanswered = False
	else:
		print "'Come again? I can't hear you if you mumble. I'm an old man after all.'"
		gandalf_unanswered = False

































