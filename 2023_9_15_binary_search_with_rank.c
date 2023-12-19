#include <stdio.h>
#include <stdlib.h>
# define INT_MAX 99999999

// use online c compiler: https://www.onlinegdb.com/online_c_compiler

/*
EX INPUT:
10 
15 
10 
1 
1 
1 
1 
2 
5 
6 
8 
8 
9 
0 
1 
2 
3 
4 
4 
5 
6 
7 
8 
8 
8 
9 
9 
9 
1 
2 
5 
6 
15 
17 
21 
22 
23 
25

EX OUTPUT:
Desired output:
low 0 high 1 i 0 j 1 a[0]=-99999999 b[1]=0 a[1]=1
b[1]=0 has rank 1
low 0 high 2 i 1 j 1 b[1]=0 a[1]=1 b[2]=1
a[1]=1 has rank 2
low 0 high 5 i 2 j 3 a[2]=1 b[3]=2 a[3]=1
low 3 high 5 i 4 j 1 b[1]=0 a[4]=1 b[2]=1
a[4]=1 has rank 5
low 0 high 6 i 3 j 3 a[3]=1 b[3]=2 a[4]=1
low 4 high 6 i 5 j 1 b[1]=0 a[5]=2 b[2]=1
low 4 high 4 i 4 j 2 a[4]=1 b[2]=1 a[5]=2
b[2]=1 has rank 6
low 0 high 10 i 5 j 10 a[5]=2 b[10]=8 a[6]=5
low 6 high 10 i 8 j 7 b[7]=5 a[8]=8 b[8]=6
low 6 high 7 i 6 j 9 a[6]=5 b[9]=7 a[7]=6
low 7 high 7 i 7 j 8 a[7]=6 b[8]=6 a[8]=8
b[8]=6 has rank 15
low 2 high 10 i 6 j 11 a[6]=5 b[11]=8 a[7]=6
low 7 high 10 i 8 j 9 b[9]=7 a[8]=8 b[10]=8
a[8]=8 has rank 17
low 6 high 10 i 8 j 13 a[8]=8 b[13]=9 a[9]=8
low 9 high 10 i 9 j 12 a[9]=8 b[12]=8 a[10]=9
b[12]=8 has rank 21
low 7 high 10 i 8 j 14 a[8]=8 b[14]=9 a[9]=8
low 9 high 10 i 9 j 13 a[9]=8 b[13]=9 a[10]=9
low 10 high 10 i 10 j 12 b[12]=8 a[10]=9 b[13]=9
a[10]=9 has rank 22
low 8 high 10 i 9 j 14 a[9]=8 b[14]=9 a[10]=9
low 10 high 10 i 10 j 13 a[10]=9 b[13]=9 a[11]=99999999
b[13]=9 has rank 23
low 10 high 10 i 10 j 15 a[10]=9 b[15]=9 a[11]=99999999
b[15]=9 has rank 25

*/


void binarySearch(int* a, int* b, int m, int n, int rank) {
  
    // high is now m, we are searching the array a (b is searched implicitly)
    int low = 0, high = m;
    
    // loop until low and high pointers cross
    while (low <= high) {
        int i = low + (high - low) / 2;   // safe midpoint calculation
        int j = rank - i - 1;             // -1 for 0 based indexing

        printf("low %d high %d i %d j %d a[%d]=%d b[%d]=%d\n", low, high, i, j, i, a[i], j, b[j]);   // print each iteration
        
        // check if j is valid index in array b
        // and check if a[i] is desired element
        if (j >= 0 && j < n && a[i] >= b[j] && (j == n - 1 || a[i] <= b[j + 1])) {
            // Element found in a
            printf("a[%d]=%d has rank %d\n", i, a[i], rank);
            return;
        } 
        
        // check if j is valid index in array b (again)
        // and check if b[j] is desired element
        else if (j >= -1 && j < n - 1 && b[j + 1] >= a[i] && (i == m - 1 || b[j + 1] <= a[i + 1])) {
            // Element found in b
            printf("b[%d]=%d has rank %d\n", j + 1, b[j + 1], rank);
            return;
        } 
      
        // adjust search range (a[i] > b[j] here, so high moves down)
        else if (j >= 0 && j <= n && a[i] > b[j]) {
            high = i - 1;
        } 
      
        // move low up
        else {
            low = i + 1;
        }
    }
}


int main() {
    int m, n, p;
    scanf("%d %d %d", &m, &n, &p);

    // Dynamically allocate arrays
    int* a = (int*)malloc((m + 2) * sizeof(int));
    int* b = (int*)malloc((n + 2) * sizeof(int));

    // Input sequences
    for (int i = 1; i <= m; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 1; i <= n; i++) {
        scanf("%d", &b[i]);
    }

    // Sentinel values
    a[0] = -INT_MAX;
    b[0] = -INT_MAX;
    a[m + 1] = INT_MAX;
    b[n + 1] = INT_MAX;

    // Perform binary searches for each rank
    for (int i = 1; i <= p; i++) {
        int rank;
        scanf("%d", &rank);
        binarySearch(a, b, m, n, rank);
    }

    // Free allocated memory
    free(a);
    free(b);

    return 0;
}