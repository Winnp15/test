def zodiac(month,date):
    if month == 1:                  
        if date < 20 :
            return 'Capricorn'
        else:
            return 'Aquarius'
    elif month == 2 :               
        if date < 19 :
            return 'Aquarius'
        else :
            return 'Pisces'
    elif month == 3 :               
        if date < 21 :
            return 'Pisces'
        else :
            return 'Aries'
    elif month == 4 :               
        if date < 20 :
            return 'Aries'
        else :
            return 'Tuarus'
    elif month == 5 :
        if date < 21 :
            return 'Tuarus'
        else :
            return 'Gemini'
    elif month == 6 :
        if date < 22 :
            return 'Gemini'
        else :
            return 'Cancer'
    elif month == 7 :
        if date < 23 :
            return 'Cancer'
        else :
            return 'Leo'
    elif month == 8 :
        if date < 23 :
            return 'Leo'
        else :
            return 'Virgo'
    elif month == 9 :
        if date < 23 :
            return 'Virgo'
        else :
            return 'libra'
    elif month == 10 :
        if date < 24 :
            return 'Libra'
        else :
            return 'Scorpio'
    elif month == 11 :
        if date < 22 :
            return 'Scorpio'
        else :
            return 'Sagitarrius'
    elif month == 12 :
        if date < 22 :
            return 'Sagitarrius'
        else :
            return 'Capricorn'


def stone(zodiac):
    if zodiac == 'Aries':
        return "Rubies and red agate" 
    elif zodiac == 'Tuarus':
        return 'Rose quartz'
    elif zodiac == 'Gemini':
        return 'Amber'
    elif zodiac == 'Cancer':
        return 'Blue valcanic stone'
    elif zodiac == 'Leo':
        return 'A hard and transparent stone'
    elif zodiac == 'Virgo':
        return 'Emerald greens'
    elif zodiac == 'Libra':
        return 'Aventurine stone'
    elif zodiac == 'Scorpio':
        return 'A touch of hematite'
    elif zodiac == 'Sagittariue':
        return 'Topaz'
    elif zodiac == 'Capricorn':
        return 'An ancient precious stone'
    elif zodiac == 'Aquarius':
        return 'White sapphire'
    elif zodiac == 'Pisces':
        return 'Turquoise'




def lucky_num(date,month,year):
    def code(n):
        while n > 10:
            n = sum(int(i) for i in str(n))
        return n
    
    date = code(date)
    month = code(month)
    year = code(year)

    y = int(date)+int(month)+int(year)
    y = code(y)

    return y


def lucky_color(zodiac):
    if zodiac == 'Aries':
        return "Shade of red, wearing bright color like red will help you feel more confident and ready for new opportunities" 
    elif zodiac == 'Tuarus':
        return 'Green, choosing to wear this color will bring you good fortune and attracts new experiences'
    elif zodiac == 'Gemini':
        return 'Bright yellow and green, this bright color make you feel excited and lift your sprit'
    elif zodiac == 'Cancer':
        return 'Magenta, wearinng this color frequently will help with money problem and provide excellent luck'
    elif zodiac == 'Leo':
        return 'Bright colors, like orange yellow gold will help you shine and gain lots of attention'
    elif zodiac == 'Virgo':
        return 'Green, choosing to wear this color will provide luck for personal relationship and help with overthinking mind'
    elif zodiac == 'Libra':
        return 'Blue, helps to maintain peace in relationship and associate with calmness kindness and beauty'
    elif zodiac == 'Scorpio':
        return 'Red Coral, helps to focus on your goal and boost your luck simply by adding this color to your wardrobe'
    elif zodiac == 'Sagittariue':
        return 'Dark yellow and Orange, support your strong personality and protect you it also enchances your communication skills'
    elif zodiac == 'Capricorn':
        return 'Black and Indigo, these colors will bring success in life while also highly suit for business and work life'
    elif zodiac == 'Aquarius':
        return 'Electric blue and Purple, brings creative mind while also promote calm and ec=nchance imaginative abilities'
    elif zodiac == 'Pisces':
        return 'Deep blue and sea, this colors helps with imaginative and focus mind while also boosting your luck'


