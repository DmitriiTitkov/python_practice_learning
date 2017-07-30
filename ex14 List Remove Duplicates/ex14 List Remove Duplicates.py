import random
import datetime


class ListDuplicatesRemoval:
    @staticmethod
    def remove_duplicates_set(input_list):
        if not isinstance(input_list, list):
            raise ValueError("Wrong argument passed to function. List expected")
        return set(input_list)

    @staticmethod
    def remove_duplicates_loop(input_list):
        if not isinstance(input_list, list):
            raise ValueError("Wrong argument passed to function. List expected")
        result_list = list()
        for number in input_list:
            if number not in result_list:
                result_list.append(number)
        return result_list


class ListDuplicatesRemovalTester:
    @staticmethod
    def run_tests(count_of_tests, lists_length, lists_range):
        # generate data
        print("Generating test data...")
        test_list_collection = list()
        for i in range(0, count_of_tests):
            test_list = list()
            for j in range(0, lists_length):
                test_list.append(random.randint(lists_range.start, lists_range.stop))
            test_list_collection.append(test_list)
        print("Complete\n")

        # run tests
        print("RUNNING TESTS \n")
        print("Testing list duplicate removal via set conversion:")
        start_test_time = datetime.datetime.now()
        for list_holder in test_list_collection:
            ListDuplicatesRemoval.remove_duplicates_set(list_holder)
        end_test_time = datetime.datetime.now()
        print(start_test_time, end_test_time, (end_test_time - start_test_time), sep="\n")

        print("\nTesting list duplicate removal via loop comparison:")
        start_test_time = datetime.datetime.now()
        for list_holder in test_list_collection:
            ListDuplicatesRemoval.remove_duplicates_loop(list_holder)
        end_test_time = datetime.datetime.now()
        print(start_test_time, end_test_time, (end_test_time - start_test_time), sep="\n")



# print(ListDuplicatesRemoval.remove_duplicates_loop([123, 163, 1, 123, 10, 10, 2, 2, 2, 1]))
ListDuplicatesRemovalTester.run_tests(20000, 500, range(1, 10))