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
