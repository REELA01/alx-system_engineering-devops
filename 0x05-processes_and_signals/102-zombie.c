#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - create an infinite loop
 * Return: 0 always
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - create fuve if zombie prossec
 * Return: 0 always
*/
int main(void)
{
	int j;
	pid_t zombie;

	for (j = 0; j < 5; j++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
