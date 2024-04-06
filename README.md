# Finetuning a gpt2 base model in to a friendly chatbot.


- Improving openai_community/gpt2_medium model for conversation task.

- Used custom dataset for instruct fine tuning.Have a look at the datset : [daily_dialog](https://huggingface.co/datasets/daily_dialog)

- performed lora peft training for efficient training with low computation resources.

- Performed hyper parameter tuning for improving the peft model.

- Please have a look at training notebok here : [[https://colab.research.google.com/drive/1LsGSPYI26tMu2hYBoFT0PaRdF5WZDzuo](https://colab.research.google.com/drive/1LsGSPYI26tMu2hYBoFT0PaRdF5WZDzuo)]

- Try the app here : [[SSahas/friendly_chat_bot](SSahas/friendly_chat_bot)]
## To run the model locally
- Deployed openai_community/gpt2_medium model on FastAPI. Inference.py is used to call this fastapi server and get the response.
- Clone the repository.
- Run the command - `uvicorn main:app --host localhost --port 8000`
- If the FastAPI server started succesfully , Run the command - `streamlit run inference.py`
