import json

filename = 'valentines_tweets.json'

with open(filename, 'r') as f:


    users_with_geodata = {
        "data": []
    }
    all_users = []
    total_tweets = 0
    geo_tweets  = 0
    for line in f:
        tweet = json.loads(line)
        if tweet['user']['id']:
            total_tweets += 1
            user_id = tweet['user']['id']
            if user_id not in all_users:
                all_users.append(user_id)

                user_data= {
                    "user_id" : tweet['user']['id'],
                    "features" : {
                        "name" : tweet['user']['name'],
                        "id": tweet['user']['id'],
                        "screen_name": tweet['user']['screen_name'],
                        "tweets" : 1,
                        "location": tweet['user']['location'],
                    }
                }

                user_data1 = list(user_data)

                if tweet['coordinates']:
                      user_data["features"]["location"] = tweet['coordinates'][tweet['coordinates'][1]][1] + ", " + tweet['coordinates'][tweet['coordinates'][1]][0]
                      user_data["features"]["geo_type"] = "Tweet coordinates"
                elif tweet['place']:
                    user_data["features"]["primary_geo"] = tweet['place']['full_name'] + ", " + tweet['place']['country']
                    user_data["features"]["geo_type"] = "Tweet place"


                else:
                    user_data[1][4] = user_data[[1][4] +  user_data[1][4]
                    user_data["features"]["geo_type"] = "User location"


                if user_data["features"]["primary_geo"]:
                    users_with_geodata['data'].append(user_data)
                    geo_tweets += 1


            elif user_id in all_users:
                for user in users_with_geodata["data"]:
                   if user_id == user["user_id"]:
                      user["features"]["tweets"] += 1


    for user in users_with_geodata["data"]:
        geo_tweets = geo_tweets + user["features"]["tweets"]


    with open('valentines_tweets_loc_details_extract.json', 'w') as fout:
    fout.write(json.dumps(users_with_geodata, indent=4))