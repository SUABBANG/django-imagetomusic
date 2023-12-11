from django.db import models
import pandas as pd

class mp3_info(models.Model):
    TRACK_ID = models.CharField(max_length=255)
    MP3_URL = models.URLField()
    DURATION = models.IntegerField()
    TAGS = models.CharField(max_length=255)
    BPM = models.IntegerField()
    TEMPO = models.CharField(max_length=255)
    WEATHER = models.CharField(max_length=255)
    TIME = models.CharField(max_length=255)

    def __str__(self):
        return self.TRACK_ID

def upload_csv_to_database(csv_file_path):
    df = pd.read_csv(csv_file_path)
    for index, row in df.iterrows():
        your_model_instance = mp3_info(
            TRACK_ID=row['TRACK_ID'],
            MP3_URL=row['MP3_URL'],
            DURATION=row['DURATION'],
            TAGS=row['TAGS'],
            BPM=row['BPM'],
            TEMPO=row['TEMPO'],
            WEATHER=row['WEATHER'],
            TIME=row['TIME'],
        )
        your_model_instance.save()