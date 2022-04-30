class Writing:
    def write(self, file_name, headers, list_data):
        # Write scraped data to a csv file (semicolon separated)
        f = open(f"{file_name}.csv", "w+", encoding="utf-8")  # open/create file and then append some item (a+)
        # headers = "Level 1;Level 2;Level 3\n"
        f.write(headers)
        for i in range(len(list_data)):
            f.write(f"{list_data[i]}\n")
        f.close()
