#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
void init()
{
    srand(1);
    return ;
}
int randd()
{
    return rand()%10000;
}