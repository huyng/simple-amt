import json

target_brand = "Ford"
prototype = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ford_Motor_Company_Logo.svg/400px-Ford_Motor_Company_Logo.svg.png"
# "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Yahoo%21_logo.svg/1000px-Yahoo%21_logo.svg.png"

with open("/Users/hnguyen/Downloads/output_filtered.txt") as fh:
    i = 0
    for l in fh:
        pid, brand, url = l.strip().split(",")
        if brand == target_brand:
            print json.dumps({"brand": target_brand, "image": url, "prototype": prototype})
            i += 1
            if i > 50:
                break
