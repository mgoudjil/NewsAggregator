###### NUXT SSR ######
# Cache data (for every subjects) : https://glitch.com/edit/#!/nuxt-cache-data?path=pages/index.vue:1:0
# Get new data every 30 mins
# 60% with best score, 30% random latest ones, 10%

###### MICROSERVICES ######

#### JOB 1:  Verify Each Source for data Every Hour  (PYTHON)

# 1 Start Script
# 2 Check if new data
# 3 Download data
# 4 Transform Data (Summarize, Translation, ...)
# 5 Add data to database

#### JOB 2:  Manage (GO Rest Api)
# 1 Get Corresponding DocId from LogFiles (If doesn't exit, get from database)
# 2 Updates values DocID : Score, Vote,FirstHour, etc
# 3 Write LogFiles
# 4 If last update > 30 min => Update Database


###### Interesting Website

