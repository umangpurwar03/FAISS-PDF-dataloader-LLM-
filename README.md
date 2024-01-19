
# FAISS PDF DataLoader for LangChain

This repository contains a Python script (`pdf_data_loader.py`) that showcases how to leverage LangChain for processing PDF files, extracting text content, and building a FAISS (Facebook AI Similarity Search) vector store. The script utilizes the LangChain library for text processing and vector storage while employing multithreading for parallel execution.

## Requirements

- **[LangChain](https://github.com/langchain-ai):** LangChain is a natural language processing library that supports document loading, text extraction, and vector storage.

  ```bash
  pip install langchain
  ```

- **[FAISS](https://github.com/facebookresearch/faiss):** FAISS is a library designed for efficient similarity search and clustering of dense vectors.

  ```bash
  pip install faiss
  ```

- **Additional requirements:** Install other dependencies by executing:

  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/umangpurwar03/FAISS-PDF-dataloader-LLM
    ```

2. Navigate to the repository directory:

    ```bash
    cd FAISS-PDF-dataloader-LLM
    ```

## Usage

1. Modify the `data_dir` variable in `pdf_data_loader.py` to indicate the directory containing your PDF files.

2. Run the script:

    ```bash
    python pdf_data_loader.py
    ```

    This script processes each PDF file concurrently using multithreading. It loads the data, extracts text content, generates embeddings using Hugging Face models, and ultimately stores the vectors in a FAISS vector store.

## Customization

- Customize the embedding model by modifying the `model_name` parameter during the initialization of `HuggingFaceEmbeddings`.

- Adjust the chunk size and overlap in the `RecursiveCharacterTextSplitter` initialization according to specific requirements.

- Feel free to customize other parameters and configurations based on your unique use case.

## Multithreading

The script employs multithreading to concurrently process multiple PDF files. The `process_pdf_files_in_parallel` function initiates a separate thread for each PDF file, facilitating efficient parallel processing. Adjust the number of threads based on system capabilities and requirements.

## [Excel DataLoader](https://github.com/umangpurwar03/FAISS-Excel-dataloader-LLM)

For a Excel data loader, refer to this [link](https://github.com/umangpurwar03/FAISS-Excel-dataloader-LLM).

## License

This code is released under the MIT License. Feel free to use and modify it as needed.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai)
- [FAISS](https://github.com/facebookresearch/faiss)

If you find this code helpful or have suggestions for improvement, please feel free to contribute or open an issue.
