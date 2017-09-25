"""
Sample Input
ABCDCDC
CDC

Sample Output
2
"""

def count_substring(string, sub_string):
    count = 0
    index = -1
    while True:
        index = string.find(sub_string, index+1)
        if index == -1:
            break
        count+=1
    return count

if __name__ == '__main__':
    #string = input().strip()
    #sub_string = input().strip()
    #string = "ABCDCDC" #ininini
    string = "ininini"
    #sub_string="CDC"   #ini => 3
    sub_string="ini"
    count = count_substring(string, sub_string)
    print(count)