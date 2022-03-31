def is_valid_input(input_data):
    if len(input_data) > 0:
        return True
    else:
        return False


def get_continuous_ranges(readings_list):
    if is_valid_input(readings_list):
        readings_list = sorted(readings_list)
        start_item = readings_list[0]
        end_item = readings_list[-1]

        unique_readings = set(readings_list)
        possible_ranges = range(start_item, end_item + 1)

        readings_not_in_range = set(possible_ranges) - unique_readings

        sliced_lists = []
        start = 0
        for i in sorted(readings_not_in_range):
            end = possible_ranges.index(i)
            sliced_lists.append(possible_ranges[start:end])
            start = end + 1
        sliced_lists.append(possible_ranges[start:])
        return print_list(sliced_lists, readings_list)
    else:
        return 'INVALID_INPUTS'


def get_valid_ranges(sliced_lists):
    for sliced_list in sliced_lists:
        if len(sliced_list) < 2:
            continue
        else:
            yield sliced_list


def print_list(sliced_lists, readings_list):
    ranges = []
    for found_range in get_valid_ranges(sliced_lists):
        count = 0
        for i in found_range:
            count = count + readings_list.count(i)
        ranges.append(f'{found_range[0]}-{found_range[-1]}, {count}')
    return ranges


def get_most_frequent_reading(readings_list):
    if is_valid_input(readings_list):
        return max(set(readings_list), key=readings_list.count)
    else:
        return 'INVALID_INPUTS'


def get_continuous_ranges_from_a2d_sensor(readings_list, no_of_bits, max_current_in_amp):
    if is_valid_input(readings_list):
        return get_continuous_ranges(convert_a2d_readings_into_current(readings_list, no_of_bits, max_current_in_amp))
    else:
        return 'INVALID_INPUTS'


def convert_a2d_readings_into_current(readings_list, no_of_bits, max_current_in_amp):
    threshold = get_threshold(no_of_bits)
    valid_readings = remove_error_readings(readings_list, threshold)
    readings_in_amps = [convert_a2d_to_amp(reading, threshold, max_current_in_amp) for reading in valid_readings]
    return readings_in_amps


def remove_error_readings(a2d_readings_list, threshold):
    valid_readings = [reading for reading in a2d_readings_list if threshold > reading >= 0]
    return valid_readings


def convert_a2d_to_amp(a2d_reading, threshold, max_current_in_amp):
    return round(max_current_in_amp * (a2d_reading / threshold))


def get_threshold(bits):
    return pow(2, bits) - 1
