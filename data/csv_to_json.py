import csv
import json

AD_MODEL = 'ads.ad'
CATEGORY_MODEL = 'ads.category'
LOCATION_MODEL = 'users.locations'
USER_MODEL = 'users.user'

def convert_file(csv_file, json_file, model):
    result = []

    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            record = {"model": model, "pk": row['id']}

            del row["id"]

            if "price" in row:
                row["price"] = int(row["price"])
                row["author_id"] = int(row["author_id"])
                row["category_id"] = int(row["category_id"])

            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                elif row["is_published"] == "FALSE":
                    row["is_published"] = False

            if 'lat' in row:
                row["lat"] = float(row["lat"])
                row["lng"] = float(row["lng"])

            if 'age' in row:
                row["age"] = int(row["age"])
                row["location_id"] = int(row["location_id"])


            record["fields"] = row
            result.append(record)

    with open(json_file, "w", encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_file("location.csv", "location.json", LOCATION_MODEL)
convert_file("user.csv", "user.json", USER_MODEL)
convert_file("ad.csv", "ad.json", AD_MODEL)
convert_file("category.csv", "category.json", CATEGORY_MODEL)
