#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RAND_MAX 1000

// Function prototypes
int GetNumSets(void);
int GetNumStartEndPts(void);
int GetNumPts(void);
double* CreateDataset(int nPts);
void SortArray(double* array, int nPts);
double Average(double* array, int nPts);

int main() {
    srand(time(NULL));

    int nSets = GetNumSets();
    double **dataSets = malloc(nSets * sizeof(double*));

    for (int i = 0; i < nSets; i++) {
        int nPts = GetNumPts();
        double* array = CreateDataset(nPts);
        SortArray(array, nPts);
        dataSets[i] = array;
    }

    for (int i = 0; i < nSets; i++) {
        int nPtsToPrint = GetNumStartEndPts();
        printf("Dataset %d: ", i + 1);
        for (int j = 0; j < nPtsToPrint; j++) {
            printf("%lf ", dataSets[i][j]);
        }
        printf("... Average: %lf\n", Average(dataSets[i], GetNumPts()));
    }

    // Free allocated memory
    for (int i = 0; i < nSets; i++) {
        free(dataSets[i]);
    }
    free(dataSets);

    return 0;
}

int GetNumSets(void) {
    return rand() % 6 + 5;
}

int GetNumStartEndPts(void) {
    return rand() % 3 + 2;
}

int GetNumPts(void) {
    return 1000 * (rand() % 8 + 4);
}

double* CreateDataset(int nPts) {
    double *array = malloc(nPts * sizeof(double));
    for (int i = 0; i < nPts; i++) {
        array[i] = rand() * 10.0 / RAND_MAX;
    }
    return array;
}

void SortArray(double* array, int nPts) {
    for (int i = 0; i < nPts - 1; i++) {
        for (int j = 0; j < nPts - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                double temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

double Average(double* array, int nPts) {
    double sum = 0.0;
    for (int i = 0; i < nPts; i++) {
        sum += array[i];
    }
    return sum / nPts;
}
