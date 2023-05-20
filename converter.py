

import datetime



def extract_timestamp(string_containing_timestamp): 
    """
    Method that extracts the timestamp from the string to make it easier for us to use it and convert. This takes string as parameter.\
    Since we know in the logs, the time stamp exist before : 
    we split the string occurence before and take the timestamp from there
    returns the time stamp extracted from string
    """
    timestamp = string_containing_timestamp.split(':')[0]
    return timestamp

def return_human_readable(timestamp):
    """
    This takes the timestamp which is in epoch format with decimal and converts into human readable format
    Returns the human readable timestamp
    
    """
    utc = datetime.datetime.utcfromtimestamp(float(timestamp))
    return utc.strftime('%a, %d %b %Y %H:%M:%S.%f UTC %Y')
    

def replace_logs_with_humanreadable_timestamp(original_string, original_time,actual_time):
    """
    Param1: Original string given by each line
    Param2: Original time which is epoch format
    Param3: Actual time which is in human readable

    This function replaces the epoch time with original time 
    returns the whole string after replacing epoch with human readable timestamp

    """
    return original_string.replace(original_time, actual_time)
    
file1 = open("log.txt", "r")
get_file_contents = file1.read()
get_timestamp = extract_timestamp(file1.read())

array = get_file_contents.split("delimeter")
for original_contents in get_file_contents.splitlines():
    print(replace_logs_with_humanreadable_timestamp(original_contents,
                                                           extract_timestamp(original_contents),
                                                          return_human_readable(extract_timestamp(original_contents))))
    
file1.close()


def test_extract_timestamp():
    test_data = '1554246802.464067: wlan0: State: SCANNING -> ASSOCIATING'
    assert(extract_timestamp(test_data) == '1554246802.464067')

def test_human_readable_conversion():
    test_data = '1554246802.464067'
    assert(return_human_readable(test_data) == 'Tue, 02 Apr 2019 23:13:22.464067 UTC 2019')

def test_replace_timestamp_to_human_readable():
    test_data = '1554246802.464067: wlan0: State: SCANNING -> ASSOCIATING'
    assert(replace_logs_with_humanreadable_timestamp(test_data, '1554246802.464067','Tue, 02 Apr 2019 23:13:22.464067 UTC 2019') == 'Tue, 02 Apr 2019 23:13:22.464067 UTC 2019: wlan0: State: SCANNING -> ASSOCIATING')
