from googleapiclient.discovery import build
import pprint

my_api_key =  "AIzaSyA6Ct0AeVgAHnisijHVxVp005shP9lau0I" 
my_cse_id = "004729200286861094334:pr-szpcgj0s"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id,  **kwargs).execute()
    return res

results = google_search('testosterone site:www.google.com/patents/', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)
