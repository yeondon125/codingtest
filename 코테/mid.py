def solution(array):
    sorted_array = sorted(array)
    answer = sorted_array[len(sorted_array)//2]
    return answer