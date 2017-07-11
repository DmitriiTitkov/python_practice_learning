import re


class ListCompare:
    """Accoring to exercise this class designed to compare lists and return list of matching list items.
        In addition this class could compare not only a pair of lists but as many as you pass.
        To generate
    """
    def __init__(self, *lists):
        for listIndex in range(0, len(lists)):
            if isinstance(lists[listIndex], list) and len(lists[listIndex]) != 0:
                self.__setattr__("list" + str(listIndex), lists[listIndex])

    @classmethod
    def from_random_date(cls):
        

    def compare_all_lists(self):
        attributes = dir(self)
        attribute_list_to_pass = list()
        for attribute in attributes:
            pattern = re.compile("list[0-9]")
            if pattern.match(attribute):
                attribute_list_to_pass.append(self.__getattribute__(attribute))
        print(attribute_list_to_pass)
        return self.compare_lists(*attribute_list_to_pass)

    @staticmethod
    def compare_lists(*lists):
        compare_result_list = list()
        lists = list(lists)
        if len(lists) != 0:
            while len(lists) != 0:
                if len(compare_result_list) == 0:
                    compare_result_list = lists.pop()
                list_to_compare = lists.pop()
                print(compare_result_list)
                for list_element in compare_result_list:
                    if list_element not in list_to_compare:
                        compare_result_list.remove(list_element)
            return compare_result_list
        else:
            print("Nothing to compare")



