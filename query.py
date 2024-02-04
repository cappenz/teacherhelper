#
# This script queries our index for a specific topic
#

import dotenv
dotenv.load_dotenv()

# Import frameworks
import os
from elevenlabs import generate, play
from llama_index import StorageContext, load_index_from_storage

# Import other part of the project
from voice import read_reply
from visuals import DidHelper
# load the existing index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Run in a loop asking for user input
while True:
    query = input("What would you like to know about? ")
    if query == "quit":
        break
    else:
        response = str(index.as_query_engine().query(query))
        print (response)
        #read_reply(response)
        #command visuals from query
        img_url = os.getenv("JUDITH_IMG")
        text = str(response)
        output_file = 'output.mp4'
        voice = os.getenv("JUDITH_VOICE")
        did = DidHelper(os.getenv("DID_API_KEY"))
        did.create_talk_and_download(img_url, text, output_file, voice)



