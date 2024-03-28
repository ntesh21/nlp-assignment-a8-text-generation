from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class TextGenerator:
    def __init__(self):
        # Load the saved model and tokenizer
        self.model_dir = '../models'
        self.model = AutoModelForCausalLM.from_pretrained(self.model_dir)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
        print("Model loaded successfully.")

    def generate_text(self, prompt):
        # Initialize the text generation pipeline
        text_generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
        # Text Generation
        generated_text = text_generator(prompt, max_length=512, num_return_sequences=1)[0]['generated_text']
        return generated_text

# if __name__ == "__main__":
#     # Input prompt
#     prompt = "Explain why the following fraction is equivalent to 1/4"
#     text_generator = TextGenerator()
#     generated_text = text_generator.generate_text(prompt)
#     print(generated_text)