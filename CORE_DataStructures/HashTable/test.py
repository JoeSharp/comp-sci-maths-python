import unittest
from CORE_DataStructures.HashTable.HashTable import HashTable
from CORE_DataStructures.HashTable.hashFunction import hash_function


class TestStringMethods(unittest.TestCase):

    def test_hash_function(self):
        print("Hashing Days of the Week")

        our_range: int = 100

        for day_of_week in ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]:
            h: int = hash_function(day_of_week, our_range)
            print("Hash of {} : {}".format(day_of_week, h))

    def test_hash_table(self):

        my_hash_table: HashTable[str] = HashTable(5)  # small capacity to ensure clashing

        for day_of_week in ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]:
            my_hash_table.add_item(day_of_week)

        print("\nTested Hash Table {}".format(my_hash_table))


if __name__ == '__main__':
    unittest.main()
