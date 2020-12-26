Lineª© ¥xÆW¹êªp¥D¤G¿ï¤@
«e¨¥
ªñ¦~¨Ó¡A¹êªpªº­·®ð¦b¥xÆW¶V¨Ó¶V²±¦æ¡A¦U¤j¥­¥x³£ª§¬Û¶}©l§ë¤J³o¶ô¡A¤£ºÞ¬OTwitch¡BYoutube¡BFacebook¡BIG¡K¡Kµ¥µ¥¡A¦Ó¤µ¤Ñ³o­Ó¹êªp¥D¤G¿ï¤@ªº©Ò¦³¹êªp¥D³£¬O¥xÆW¦³¦Wªº¹êªp¥D¡A¥D­n¬O¿ï¦ÛTwitch¥H¤ÎFacebook³o¨â¤j¥­¥x¡CÂÇ¥Ñ¦¹¥\¯à¨Ó¿ï¥X§A¤ß¥Ø¤¤ªº²Ä¤@¦W¡C
ºc·Q
¨Ï¥ÎButton¡BImageCarouse¡BTextMessage¹ê§@¥\¯à¡AÅý¨Ï¥ÎªÌ¥i¥Hª½±µÂI¨ú¦Û¤v³ßÅwªº¹êªp¡A¥H¤ÎÂ²³æªº¨Ï¥Î»y¥y¡AÅý¨Ï¥ÎªÌ¥i¥H¤è«Kªº¨Ï¥Î¡C

¨Ï¥Î»¡©ú
( °ò¥»¾Þ§@
1. ¿é¤J¡¨¶}©l ¡¨¡A§Y¥i¶}©l¤G¿ï¤@¥\¯à
2. ¿é¤J¡¨²á¤Ñ ¡¨¡A¥i¥H¦^ÂÐ»P±z¿é¤Jªº¬Û¦P¦r¥y
3. ÀH®É¥i¥H¿é¤J¡¨µ²§ô ¡¨¡A¦^¨ì³Ì¶}©lªºª¬ºA
4. ¶i¤J¤G¿ï¤@¥\¯à«á¡AÂI¿ï¹Ï¤ù¿ï¨ú§A³ß·Rªº¹êªp¥D


¨Ï¥Î½d¨Ò








³Ì«áªº¿ï¾Ü§¹ªºµ²ªG:





FSM

State»¡©ú
„H in : ¨Ï¥ÎªÌ¤@¶}©lªºª¬ºA¡A¿é¤J¡¨¶}©l ¡¨¶}©l¨Ï¥Î
„H choose : ¿ï¾Ü¹êªp¥Dªº©Ê§O
„H male: ¶i¤J¨k©Ê¹êªp¥D²Ä¤@½ü¤ñ¸û¨ú8±j
„H male2: ¶i¤J¨k©Ê¹êªp¥D²Ä¤G½ü¤ñ¸û¨ú4±j
„H male3: ¶i¤J¨k©Ê¹êªp¥D²Ä¤T½ü¸û¨ú«a¨È
„H male4: ¨ú¨k©Ê¹êªp¥D«a­x
„H female: ¶i¤J¤k©Ê¹êªp¥D²Ä¤@½ü¤ñ¸û¨ú8±j
„H female2: ¶i¤J¤k©Ê¹êªp¥D²Ä¤G½ü¤ñ¸û¨ú4±j
„H female3: ¶i¤J¤k©Ê¹êªp¥D²Ä¤T½ü¤ñ¸û¨ú«a¨È
„H female4: ¨ú¤k©Ê¹êªp¥D«a­x
„H final: Åã¥Ü³Ì«áªºµ²ªG

###?Upload?project?to?Heroku

1.?Add?local?project?to?Heroku?project

????heroku?git:remote?-a?{HEROKU_APP_NAME}

2.?Upload?project

????```
????git?add?.
????git?commit?-m?"Add?code"
????git?push?-f?heroku?master
????```

3.?Set?Environment?-?Line?Messaging?API?Secret?Keys

????```
????heroku?config:set?LINE_CHANNEL_SECRET=your_line_channel_secret
????heroku?config:set?LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
????```

4.?Your?Project?is?now?running?on?Heroku!

????url:?`{HEROKU_APP_NAME}.herokuapp.com/webhook`

????debug?command:?`heroku?logs?--tail?--app?{HEROKU_APP_NAME}`

5.?If?fail?with?`pygraphviz`?install?errors

????run?commands?below?can?solve?the?problems
????```
????heroku?buildpacks:set?heroku/python
????heroku?buildpacks:add?--index?1?heroku-community/apt
????```


