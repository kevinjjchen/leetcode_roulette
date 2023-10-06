import random

class RandomSelector:
    def __init__(self):
        self.leetcode_dict = {}
        
    def add_leetcode(self, leetcode):
        self.leetcode_dict[leetcode.id] = leetcode
    
    def random_leetcode_id(self):
        ids = list(self.leetcode_dict.keys())
        selected_id = random.choice(ids)
        return (self.leetcode_dict[selected_id].id, self.leetcode_dict[selected_id].name)

    def show_hint(self, id):
        return self.leetcode_dict[id]

class Leetcode:
    def __init__(self, number, name, category):
        self.id = number
        self.name = name
        self.category = category

def main():
    curr_category = ""
    random_selector = RandomSelector()
    with open("leetcode.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line[0].isalpha():
                curr_category = line
            else:
                number, name = line.split(". ")
                temp_leetcode = Leetcode(number, name, curr_category)
                random_selector.add_leetcode(temp_leetcode)
    selected_id, selected_name = random_selector.random_leetcode_id()
    print("The selected leetcode is: " + selected_id + " " + selected_name)
    user_input = input("Do you want to see the hint? (y/n)")
    if user_input == "y":
        hint = random_selector.show_hint(selected_id)
        print(hint.category)
        print("Good luck!")
    else:
        print("Good work!")
    
if __name__ == "__main__":
    main()