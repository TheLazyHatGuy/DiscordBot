import requests

url = "https://discordapp.com/api/channels/ChannelIdHere/messages"

payload = "{\r\n    \"embed\": {\r\n    \t\"description\": \"According to all known laws of aviation,\\n there is no way a bee should be able to fly.\\n Its wings are too small to get its fat little body off the ground.\\n The bee, of course, flies anyway because bees don't care what humans think is impossible.\\nYellow, black. Yellow, black.\\nYellow, black. Yellow, black.\\nOoh, black and yellow!\\nLet's shake it up a little.\\nBarry! Breakfast is ready!\\nOoming!\\nHang on a second.\\nHello?\\n- Barry?\\n- Adam?\\n- Oan you believe this is happening?\\n- I can't. I'll pick you up.\\nLooking sharp.\\nUse the stairs. Your father paid good money for those.\\nSorry. I'm excited.\\nHere's the graduate.\\nWe're very proud of you, son.\\nA perfect report card, all B's.\\nVery proud.\\nMa! I got a thing going here.\\n- You got lint on your fuzz.\\n- Ow! That's me!\\n- Wave to us! We'll be in row 118,000.\\n- Bye!\\nBarry, I told you, stop flying in the house!\\n\",\r\n    \t\"title\": \"Bee Movie pt1\"\r\n    }\r\n}"
headers = {
    'authorization': "Bot tokenhere",
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

payload = "{\r\n    \"embed\": {\r\n    \t\"description\": \"- Hey, Adam.\\n- Hey, Barry.\\n- Is that fuzz gel?\\n- A little. Special day, graduation.\\nNever thought I'd make it.\\nThree days grade school, three days high school.\\nThose were awkward.\\nThree days college. I'm glad I took a day and hitchhiked around the hive.\\nYou did come back different.\\n- Hi, Barry.\\n- Artie, growing a mustache? Looks good.\\n- Hear about Frankie?\\n- Yeah.\\n- You going to the funeral?\\n- No, I'm not going.\\nEverybody knows, sting someone, you die.\\nDon't waste it on a squirrel.\\nSuch a hothead.\\nI guess he could have just gotten out of the way.\\nI love this incorporating an amusement park into our day.\\nThat's why we don't need vacations.\\nBoy, quite a bit of pomp... under the circumstances.\\n- Well, Adam, today we are men.\\n- We are!\\n- Bee-men.\\n- Amen!\\nHallelujah!\\nStudents, faculty, distinguished bees, please welcome Dean Buzzwell.\\nWelcome, New Hive Oity graduating class of...\\n...9:15.\\nThat concludes our ceremonies.\\nAnd begins your career at Honex Industries!\\nWill we pick our job today?\\nI heard it's just orientation.\\nHeads up! Here we go.\\nKeep your hands and antennas inside the tram at all times.\\n\",\r\n    \t\"title\": \"Bee Movie pt2\"\r\n    }\r\n}"
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
