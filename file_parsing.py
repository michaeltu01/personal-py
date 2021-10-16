# Exercise 22
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

def count_names():
    with open("../../nameslist.txt", "r") as nameslist:
        names = nameslist.readlines()
        for i in range(len(names)):
            names[i] = names[i].strip()

        # Put unique names into list
        unique_names = [names[0]]
        if_unique = True
        for name in names:
            for unique_name in unique_names:
                if(name == unique_name):
                    if_unique = False
                    break
                else:
                    if_unique = True
            if(if_unique):
                unique_names.append(name)

        # Count the number of occurances for each name
        count = 0
        for unique_name in unique_names:
            for name in names:
                if(name == unique_name):
                    count += 1
            print("The number of occurances for", unique_name, "is:", count)
            count = 0

def main():
    count_names()
    
if __name__ == "__main__":
    main()