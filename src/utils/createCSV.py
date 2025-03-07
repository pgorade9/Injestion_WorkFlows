def csv_writer():
    count_of_records = 20000
    FILE = "../input_files/csv_test_" + f"{count_of_records}" + ".csv"
    line_1 = "UWI,PARENT,WB_NAME,WB_NUM,SPUD_DATE,MD,TVD,OPERATOR,Longitude,Latitude,ELEVATION,ELEVATION UNIT,LEASE,FIELD,BASIN,FORMATION,COUNTRY,STATE"
    line_ref = "MS1000,SMP G099,MS11020,17-Jan-06,20960,20711,SCHLUMBERGER,-89.6661,27.85012,84,KB,SMP G099,ATWATER,AT,MIOCENE,USA,NORTHERN CALIFORNIA"
    with open(FILE, "w") as fp:
        fp.writelines([line_1, "\n"])
        # fp.write("\n")
        # fp.write(line_2)
        for i in range(20000):
            line_3 = "MS" + str(2000 + i) + "," + line_ref + "\n"
            fp.write(line_3)


csv_writer()

if __name__ == "__main__":
    csv_writer()
