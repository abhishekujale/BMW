# Use a pipeline as a high-level helper
from transformers import pipeline

ds = load_dataset("akritRihal/Indian_Sign_Language_dataset")
from datasets import load_dataset

pipe = pipeline("image-classification", model="Hemg/Indian-sign-language-classification")

# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("Hemg/Indian-sign-language-classification")
model = AutoModelForImageClassification.from_pretrained("Hemg/Indian-sign-language-classification")