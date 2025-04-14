# التكليف 04
# قم بعمل Function تقوم بنفس آلية عمل ال all وقم بتسميتها my_all
# قم بعمل Function تقوم بنفس آلية عمل ال any وقم بتسميتها my_any
# قم بعمل Function تقوم بنفس آلية عمل ال min وقم بتسميتها my_min
# قم بعمل Function تقوم بنفس آلية عمل ال max وقم بتسميتها my_max
# تأكد ان my_min + my_max تقبل List أو Tuple
# my_all


def my_all(my_list):
    for i in my_list:
        if not i:
            return False
    return True


def my_any(my_list):
    for i in my_list:
        if i:
            return True
    return False


def my_min1(my_list):
    counter = 0
    for i in my_list:
        if i < my_list[counter]:
            counter += 1
            my_number = my_list[counter + 1]
    return my_number


def my_min2(iterable):
    # التحقق من أن المدخلات غير فارغة
    if not iterable:
        raise ValueError("my_min() arg is an empty sequence")
    min_value = iterable[0]
    for item in iterable:
        if item < min_value:
            min_value = item
    return min_value


def my_max(iterable):
    if not iterable:
        raise ValueError('Wrong Value')
    max_value = iterable[0]
    for number in iterable:
        if number > max_value:
            max_value = number
    return max_value

print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, False]))  # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min1([10, 100, -20, -100, 50]))  # -100
print(my_min1((10, 100, -20, -100, 50))) # -100
print(my_min2((10, 100, -20, -100,-900, 50))) # -100
print(my_min2((10, 100, -20, -100,-900, 50,-1500))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
