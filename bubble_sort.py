arr=[23,45,76,89,34,67,56,87,12,34,1,22,324,566,778,900] 
print(f"unsorted array {arr}")
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(f"sorted array using bubble sort method: {arr}")
