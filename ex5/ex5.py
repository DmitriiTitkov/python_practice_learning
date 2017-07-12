import re
import random

class ListCompare:
    """According to exercise this class designed to compare lists and return list of matching list items.
        In addition this class could compare not only a pair of lists but as many as you pass.
        To generate random data you can use "from_random_data" class method

        # EXAMPLES: ###############################################################
        #
        #    list_compare = ListCompare.from_random_data(5, 5, 10)
        #    list_compare.compare_all_lists()
        #    list_compare.remove_all_lists()
        #    ListCompare.compare_lists([1, 2, 4], [5, 1, 6, 2], [6, 7, 1, 2])
        #
        ###########################################################################
    """
    def __init__(self, *lists):
        """Sets dynamic object properties given as parameters"""
        for listIndex in range(0, len(lists)):
            if isinstance(lists[listIndex], list) and len(lists[listIndex]) != 0:
                self.__setattr__("list" + str(listIndex), lists[listIndex])

    @classmethod
    def from_random_data(cls, count, len, celing):
        """generates random lists and runs constructor"""
        list_of_attributes = list()
        for index in range(0, count):
            list_attribute = list()
            for list_item_index in range(len):
                list_attribute.append(random.randint(0, celing))
            list_of_attributes.append(list_attribute)
            print(list_of_attributes)
        return cls(*list_of_attributes)

    def compare_all_lists(self):
        """Compare all lists assigned as dynamic properties by passing them as arguments to compare_lists static
        method"""
        attributes = dir(self)
        attribute_list_to_pass = list()
        for attribute in attributes:
            pattern = re.compile("list[0-9]")
            if pattern.match(attribute):
                attribute_list_to_pass.append(self.__getattribute__(attribute))
        print(attribute_list_to_pass)
        return self.compare_lists(*attribute_list_to_pass)

    def remove_all_lists(self):
        """Removes all dynamic list properties"""
        attributes = dir(self)
        for attribute in attributes:
            pattern = re.compile("list[0-9]")
            if pattern.match(attribute):
                delattr(self, attribute)

    @staticmethod
    def compare_lists(*lists_tuple):
        """Main comparison method. Takes multiple lists as parameters"""
        compare_result_list = list()
        lists = list(lists_tuple)
        if len(lists) != 0:
            while len(lists) != 0:
                if len(lists) == len(lists_tuple):
                    compare_result_list = lists.pop()[:]  # Have to slice list or it affects original tuple.
                list_to_compare = lists.pop()
                print(compare_result_list)
                for list_element in compare_result_list:
                    if list_element not in list_to_compare:
                        compare_result_list.remove(list_element)
            return set(compare_result_list)
        else:
            print("Nothing to compare")



