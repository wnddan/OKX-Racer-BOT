# api id, hash
API_ID=20745400
API_HASH="565fd03cdac90f75bff96707f68bd87d"

DELAYS = {
    'ACCOUNT': [5, 6],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [5, 5],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
}
# Use proxies or not
PROXY = True

# Play drop game
PLAY_GAMES = True

# points with each play game; max 280
POINTS = [240, 280]

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points']

# session folder (do not change)
WORKDIR = "sessions/"


ACCOUNT_PER_ONCE = 3
