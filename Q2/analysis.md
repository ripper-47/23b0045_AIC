# RAG:
### Retrieval-Augmented Generation (RAG) works as follows:
1. First it converts the required pdf into a markdown file from where the data is splitted in 'chunks'. My model uses **LLamaParse** to load the pdf, **UnstructuredMarkdownLoader** to load the markdown file and **RecursiveCharacterTextSplitter**  to split the data into chunks.
2. Each word is converted to word embeddings. Embeddings capture the similarities between the words. To get the embeddings i have used **FastEmbedEmbeddings** from huggingface and to store them in a database i have used **Qdrant**. The vector database allows for efficient similarity search accross the querry and the documents.
3. For retreiving relevant docs from the chunks, I have used **ContextualCompressionRetriever** which helps in compressing the retrieved docs and extracts only the relevant data.

# Attention Mechanism:
1. Attention mechanisms enable the model to weigh the importance of different parts of the input data, focusing on the most relevant information when generating responses.
2. They allow models to capture long-range relatons in the text, which is essential for maintaining context over longer conversations.

# Integration:
The retrievel component of the RAG pipeline provies the LLM with precise data. The attention mechanism then helps in determining the most relevant details from this retrieved data.

# Strengths:

1. Overall, the chatbot performed well on the queries related to the data it was asked. It almost always produced consise and relevant answer to the user's query.
2. The chatbot can further be trained on any data if required. Also updating the data is also easy aas we have to just update the pdf.


# Weakness:

1. One of the major drawbacks of this model is that it does not remember the conversation history between it and the user.
2. Sometimes the model outputs too much like when asked for revenue for meta in 2022, it answered "It does not have the data"(which is correct) but also gave revenue in 2023 and 2024 as well.

# Future Improvements In Conversational AI:
1. Several models like ChatGPT struggle with maintaining context over long-term conversations. Improving their memory mechanisms can help in remembering their past interactions quickly.
2. Integrating audio, video and visuals along with text can improve AI conversations drastically.
