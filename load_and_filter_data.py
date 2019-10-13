import csv
import pymysql
import os
    
# global variable
dataset_file_name = "/home/archit/Documents/STUDY/CCE_IISC/BasicsofDataAnalytics/dataset/delhi_weather_test.csv"
db = pymysql.connect("localhost", "root", "toortoor", "analytics")
cursor = db.cursor()
dataset_name = os.path.splitext(os.path.basename(dataset_file_name))[0]


class Wheather:

    def __init__(self):
        return

    def load_csv_file(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            temp_list = list(reader)
        return temp_list

    def filter_data(self, temp_data):
        length = len(temp_data)
        i = 0
        while i < length:
            temp_data[i].append(0)
            temp_data[i].append(0)
            i += 1
        return temp_data

    def create_structured_data(self, row_data):
        column_name = row_data[0]
        row_data.pop(0)
        for i in range(len(row_data)):
            for j in range(len(row_data[0])):
                if (row_data[i][j] == ''):
                    row_data[i][j] = 'NULL'
        return column_name, row_data

    def check_if_exists(self):
        check_table_str = "show tables like \"" + dataset_name + "\";"
        table_count = cursor.execute(check_table_str)
        return table_count

    def create_data_table(self, column_name):
        columns = " DOUBLE,".join(column_name) + " DOUBLE"
        create_table_str = "CREATE TABLE IF NOT EXISTS " + dataset_name + "(id int  NOT NULL AUTO_INCREMENT," + columns + ",PRIMARY KEY (id));"
        print ("create table query : "+create_table_str)
        cursor.execute(create_table_str)

    def insert_data_to_db(self, structured_data, column_name):
        count = 0
        columns = "`" + "`,`".join(column_name) + "`"
        for list in structured_data:
            values = ",".join(list)
            temp_str = "INSERT INTO `" + dataset_name + "` ( " + columns + ") VALUES (" + values + ") ;"
            cursor.execute(temp_str)
            count = count + 1
        cursor.execute("commit")
        return count



if __name__ == '__main__':
    my_weather = Wheather()
    row_data = my_weather.load_csv_file(dataset_file_name)
    column_name, structured_data = my_weather.create_structured_data(row_data)
    print("column name " + str(column_name))
    if (my_weather.check_if_exists()):
        print("The table already exists. Overwriting content ...")
    else:
        my_weather.create_data_table(column_name)
        print("Table created: " + dataset_name)
    inserted_rows_count = my_weather.insert_data_to_db(structured_data, column_name)
    print("Number of rows inserted :" + str(inserted_rows_count))
