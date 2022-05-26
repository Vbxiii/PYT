# # Create functions to calculate the following statistical measures

# 1. Mean
def mean (arr):
    return sum

# 2. Median
arr = [1,2,3,4,5]
arr [len(arr//2)]
arr [2] =3
n = len(arr)


def median(arr):
    # ''Return the median (meidan value) of numeric data. Hwen the number of data points is odd, return the middle data point; when the number of data points is even, the median is interpolated by taking the average of the two middle values'
sorted_data = sorted(arr)
n = len(sorted_data)
if n ==0
return "no median for empty dataset"
if n%2 == 1: #check if the total num of elements in array is odd
    return sorted_data[n/2]
else: #check if it is even
    i = n//2
    return (sorted_data[i-1] + sorted_data[i]) /2
# 3. Variance
# 4. Standard Deviation
# 5. Skewness