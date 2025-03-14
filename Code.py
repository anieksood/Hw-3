import pandas as pd
import numpy as np


# Calculate average likes by Platform and PostType
def create_social_media_avg():
    # Read the data
    df = pd.read_csv('socialMedia.csv')
    
    # Group by Platform and PostType, calculate average Likes
    avg_likes = df.groupby(['Platform', 'PostType'])['Likes'].mean().reset_index()
    
    # Rename column to AvgLikes and round to 2 decimal places
    avg_likes = avg_likes.rename(columns={'Likes': 'AvgLikes'})
    avg_likes['AvgLikes'] = avg_likes['AvgLikes'].round(2)
    
    # Save to CSV
    avg_likes.to_csv('SocialMediaAvg.csv', index=False)
    print("Created SocialMediaAvg.csv")


# Calculates average likes by Date
def create_social_media_time():
    # Read the data
    df = pd.read_csv('socialMedia.csv')
    
    # Group by Date, calculate average Likes
    avg_likes_by_date = df.groupby('Date')['Likes'].mean().reset_index()
    
    # Rename column to AvgLikes and round to 6 decimal places
    avg_likes_by_date = avg_likes_by_date.rename(columns={'Likes': 'AvgLikes'})
    avg_likes_by_date['AvgLikes'] = avg_likes_by_date['AvgLikes'].round(6)
    
    # Save to CSV
    avg_likes_by_date.to_csv('SocialMediaTime.csv', index=False)
    print("Created SocialMediaTime.csv")

# Run the functions to create the required CSV files
create_social_media_avg()
create_social_media_time()