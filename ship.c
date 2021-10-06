#include <stdio.h>
#include <math.h>

float getdist(int x1, int x2, int y1, int y2)
{
    int xdiff = x1 - x2;
    int ydiff = y1 - y2;
    xdiff = xdiff * xdiff;
    ydiff = ydiff * ydiff;
    return sqrt(xdiff + ydiff);
}

int main()
{
    int n;
    int count = 0;
    scanf("%d", &n);
    int arrx[] = {5, 13, 6, 4};
    int arry[] = {2, 4, 2, 8};
    for (int i = 0; i < n; i++)
    {
        if (arrx[i] != -1)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (getdist(arrx[i], arrx[j], arry[i], arry[j]) <= 5)
                {
                    printf("(%d,%d),(%d,%d) will be destroyed\n", arrx[i], arry[i], arrx[j], arry[j]);
                    count += 1;
                    arrx[i] = arrx[j] = arry[i] = arry[j] = -1;
                    break;
                }
            }
        }
        if (arrx[i] != -1)
        {
            printf("(%d,%d) will be destroyed\n", arrx[i], arry[i]);
            count += 1;
        }
    }
    printf("No of bombs needed = %d", count);
    return 0;
}