#SmashingFour Reddit Bot
Very simple bot that will reply to posts mentioning it with card stats.

Beware, the bot is currently rate-limited at 1 post each 10 minutes

### Reddit usage

Comment in r/smashingfour with 

`u/smashingfour_bot card:Barbarian`


### Bot usage
Create a credentials.py file that looks like this:

` 
client_id = 'reddit_app_client'

client_secret = 'reddit_app_secret'

username = 'your_reddit_username'

password = 'your_reddit_pass'

mashape_key = 'your_mashape_key'
`

Then run

`
pip install requirements.txt

python bot.py
`