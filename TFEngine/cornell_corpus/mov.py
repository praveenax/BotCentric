with open('movie_titles_metadata.txt') as f:
   for l in f:
       print l.strip().split("+++$+++")
