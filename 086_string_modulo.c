#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);

    while (t-- > 0)
    {
        char str[100001];
        unsigned long long num, res = 0;

        scanf("%s %llu", str, &num);

        for (long long i = 0; i < strlen(str); i++)
        {
            res = (res * 10 + (str[i] - '0')) % num;
        }
        printf("%llu\n", res);
    }
    return 0;
}