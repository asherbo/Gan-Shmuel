#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
def direct_share(self, media_id, recipients, text=None):
    if not isinstance(recipients, list):
        recipients = [str(recipients)]
    recipient_users = '"",""'.join(str(r) for r in recipients)
    endpoint = 'direct_v2/threads/broadcast/media_share/?media_type=photo'
    boundary = self.uuid
    bodies = [
        {
            'type': 'form-data',
            'name': 'media_id',
            'data': media_id,
        },
        {
            'type': 'form-data',
            'name': 'recipient_users',
            'data': '[["{}"]]'.format(recipient_users),
        },
        {
            'type': 'form-data',
            'name': 'client_context',
            'data': self.uuid,
        },
        {
            'type': 'form-data',
            'name': 'thread',
            'data': '["0"]',
        },
        {
            'type': 'form-data',
            'name': 'text',
            'data': text or '',
        },
    ]
    data = self.buildBody(bodies, boundary)
    self.s.headers.update({'User-Agent': self.USER_AGENT,
                            'Proxy-Connection': 'keep-alive',
                            'Connection': 'keep-alive',
                            'Accept': '*/*',
                            'Content-Type': 'multipart/form-data; boundary={}'.format(boundary),
                            'Accept-Language': 'en-en'})
    # self.SendRequest(endpoint,post=data) #overwrites 'Content-type' header and boundary is missed
    response = self.s.post(self.API_URL + endpoint, data=data)

    if response.status_code == 200:
        self.LastResponse = response
        # self.LastJson = json.loads(response.text)
        return True
    else:
        print("Request return " + str(response.status_code) + " error!")
        # for debugging
        try:
            self.LastResponse = response
            # self.LastJson = json.loads(response.text)
        except:
            pass
        return False

from InstagramAPI import InstagramAPI
from usersAndPassword import passwordOf, pkOf
user = "mor._.bar"
InstagramAPI = InstagramAPI(user, passwordOf(user))
InstagramAPI.login()                         # login
mediaId = '2243538453327377884_212311211'    # a media_id
recipients = [212311211]         # array of user_ids. They can be strings or ints
from types import MethodType
InstagramAPI.direct_share = MethodType(direct_share, InstagramAPI)
InstagramAPI.direct_share(mediaId, recipients, text=' hi how r u https://www.instagram.com/mor_bargig  ')
