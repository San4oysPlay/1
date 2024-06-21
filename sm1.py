import requests
import json
link = "https://portal.avianik.com/rest/8/wnmsdwl9y8jllpqm/user.get"
body = {
    "FILTER": {
        "UF_DEPARTMENT": 273,
        "IS_ONLINE": "Y"
    },
    "SORT": {
        "LAST_NAME": "ASC"
    }
}
ans = requests.post(link, json=body)
print(ans.text)
