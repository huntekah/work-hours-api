import csv 

def get_records():
    with open("hour_data.tsv") as f:
        reader = csv.reader(f, delimiter="\t")
        data_header = []
        for record in reader:
            if reader.line_num ==1:
                data_header.extend(record[:-1])
            else:
                data_object = {key:value for (key,value) in zip(data_header,record) }
                yield data_object


if __name__ == "__main__":
    for a in get_records():
        print(a)
        break
