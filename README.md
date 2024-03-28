Alpaca Dataset
=======================

The dataset contains 51,760 records with three field:

Instruction: This field contains textual instructions or prompts for a task or action. These instructions provide guidance or context for generating a response or completing a task.

Input: The input field is mainly empty string in this data. It may include additional information or details relevant to the task or action described in the instruction field.

Output: This field contains the desired output or response corresponding to the provided instruction and input. It represents the expected result or completion of the task described in the instruction field.


### Mapping json format into Dataset package
The json file is loaded as the pandas dataframe object first. The `dataframe_to_dataset` function is defined to convert a DataFrame into a datasets object.  This function creates a dictionary dataset_dict where each key in this dictionary corresponds to a column name in the original DataFrame, and the values are the respective column values. Using the Dataset.from_dict() method, a datasets object is created from the `dataset_dict`.


### Setup instruction format
`format_instruction` function formats the instruction and output according to the desired format. The function takes a single sample from the dataset, which typically consists of an instruction and its corresponding output. The formatted instruction section starts with the heading "Instruction:" followed by the actual instruction text provided in the sample. The formatted response section starts with the heading "Response:" followed by the output text corresponding to the instruction in the sample. The function returns the formatted instruction as a list containing a single string. The string includes both the instruction and output sections formatted as described above.

###  Model Training
The model training process described in the provided code snippet involves training a GPT-2 language model on a custom dataset using the SFT (Self-Finetuning) Trainer from the trl library. Pretrained GPT2 model and corresponding tokenizer is loaded. The pad token to the end-of-sequence (EOS) token is also loaded.

`SFTTrainer` instance is created with parameters:
- model: The pretrained GPT-2 model to be fine-tuned.
- train_dataset: The training dataset containing instruction-output pairs.
- tokenizer: The tokenizer used to tokenize the input data.
- max_seq_length: The maximum sequence length allowed for the input data.
- formatting_func: The function used to format the dataset samples.

The SFTTrainer instance is used to train the model on the provided training dataset. During training, the model learns to generate responses based on the input instructions provided in the dataset. The trainer iterates over the dataset, fine-tuning the GPT-2 model parameters to minimize the loss function and improve performance on the task.

The model and tokenizer is saved for later use.


### Model Evaluation

##### Evaluation Dstaset
The `Alpaca Evaluation` dataset comprises two main columns: instruction and output. The instruction column contains textual prompts or instructions provided to the model, outlining specific tasks or questions for the model to address. These instructions serve as the context for generating the corresponding responses. On the other hand, the output column contains the model-generated responses, representing completions or answers to the provided instructions. The size of the eval dataset is 805.


##### Evaluation Process
 - Iterate through the evaluation dataset to extract the instructions or prompts. These prompts serve as input to the language model for generating responses.

 - For each input prompt, encode it using the saved tokenizer and pass it to the saved language model for text generation. The generated response is then decoded using the tokenizer to convert it from token IDs to human-readable text. The generated responses are stored in a list.

 - Extract the gold labels (expected responses) from the evaluation dataset. Iterate through the generated responses and corresponding gold labels to compare them.

- Calculate 

    -   `Absolute Accuracy`: Calculate the percentage of correct predictions by counting the number of generated responses that match the gold labels.
    -   `Cosine Similarity Accuracy`: Calculate the cosine similarity between each generated response and its corresponding gold label. Sum up the similarity scores and divide by the total number of samples in the evaluation dataset to get the average cosine similarity accuracy.


##### Result
* Absolute Accuracy: 0.0
* Cosine Accuracy: 0.09083677505108742

The absolute accuracy, which measures the percentage of generated responses that exactly match the gold labels, is reported as 0.0. This suggests that none of the generated responses perfectly align with the expected outputs in the evaluation dataset.

On the other hand, the cosine accuracy, which assesses the similarity between the generated responses and the gold labels using cosine similarity, is calculated to be approximately 0.091. While this metric accounts for responses that may not match exactly but are semantically similar to the gold labels, the relatively low value implies that the generated responses still diverge significantly from the expected outputs in terms of their semantic relevance.

Task 4. Web Application
========================================

* **generate_text** function 
The generate_text function is responsible for generating text based on a given prompt using a pre-trained text generation model. The function initializes a text generation pipeline using the pipeline function from the Hugging Face transformers library. This pipeline facilitates text generation using a pre-trained language model along with its corresponding tokenizer.  Once the pipeline is set up, the function generates text by invoking the text_generator object with the provided prompt. It specifies parameters such as the maximum length of the generated text (max_length) and the number of sequences to return (num_return_sequences). In this case, it requests only one sequence. After text generation, the function extracts the generated text from the output dictionary obtained from the text_generator object. Specifically, it retrieves the `generated_text` field from the first sequence returned by the text generation process.

Return: Finally, the function returns the generated text as output, which can be further processed or displayed as needed.

##### **Overview**
This is flask web application consists of input box which allows users to input prompt text. After generating the text from the text generation model based on the given prompt the response box provides with the generated text.

- This web application consists of single web page - Home Page(*index.html*).

The application uses **generate.py**, which has the model that can provide gentle and informative answers
  

#### **Sample chats**

- Query 1:
    ![alt text](./app/static/text_g_1.png?raw=true)

- Query 2:
    ![alt text](./app/static/text_g_2.png?raw=true)

- Query 3:
    ![alt text](./app/static/text_g_3.png?raw=true)

- Query 4:
    ![alt text](./app/static/text_g_4.png?raw=true)

##### **Running the Application**
The Flask application is run using python app.py in the terminal, and the web interface can be accessed at http://127.0.0.1:5000/.

