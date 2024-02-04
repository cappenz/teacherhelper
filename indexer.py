import os.path

import dotenv
dotenv.load_dotenv()

from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

# check if storage already exists
if not os.path.exists("./storage"):
    # load the documents and create the index
    documents = SimpleDirectoryReader("transcripts").load_data()
    index = VectorStoreIndex.from_documents(documents,show_progress=True)
    # store it for later
    index.storage_context.persist()