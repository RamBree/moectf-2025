#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
void init()
{
    srandom(time(0));
    return ;
}
int randd()
{
    return random()%114514;
}