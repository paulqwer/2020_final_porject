Line�� �x�W��p�D�G��@
�e��
��~�ӡA��p������b�x�W�V�ӶV����A�U�j���x�����۶}�l��J�o���A���ެOTwitch�BYoutube�BFacebook�BIG�K�K�����A�Ӥ��ѳo�ӹ�p�D�G��@���Ҧ���p�D���O�x�W���W����p�D�A�D�n�O���Twitch�H��Facebook�o��j���x�C�ǥѦ��\��ӿ�X�A�ߥؤ����Ĥ@�W�C
�c�Q
�ϥ�Button�BImageCarouse�BTextMessage��@�\��A���ϥΪ̥i�H�����I���ۤv���w����p�A�H��²�檺�ϥλy�y�A���ϥΪ̥i�H��K���ϥΡC

�ϥλ���
( �򥻾ާ@
1. ��J���}�l ���A�Y�i�}�l�G��@�\��
2. ��J����� ���A�i�H�^�лP�z��J���ۦP�r�y
3. �H�ɥi�H��J������ ���A�^��̶}�l�����A
4. �i�J�G��@�\���A�I��Ϥ�����A�߷R����p�D


�ϥνd��








�̫᪺��ܧ������G:





FSM

State����
�H in : �ϥΪ̤@�}�l�����A�A��J���}�l ���}�l�ϥ�
�H choose : ��ܹ�p�D���ʧO
�H male: �i�J�k�ʹ�p�D�Ĥ@�������8�j
�H male2: �i�J�k�ʹ�p�D�ĤG�������4�j
�H male3: �i�J�k�ʹ�p�D�ĤT�������a��
�H male4: ���k�ʹ�p�D�a�x
�H female: �i�J�k�ʹ�p�D�Ĥ@�������8�j
�H female2: �i�J�k�ʹ�p�D�ĤG�������4�j
�H female3: �i�J�k�ʹ�p�D�ĤT��������a��
�H female4: ���k�ʹ�p�D�a�x
�H final: ��̫᪺ܳ���G

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


