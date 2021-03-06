# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with
	# the first element	
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")


/*
#include <bits/stdc++.h>
 
using namespace std;
 
struct Job
{
    char id;
    int dead, prof;
};
 
bool comparison(Job a, Job b)
{
    return (a.prof > b.prof);
}
void JobScheduling(Job arr[], int n)
{
    int maxDead = 0;
    // set maxDead
    for (int i = 0; i < n; i++)
    {
        if (maxDead <= arr[i].dead)
        {
            maxDead = arr[i].dead;
        }
    }
 
    char result[maxDead];
    
    bool slots[maxDead] = {false};
    
    sort(arr, arr + n, comparison);
 
    for (int i = 0; i < n; i++)
    {
        for (int j = min(maxDead, arr[i].dead) - 1; j >= 0; j--)
        {
            if (slots[j] == false)
            {
                slots[j] = true;
                result[j] = arr[i].id;
                break;
            }
        }
    }
    int sum=0;
    for (int i = 0; i < maxDead; i++) {
        cout << result[i] << " ";
    	sum += arr[i-1].prof;
    }
    cout<<endl<<"Total Profit: "<<sum;
}
int main()
{
    int n = 0;
    cout << "Enter the number of jobs: ";
    cin >> n;
    Job arr[n];
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the job id: ";
        cin >> arr[i].id;
        cout << "Enter the job deadline: ";
        cin >> arr[i].dead;
        cout << "Enter the job profit: ";
        cin >> arr[i].prof;
        cout << "\n";
    }
 
    JobScheduling(arr, n);
    return 0;
}
*/
