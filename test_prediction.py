from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import pandas as pd

# Test data
data = CustomData(
    gender='male',
    race_ethnicity='group A',
    parental_level_of_education='high school',
    lunch='standard',
    test_preparation_course='none',
    reading_score=88.0,
    writing_score=59.0
)

pred_df = data.get_data_as_data_frame()
print("DataFrame:")
print(pred_df)

predict_pipeline = PredictPipeline()
results = predict_pipeline.predict(pred_df)
print("Prediction result:", results)
