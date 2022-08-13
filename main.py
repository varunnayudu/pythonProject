import json






def fetch_data_from_file(file_path):
    file = open(file_path)
    file_data = json.loads(file.read())
    # print(file_data)
    return file_data


def bmi_calculator(weight, height):
    _value = (weight / (height * height))
    return _value


def populate(_inputObj, _table_one):
    bmi = round(bmi_calculator(_inputObj['WeightKg'], (_inputObj['HeightCm'] * 0.01)), 2)
    #print("Bmi : ", bmi)
    # iterate through table to find the category and other details
    for table_one in _table_one:
        if float(table_one['bmi_range'].split(" ")[0]) < bmi:
            bmi_obj = table_one
        else:
            break
    _inputObj.update(bmi_obj)


def append_output_file(_inputObj, output_array):
    output_array.append(_inputObj)
    output_array_string = json.dumps(output_array)
    with open("output.txt", "w") as output_file:
        output_file.write(output_array_string)

def countOverweight(output_array):
    count=0
    for output in output_array:
        if output['bmi_category'] == 'Overweight' \
                or output['bmi_category'] == 'Severely obese' \
                or output['bmi_category'] == 'Very severely obese':
            count=count+1

    print('Overweight count :', count)






class BMI:
    def calculate(self):
        _input_records = fetch_data_from_file("input.txt")
        _table_one = fetch_data_from_file("table_one.txt")
        print('--start--')
        output_array=[]
        for _inputObj in _input_records:
            #print(_inputObj)
            populate(_inputObj, _table_one)
            #print(_inputObj)
            append_output_file(_inputObj,output_array)

        #print(output_array)
        print('..saving bmi calculate data into output.txt ')
        countOverweight(output_array)
        print('--complete--')

bmi = BMI()
bmi.calculate()