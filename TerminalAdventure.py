
#Name of the player
name = input("What's your name? ")
print(f"\nHey {name}! Let’s live your best day!\n")

# Morning
choice1 = int(input("⏰ It’s 7:00 AM. The alarm rings.\n1. Get out of bed and start your day\n2. Hit snooze.\nWhat do you do? (1/2): "))
if choice1 == 1:
    print("\n🏃 You start with a quick jog and feel energized!\n")
else:
    print("\n😴 You oversleep and skip breakfast. Risky start!\n")

# Mid-Morning
choice2 = int(input("🎓 It’s 10:00 AM. You have a lecture.\n1. Attend it.\n2. Skip and work on your side project.\nWhat do you do? (1/2): "))
if choice2 == 1 and choice1 == 1:
    print("\n📘 You learn something useful for your career.\n")
elif choice2 == 2 and choice1 == 1:
    print("\n💻 You make great progress on your project—worth it!\n")
elif choice2 == 1 and choice1 == 2:
    print("\n🍕 It's something useful for your career but darn, aren't you hungry! You couldn’t pay attention at all!\n")
elif choice2 == 2 and choice1 == 2:
    print("\n🍕 You sit on your project but couldn't make any progress as you were buying food for yourself. So much for that laptop.\n")
else: 
    print("Oops! I hope you know your numbers! Wrong entry!")

# Noon
choice3 = int(input("📞 You get a call from your friend.\n1. Pick up\n2. Ignore\nWhat do you do? (1/2): "))
if choice3 == 1:
    print("\n🗣️ You catch up and your friend invites you to an evening hangout.\n")
    choice4 = int(input("🎤 They ask if you'd like to join an open mic night.\n1. Say yes.\n2. Politely decline.\nYour choice? (1/2): "))
    if choice4 == 1:
        print("\n🎸 You perform a quick piece on stage—nervous at first, but the crowd cheers you on. You feel alive! You later head back home\n")
    else:
        print("\n☕ You hang out at the venue, sipping hot chocolate and laughing with friends. taking pictures all evening.you later head back home\n")
else:
    print("\n🙁 You ignore the call. Later, you feel a bit left out seeing their group story online.\n")
    choice4 = int(input("📚 Do you:\n1. Read a book and wind down.\n2. Scroll social media endlessly.\nYour choice? (1/2): "))
    if choice4 == 1:
        print("\n📖 The book makes you reflect on your goals. You journal your thoughts and plan a better tomorrow.\n")
    else:
        print("\n📱 You lose track of time, and get immersed into the internet.\n")

# Afternoon twist
choice5 = int(input("⚡ A sudden power cut hits the area at 4:00 PM.\n1. Go for a walk in the park\n2. Light candles and play music from your phone\nWhat do you do? (1/2): "))
if choice5 == 1:
    print("\n🌳 You walk under the golden sun, meet an old neighbor and get invited to a weekend event!\n")
else:
    print("\n🕯️ The candlelight mood is magical. You hum along to your playlist and feel like you're in a movie.\n")

# Evening productivity
choice6 = int(input("🧠 You feel a burst of focus around 6:00 PM.\n1. Study for upcoming test\n2. Try that online course you've been curious about\n3. Bake something for fun\nYour choice? (1/2/3): "))
if choice6 == 1 and choice4 == 1:
    print("\n📚 You revise like a boss. Even made a mind map. Future You is grateful!\n")
elif choice6 == 1 and choice4 == 2:
    print("\n📚 You start studying but now since you doom scrolled you have very less time for preparation. Gotta pull an all nighter maybe...\n")
elif choice6 == 2 and choice4 == 1:
    print("\n🌐 You finish 2 modules of the course and get a digital badge. Sweet!\n")
elif choice6 == 2 and choice4 == 2:
    print("\n🌐 You could only finish the 1st module. Darn... doomscrolling did take away your time.. But nonetheless awesome work!\n")
elif choice6 == 3 and choice4 == 1:
    print("\n🍪 You bake choco-chip cookies and even share a few with your neighbor. You're officially everyone's favorite human now.\n")
elif choice6 == 3 and choice4 == 2:
    print("\n🍪 You bake choco-chip cookies and even add a few new things to your cookies because of those tricks on the internet! your neighbours loved it.\nYou now have a secret cookie recipe that all the kids in the neighbourhood love!\n")
else:
    print("\nOops!wrong choice\n")

# Night time finale
choice7 = int(input("🌙 It's bedtime but you're still wide awake.\n1. Watch a short documentary\n2. Meditate and sleep\n3. Text your crush\nWhat do you do? (1/2/3): "))
if choice7 == 1:
    print("\n📺 You learn about bioluminescent jellyfish.Something to talk about when u text ur crush?Who knows...\n")
elif choice7 == 2:
    print("\n🧘 You sleep peacefully with lavender-scented vibes. 10/10 sleep quality.\n")
else:
    print("\n💬 You text them 'Hey' and they reply instantly! A new chapter may be beginning... 😳\n")

# Closing
print(f"🌟 Goodnight, {name}. Whether it was a perfect day or a weird one, you made it count.")
print("✨ Come back tomorrow for another version of your best life!")
