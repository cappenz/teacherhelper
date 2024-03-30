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

def create_video_from_query(query,name):
    response = str(index.as_query_engine().query(query))
    print(response) 
    if name.lower() == "judith":
        voice = os.getenv("JUDITH_VOICE")
        img_url = os.getenv("JUDITH_IMG")
    elif name.lower() == "cynthia":
        voice = os.getenv("CYNTHIA_VOICE")
        img_url = os.getenv("CYNTHIA_IMG")
    else:
        print ("error: unknown teacher name {name}")
        return

    text = str(response)
    output_file = 'output.mp4'
    did = DidHelper(os.getenv("DID_API_KEY"))
    did.create_talk_and_download(img_url, text, output_file, voice)
    

# Run in a loop asking for user input
if __name__ == "__main__":
    while True:
        query = input("What would you like to know about? ")
        if query == "quit":
            break
        else:
            create_video_from_query(query, "Cynthia")
            print("Done!")


