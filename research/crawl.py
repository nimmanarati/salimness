import twint
from pathlib import Path

salim_list = Path(__file__).parent / Path("sample_salim.txt")
db = Path(__file__).parent / "datasets/salim/salim_tweet.db"

with salim_list.open() as f:
    for user in f.readlines():
        print(user)
        # remove '@' prefix
        user = user[1:]
        user = user.strip()

        # Configure
        c = twint.Config()
        c.Username = user
        # c.Store_csv = True
        c.Database  = str(db)
        # c.Output = f"datasets/salim/tweet_{user}.csv"
        c.Limit = 100
        
        twint.run.Search(c)