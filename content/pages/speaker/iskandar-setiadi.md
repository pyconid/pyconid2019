title: Speaker Detail
Template: speaker-detail
slug: speaker/iskandar-setiadi
talk_title: Python Website is Slow? Think Again!
talk_language: English
speaker_name: Iskandar Setiadi
speaker_photo: /images/speakers/iskandar-setiadi.jpg
speaker_organization: HENNGE, K.K.
short_bio: Software engineer working for HENNGE, K.K. in Tokyo, Japan. Anime lovers.
short_intro: In this talk, we will briefly explore how we achieved 60% cost savings and improved our Python website response time from 400 ms to 150 ms.
speaker_website: https://github.com/freedomofkeima
speaker_ppt: https://drive.google.com/file/d/0B46IJwutRDjLZUwzRVVDbGRVdmZ5Smh3b043MzNwT1RMYU9F/view
speaker_video_id: pPLOGoqjtgA
speaker_bio: I am an Indonesian software engineer working for HENNGE, K.K. in Tokyo, Japan. In the past 3 years, I have given talks at several PyCons around the globe (Japan, Italy, Hong Kong, Indonesia, etc).
speaker_abstract: As a Python avid user, we read a lot of articles that describe Python as a slow, interpreted language. At a certain point, some people start to blame the language itself for performance problems and consider to migrate their codebase to other languages. However, the success story of Instagram in handling four hundred million users has shown us that Python is not the bottleneck, but our codebase is.
    <br>In this talk, the speaker will share a tale of improving Python website performances in medium-sized enterprise (serving million users) that I’m currently working at. In a year, we finally achieved speed improvement from the average response time of 400 ms to 150 ms per request and we could save around $100k per year in AWS EC2 instance provisioning, which is around 60% of total cost.
    <br>Several key points that we have learned from our development process includes:<br>
    - Tracking database queries with Python decorator will reduce number of unnecessary queries
    - Using an async framework does not guarantee your codebase is implementing it correctly
    - Default configured third-party library is not always suitable for all use cases
    - Utilizing memory profiler and pdb properly will help you in pinpointing application bottleneck
    - Python for-loops vs generators
    - And several other common pitfalls
