*************Command to Run in Hadoop**********

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input sample_weather.txt \
-output weather_output \
-mapper mapper.py \
-reducer reducer.py






**********Expected Output**********
Average Temperature: 30.9
Average Dew Point: 18.9
Average Wind Speed: 11.5