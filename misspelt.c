#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char words[10][10] = {"success", "succeed"};
    char inputword[10];
    printf("Enter the word ");
    scanf("%s", inputword);
    for(int i=0;i<2;i++){
        int len = strlen(words[i]);
        if(strlen(inputword)==len){
            int j=0,count=0;
            while (inputword[j]!='\0')
            {
                if(inputword[j]!=words[i][j])count++;
                j++;
            }
            printf("\nCorrect word is %s - cost(%d)",words[i],count);
        }
    }
    return 0;
}