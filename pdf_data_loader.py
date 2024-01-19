# Import necessary modules
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
import os
import threading

# Define paths
data_dir = 'data/'
faiss_db = 'vectorstore/db_faiss'

# Function to create a vector database
def create_vector_db():
    # Check if the directory exists, if not, create it
    if not os.path.exists(data_dir):
        os.makedirs(faiss_db)
    
    # Create a DirectoryLoader instance to load PDF documents
    loader = DirectoryLoader(data_dir,
                            glob='*.pdf',
                            loader_cls=PyPDFLoader,
                            use_multithreading=True)
    
    # Load documents from the directory
    document = loader.load()
    print('.....document_loaded.....')
    
    # Initialize a text splitter to divide documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                  chunk_overlap=100)
    print('.....document_splitter.....')
    
    # Split documents into smaller text chunks
    texts = text_splitter.split_documents(document)
    print('.....document_splitted.....')
    
    # Initialize HuggingFaceEmbeddings using a specific model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2',
                                      model_kwargs={'device': 'cpu'})
    print('.....document_embedded.....')
    
    # Create a vector store using FAISS from the text chunks and embeddings
    db = FAISS.from_documents(texts, embeddings)
    print('.....document_loaded_at_db.....')
    
    # Save the vector store locally
    db.save_local(faiss_db)

if __name__ == "__main__":
    # Create a new thread to execute the function
    document_thread = threading.Thread(target=create_vector_db)
    document_thread.start()
    document_thread.join()