def personality(time):
    if time <=0.59 or time>=23.00:
        return "you are lively person like to travel to new places,like to do risky things.You are kind person, like to help others. You don't easily get attached to anyone."
    elif time <=2.59:
        return "You are calm person, but when you gets angry you is violent. You do things slowly and takes your time, but you are a cheerful person who gets along well with people."
    elif time <=4.59:
        return "You are person who likes to do challenging things, has high self-confidence, does not give up to anyone and dares to speak out about what you believes. You quite stubborn, but you loves someone truly. However, you are person who falls in love easily."
    elif time <=6.59:
        return "You are a well-mannered person, careful in everything you does, and quite meticulous. You do not let anything go wrong easily in your work. You likes to help others. You gets upset easily, but soon you smiles again. You is quite reserved and does not like to cause trouble with anyone."
    elif time <=8.59:
        return "You are person with a leadership personality makes others trust you easily. You is not afraid of anyone, likes to do risky things, likes challenges, is a person with high self-confidence, is a creative person, has the ability to complete various tasks successfully."
    elif time <=10.59:
        return "You are rather neat person, likes cleanliness, has good taste.You are gentle and polite. You fell easy to get along with someone. You has goals in life."
    elif time <=12.59:
        return "You are cheerful person, have a sense of humor and you are happy almost the time. You are a freedom-loving person, you do not like to be controlled by others, you do not like to stay in one place, you like to travel, you like adventures, and seeing new things makes you happy."
    elif time <=14.59:
        return "You is a peaceful person, does not like anything chaotic. You does everything very carefully. You is an honest person, kind-hearted, humble and polite. You does not like to argue with anyone. You is very compromising. If you loves someone, you loves them truly and devotes everything for love."
    elif time <=16.59:
        return "You are a person who always does things according to your own wishes, doesn't care what others think, tends to act before thinking, so you always has headaches. You are a person who is intelligent, quick-witted, good at surviving, dares to speak, dares to act, has a strong mind. You always looks a bit agile but You have a good heart"
    elif time <=18.59:
        return "You are a reserved person, has a rather aggressive mindset, is highly self-confident, likes to do things according to the rules, is rather fussy, likes to complain, does things meticulously, does not like to do things out of line, works seriously, has very high standards in work, does not like to do things carelessly."
    elif time <=20.59:
        return "You are a hardworking person, work hard and never give up. Do things straightforwardly, dare to speak and dare to do. Be a person who is enthusiastic in everything. Do not like daydreaming. Like to make dreams come true. Like to help others. Be open-minded. Be a person worth getting to know. Be sincere to everyone."
    elif time <=22.59:
        return "You is not talkative, but you is romantic, likes to surprise someone, is kind, polite, charming, and does not like to rush things. You is considered a slow person, gentle and soft."


def guardian_angel(week):
    if week=="monday"or "Monday":
        return "your guardian angel is Gabriel: The Angel of the Moon and Magic"
    elif week=="tuesday"or "Tuesday":
        return "your guardian angel is Samael: The Warrior Angel"
    elif week=="wednesday"or "Wednesday":
        return "your guardian angel is Raphael: the Divine Healer and Guide"
    elif week=="thursday"or "thursday":
        return "your guardian angel is Sachiel: The Angel of Mercy and Good Fortune"
    elif week=="friday"or "Friday":
        return "your guardian angel is Anael: The Angel of Love and Relationships"
    elif week=="saturday"or "Saturday":
        return "your guardian angel is Angel: Cassiel, the Angel of Discipline and Perseverance"
    elif week=="sunday"or "Sunday":
        return "your guardian angel is Michael: Empowering Your Inner Light"