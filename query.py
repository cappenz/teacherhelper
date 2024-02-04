#
# This script queries our index for a specific topic
#

import dotenv
dotenv.load_dotenv()

# Import frameworks
from elevenlabs import generate, play
from llama_index import StorageContext, load_index_from_storage

# Import other part of the project
from voice import read_reply

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
        read_reply(response)



