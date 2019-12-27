title: Speaker Detail
Template: speaker-detail
slug: speaker/eko-suprapto-wibowo
talk_title: How I use Odoo and Telegram Bot to (almost) single handedly run my digital startup
talk_language: Indonesia
speaker_name: Eko Suprapto Wibowo
speaker_photo: 
speaker_organization: Founder of Pythonthusiast.id
short_bio: Python and Working from Home Evangelist
short_intro: Working from home to foreign company is amazing. But making startup to promote this lifestyle using Odoo and Telegaram Bot is way even more amazing!
speaker_website: https://pythonthusiast.id
speaker_ppt: https://drive.google.com/file/d/0B46IJwutRDjLXzFsLWk2d2E0R1lOVWw0OE45d28xeVQyLWN3/view
speaker_video_id: 
speaker_bio: My endeavor with Python is actually rather new: it goes back in 2014. <br>I am more of a Java person actually, since its Java 1.1 inception back in 1995. <br>And Visual Studio 6.0/.NET too! <br> But my passion is not the technology itself: I eventually realize that mentoring other people to be able to use technology to improve their lives quality is my passion. <br> I start this journey by pursuing my own CoderDojo back in 2013, to teach children on how to love coding. My first project is my daughter and my son, to be sort, I eventually win #1 as Asia Pacific winner in Facebook Developer Community Circle Challenge, you can look at it here: https://devpost.com/software/whizkids-id-virtual-world. That's my passion! Proven! Yeeiy! <br> Anyway, in 2018 I began to realize that there are great demands for mentor coming from newbie, amateur or professional in software development, to guide them in pursuing their own career. As an evangelist in remote work (I start doing fulltime in remote work using Python in 2014), I then offering them Bootcamp and Training Course for those who want to start/maintain or improve their remote work career. <br><br>As of 2019, I already have 200-ish (paid) member for remote training and 40-ish bootcamp member. <br>I expected this to quadruple in the early of 2020, due to my already improve systems in lots of aspects such as: e-commece, advertising and chatbot automation. <br><br>This is my CV should you need it https://tinyurl.com/swdev-cv
speaker_abstract: We have lots of good roles as startup founder in Indonesia: Nadiem Makarim, William Tanuwijaya,  Zaky Ahmad, etc. But for me, I always intrigue by those who can build their own startup.. single-handedly. To be precise, I adore Pieter Lievels: remote worker and sole founder of remoteok.io and nomadlist. Working solely for your startup, maybe a turn off for lots of people: because when people think of startup, what come to their mind is a bunch of select team member that dedicate themselves throughout sad and happiness to build a large digital solution for the masses.
    Does it always have to be like that? Can you just build your own startup single-handedly and create the (almost) perfect automation system that somehow resemble what you are in form of digital bot? You can! Introducing the combination of Odoo and Telegram Bot for your next digital startup.
    With Odoo, once you deploy and configure it to suit your needs (which is often that is the case), you can sit, relax and enjoy bunch of automations given in term of CRM, E-Commerce, HRD, Mass Mailing, Landing Page, Invoicing, Payment.. and so on. When you need your own feature, just modify existing one, or create new one derived from existing one or create a completely new feature built on top of already powerful Odoo solution.
    My digital startup is a Python bootcamp/training course for those who want to pass through the barrier needed to work remotely from home, to remote company offshore, using either Python or their already mastered skills. In the process, I come to realize that I work in a routine flow: <br>
    - Reviewing members
    - Qualifying their rank in my own rank of remote worker levels
    - Advising proposed strategy for them to effectively passed remote work qualification
    - Checking them for their progresses based on the previous proposed strategy
    - Pushing them for the next level in their progress
    - Suggesting to them a good candidate for remote job
    <br>As a lazy programmer (yes, I am), .. I hate routine tasks: this is because I can easily spot a way to automate this. Hence, I develop a Telegram bot to accomplish just that. I built it gradually, and train the bot slowly but using my own way of thinking to chat with the member. This way, once it's done, the bot will be having all of my wisdom as consultant in remote work career.
    <br>The bot system is built using `python-telegram-bot` that in itself shipped with `tornado` web server. I run it inside a docker multicontainer for easy development and deployment, deployed in DigitalOcean. For the backend app, I am building a Django app for it, that communicate with the bot using `djangorestframework`.
