#
#stuff for visuals
# Test of the D-ID API

import requests
import json
import os
from time import sleep
from dotenv import load_dotenv, find_dotenv

class DidHelper:
    def __init__(self,api_key:str) -> None:
        try:
            split_key = api_key.split(':')
            username = split_key[0]
            password = split_key[1]
        except Exception as e:
            raise 'API key should contain a colon. Format-> username:password'

        elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        elevenlabs_api_str = '{"elevenlabs" : "'+elevenlabs_api_key+'"}'

        self.username = username
        self.password = password
        self.base_url = 'https://api.d-id.com/'
        self.headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : 'Basic ' + username + ':' + password,
            'x-api-key-external': elevenlabs_api_str
        }

    def create_talk(self,img_url, script, voice):
        url = self.base_url + 'talks' 

        elevenlabs_voice_id = voice

        payload = {
            "source_url":img_url,
            "script": {
                "type": "text",
                "input": script,
                "provider": {
                    "type": "elevenlabs",
                    "voice_id": elevenlabs_voice_id
                },
            }            
        }

        response = requests.post(url, json=payload, headers=self.headers)
        print("Response from D-ID API:")
        print(response.json())

        try:
            id = response.json()['id']
        return id

    def get_talk(self, talk_id):
        url = self.base_url + 'talks/' + talk_id
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    # Generate a video from a script and an image and download it
    # to the local disk
    #
    # Inputs:
    #   img_url: the url of the image
    #   script: the text to be spoken in the video
    #   output_file: the name of the file to be saved

    def create_talk_and_download(self, img_url, text, output_file, voice):

        #call the api to make a talk from the img and text
        # eleven labs is called in backround to get the voice
        print('Calling DID API with text: '+text)
        did = DidHelper(os.getenv("DID_API_KEY"))
        id = did.create_talk(img_url, text, voice)

        #wait till talk = finalized (pole did api until vid = complete then get url)

        response_url = None
        counter = 0
        while response_url == None:
            sleep(1)
            print(f"Try to get result #{counter}")
            response = did.get_talk(id)
            if 'result_url' in response:
                response_url = response['result_url']
            else:
                print("result_url not found in the response")
            counter += 1

        print(f"Download URL {response_url}")

        #download the video from the url
        response = requests.get(response_url)
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
# Test code to run test out D-ID API

if __name__ == '__main__':
    # Get relevant keys and URLs from the environment file
    load_dotenv(find_dotenv())
    img_url = os.getenv("JUDITH_IMG")
    text = "chicken"
    output_file = 'output.mp4'
    voice = os.getenv("JUDITH_VOICE")
    did = DidHelper(os.getenv("DID_API_KEY"))
    did.create_talk_and_download(img_url, text, output_file, voice)

