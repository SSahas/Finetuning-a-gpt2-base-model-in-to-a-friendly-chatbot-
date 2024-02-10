# Improving-FLAN-t5-base-model-for-conversation


- Improving google/flan-t5-base model for conversation task.

- Used custom dataset for instruct fine tuning.Have a look at the datset : [daily_dialog](https://huggingface.co/datasets/daily_dialog)

- performed lora peft training for efficient training with low computation resources.

- Performed hyper parameter tuning for improving the peft model.

- Please have a look at training here : https://colab.research.google.com/drive/18ivkCHe_wdwRjSlFajYLXN4Vz0dmvr6_#


## To run the model locally
- Deployed google/flan-t5-base model on FastAPI. Inference.py is used to call this fastapi server and get the response.The model is able to remeber past conversational context and able to respond accordingly. Also added chatgpt like ui using streamlit framework.
- Clone the repository.
- Run the command - `uvicorn main:app --host localhost --port 8000`
- If the FastAPI server started succesfully , Run the command - `streamlit run inference.py`
