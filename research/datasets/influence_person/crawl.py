import twint
from pathlib import Path
from tqdm import tqdm

the_list = Path(__file__).parent / Path("non_salim.txt")
db = Path(__file__).parent / "non_salim.db"

with the_list.open() as f:
    for user in tqdm(f.readlines()):
        print(user)
        # remove '@' prefix
        user = user[1:]
        user = user.strip()

        # Configure
        c = twint.Config()
        c.Username = user
        # c.Followers = True
        # c.Following = True
        # c.Favorites = True
        # c.User_full = True
        # c.Retweets = True
        c.Since = "2020-01-01"
        # c.Store_csv = True
        c.Database  = str(db)
        # c.Output = f"datasets/salim/tweet_{user}.csv"
        # c.Limit = 100

        twint.run.Search(c)
        # break
