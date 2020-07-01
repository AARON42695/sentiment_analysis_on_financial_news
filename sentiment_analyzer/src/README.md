
`Two_stage_flair_training.py`: This script is used train a given model in two phases (example code used to build GDP model).

`Load_and_predict.py`: This script is used to generate prediction results using trained models. User needs to download the model, and specify the directory of the model for prediction.

`generate_senti_df.py`: This script is used to generate one sentiment score for each article. And combine annotated articles and predicted articles into one big dataframe `combined_sentiment_data.csv` for visualization

`undersampling_on_indicator_and_split.py`: the script used to undersample training data in the second stage of model fine-tuning.

`Oversampling_on_indicator_and_split.py`: the script used to oversample training data in the second stage of model fine-tuning.


MODEL TRAINING NOTEBOOKS FOR REFERENCE:

`Employment_and_TSX_Two_stage_flair_training.ipynb`：ipython notebook that was used to train the models for employment and tsx datasets (best performance using undersampling dataset). 

`Interest_Rates_and_Housing_Two_stage_flair_training.ipynb`: ipython notebook that was used to train the models for interest rate and housing prices datasets (best performance using oversampling dataset).

`GDP_model_Two_stage_flair_training_and_error_analysis.ipynb`: ipython notebook that was used to train the models for GDP model (best performance using oversampling dataset). Includes error analysis at end of notebook.

`mortgagerates_model_Two_stage_flair_training_and_error_analysis.ipynb`: ipython notebook that was used to train the models for mortgage rate model (best performance using oversampling dataset). Includes error analysis at end of notebook.


