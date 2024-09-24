import fitz
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from resume_filter_API.Configuration import google_prompt
from resume_filter_API.operation.CRUD import update_answer_in_table
from resume_filter_API.operation.GoogleAI import google_gen_AI_response


def create_embeddings(text_chunks):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(text_chunks)
    return embeddings


def split_text_into_chunks(text: str, chunk_size=1000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


# Step 4: Store embeddings in FAISS
def store_embeddings_in_faiss(embeddings):
    # Create a FAISS index (L2 norm)
    dimension = embeddings.shape[1]  # Embedding size
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)  # Add embeddings to the FAISS index
    return index


def pdf_to_text(pdf_path: str):
    try:
        # Open the PDF file in read-binary mode
        text_chunks = []
        doc = fitz.open(pdf_path)

        for page in doc:
            # Get the text for the current page
            page_text = page.get_text()
            # Split the page text into chunks
            chunks = split_text_into_chunks(page_text)
            text_chunks.extend(chunks)

        chunks = split_text_into_chunks(text_chunks)

        embeddings = create_embeddings(chunks)
        index = store_embeddings_in_faiss(np.array(embeddings))

        return text_chunks

        return chunks
    except Exception as e:
        print(e)


def get_answer_from_gen_AI(original_question: str, original_file_text: str):
    final_response = None
    try:
        final_answer = google_gen_AI_response(model_prompt=google_prompt, input_data_from_user=original_file_text,
                                              question=original_question)
        if final_answer:
            # save file in db
            updated_response = update_answer_in_table(question_data=original_question, answer_data=final_answer)
            if updated_response:
                final_response = {"answers": updated_response["answers"], "qa_id": updated_response["qa_id"], \
                                  "question": updated_response["question"]}
        return final_response

    except Exception as e:
        print(e)

# if __name__ == "__main__":
#     pdf_to_text(
#         pdf_patgetvh="C:\\Users\\ADMIN\\Documents\\Workarea\\ml_project_resume\\temporary_path\\DhanshreePatangrao_Resume.pdf")

# if __name__ == "__main__":
#     file_process(
#         file_path="C:\Users\ADMIN\Documents\Workarea\ml_project_resume\temporary_path\DhanshreePatangrao_Resume.pdf")
