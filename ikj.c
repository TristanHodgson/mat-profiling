#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv)
{

    int n = 500;

    if (argc > 1)
    {
        n = (int)strtol(argv[1], NULL, 10);
    }

    srand(time(NULL));

    float *A = malloc(n * n * sizeof(float));
    float *B = malloc(n * n * sizeof(float));
    float *C = malloc(n * n * sizeof(float));

    for (int i = 0; i < n * n; i++)
    {
        A[i] = (float)rand() / RAND_MAX;
    }
    for (int i = 0; i < n * n; i++)
    {
        B[i] = (float)rand() / RAND_MAX;
    }
    for (int i = 0; i < n * n; i++)
    {
        C[i] = 0.0f;
    }

    clock_t start, end;

    start = clock();

    for (int i = 0; i < n; i++)
    {
        for (int k = 0; k < n; k++)
        {
            for (int j = 0; j < n; j++)
            {
                C[i * n + j] += A[i * n + k] * B[k * n + j];
            }
        }
    }

    end = clock();

    printf("%f\n", (double)(end - start) / CLOCKS_PER_SEC);

    free(A);
    free(B);
    free(C);

    return 0;
}