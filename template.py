import json
import os

def create_device_unique_id(device_type,device_address):
    # 创建一个device_unique_id
    # 然后存到Flash里
    # device_unique_id | device_address
    # 0001             | 201888888888
    # return device_unique_id
    pass

def create_unique_id_to_address(device_type,from_address):
    # 创建一个unique_id
    # 创建一个lite modbus address
    # 然后存到Flash里
    # unique_id | fc | from_address | device_id | to_address
    # 0001      | 01 | 40001:1      | 1         | 410001:1
    # return device_unique_id
    pass




def read_read():
    print('rr')

def post_device(device_type, device_address):
    if device_type == '1':
        print('Device Type:', device_type, ', Create a entry at table/flash for DLT645 device at device_address, ', device_address)
        device_unique_id = create_device_unique_id(device_type, device_address)
    elif device_type == '2':
        device_unique_id = create_device_unique_id(device_type, device_address)
        print('Device Type:', device_type, ', Create a entry at table/flash for ModbusTCP device at device_address, ', device_address)


def modify_device(device_type, device_unique_id, device_address):
    if device_type == '1':
        print('Device Type:', device_type, ', Change entry at table/flash for DLT645 device to, ', device_address, 'by select device_unique_id, ', device_unique_id)
    elif device_type == '2':
        print('Device Type:', device_type, ', Change entry at table/flash for ModbusTCP device to, ', device_address, 'by select device_unique_id, ', device_unique_id)


def del_device(device_type, device_unique_id):
    if device_type == '1':
        print('Device Type:', device_type, ', Delete entry at table/flash for DLT645 device by select device_unique_id, ', device_unique_id)
    elif device_type == '2':
        print('Device Type:', device_type, ', Delete entry at table/flash for ModbusTCP by select device_unique_id, ', device_unique_id)


def post_address(device_type, from_address):
    if device_type == '1':
        print('Device Type:', device_type, ', Create a local ModbusTcp address at table/flash for DLT645 device to pair from_address, ', from_address)
    elif device_type == '2':
        print('Device Type:', device_type, ', Create a local ModbusTcp address at table/flash for ModbusTCP device to pair from_address, ', from_address)


def modify_address(device_type, unique_id, from_address):
    if device_type == '1':
        print('Device Type:', device_type, ', Change entry at table/flash for DLT645 device to pair from_address, ', from_address, 'by select unique_id, ', unique_id)
    elif device_type == '2':
        print('Device Type:', device_type, ', Change entry at table/flash for ModbusTCP device to pair from_address, ', from_address, 'by select unique_id, ', unique_id)


def del_address(device_type, unique_id):
    if device_type == '1':
        print('Device Type:', device_type, ', Delete entry at table/flash for DLT645 device by select unique_id, ', unique_id)
    elif device_type == '2':
        print('Device Type:', device_type, ', Delete entry at table/flash for ModbusTCP by select unique_id, ', unique_id)




function_code = {'rr':read_read,
                 'pd':post_device,
                 'pa':post_address,
                 'md':modify_device,
                 'ma':modify_address,
                 'dd':del_device,
                 'da':del_address}

devide_type = {1:'dlt645', 2:'modbusTCP'}
status_code = {200:'Ok', 400:'Error'}

iterate_file_name = ['pd.1.json', 'pa.1.json', 'md.1.json', 'ma.1.json', 'dd.1.json', 'da.1.json',
                     'pd.2.json', 'pa.2.json', 'md.2.json', 'ma.2.json', 'dd.2.json', 'da.2.json']

for file_name in iterate_file_name:


    dir = './jsonData/'
    file= file_name

    full_path=os.path.join(dir,file)


    with open(full_path, 'r') as f:
        json_data = json.load(f)

    print('------------------read {0}-----------------{1}'.format(full_path, json_data))
    json_function_code = json_data['fc']
    if json_function_code == 'pd':
        json_device_type = json_data['dt']
        json_device_address = json_data['dadd']
        function_code[json_function_code](json_device_type, json_device_address)
    elif json_function_code == 'md':
        json_device_type = json_data['dt']
        json_device_unique_id = json_data['did']
        json_device_address = json_data['dadd']
        function_code[json_function_code](json_device_type, json_device_unique_id, json_device_address)
    elif json_function_code == 'dd':
        json_device_type = json_data['dt']
        json_device_unique_id = json_data['did']
        function_code[json_function_code](json_device_type, json_device_unique_id)
    elif json_function_code == 'pa':
        json_device_type = json_data['dt']
        json_from_address = json_data['fa']
        function_code[json_function_code](json_device_type, json_from_address)
    elif json_function_code == 'ma':
        json_device_type = json_data['dt']
        json_unique_id = json_data['id']
        json_from_address = json_data['fa']
        function_code[json_function_code](json_device_type, json_unique_id, json_from_address)
    elif json_function_code == 'da':
        json_device_type = json_data['dt']
        json_unique_id = json_data['id']
        function_code[json_function_code](json_device_type, json_unique_id)






