# sentiment_analysis/data_pipeline_project
Using twitter API as a source for data, I built a data pipeline to get tweets. 
The tweets are stored in mongoDB, I perfomed ETL job and sentiment analysis and then stored the results in Postgres database.
I used docker to build and run the pipeline successfully. Once I was able to store the results into Postgres, I connected Postgres to Metabase and generated visualizations and dashboard. 

Yes, I could have easily done the sentiment analysis without the extensive pipeline, but my main goal was not the sentiment analysis but to practise my data engineering skils.


### Tech stack, tools, and activities : tweepy(twitter API), Docker, mongoDB, Postgress, Metabase


