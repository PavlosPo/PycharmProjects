import random


class KinoEngine:

    def __init__(self, num):
        self.data_dict = {i: 0 for i in range(1, 81)}
        self.lucky_number = 0
        self.lucky_list = []
        self.lucky_dict = {i: 0 for i in range(1, 81)}
        self.updated_numbers_list_original = [i for i in range(1, 81)]
        self.updated_numbers_list = self.updated_numbers_list_original
        self.kino_engine()
        self.kino_simulation(num)

    def kino_engine(self):
        self.updated_numbers_list = [i for i in range(1, 81)]
        self.lucky_list.clear()
        for number_times in range(1, 21):
            for i in range(random.randint(1, 5)):
                self.lucky_number = random.choice(self.updated_numbers_list)
                # print(len(self.updated_numbers_list))
            # Updates the list with the numbers that they will random next loop
            self.updated_numbers_list.remove(self.lucky_number)

            self.lucky_list.append(self.lucky_number)
        # self.make_updated_numbers_list_original()
        # print('/Next Round')
        # print(self.lucky_list)
        return self.lucky_list

    def kino_simulation(self, num):
        for i in range(1, num):
            current_list = self.kino_engine()
            for num_in_list in current_list:
                # if num_in_list in self.data_dict:

                self.data_dict[num_in_list] += 1
            # self.make_updated_numbers_list_original()

    # def make_updated_numbers_list_original(self):
    #     self.updated_numbers_list = self.updated_numbers_list_original

    def return_tupple(self, num):
        temp = tuple(self.lucky_list)
        # print(temp)
        return temp[:num]