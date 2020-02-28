# Array Structure

## The array represents the data structure consisting of numbers and corresponding data.
## 배열은 번호와 번호에 대응하는 데이터들로 이루어진 자료 구조를 나타낸다.

# ex) C language Arry

"""
#include <stdio.h>

int main(void){
    char arr[20];
}
"""

# Python dynamically allocates the length of the arrangement.
# 파이썬에서는 배열의 길이를 동적할당해준다.
arr = 'array'
print(arr)

arr = arr + "is Good"
print(arr)

# First Dimension list Array

array = [1, 2, 3, 4, 5]
print(array)

# Two Dimensional list Array

array_second = [[1,2,3,], [4,5,6,], [7,8,9]]
print(array_second[0])
print(array_second[0][0])

# dataset Count Frequency

dataset = ['Mikda', "list Mk", "What", "Bain sister eMa", "this Hour", "Live Computing", "List Models", "Django Admin", "Wakastring", "However", "Apple", "Mongo DB", "Maria DB", "Graphql"]

count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            count += 1

print(count)