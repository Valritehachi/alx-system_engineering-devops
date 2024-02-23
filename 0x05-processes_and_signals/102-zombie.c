#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - ... 
 * Return: 0
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
 * main - ...
 * Return: 0
 */
int main(void)
{
	int y;
	pid_t zombie;

	for (y = 0; y < 5; y++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}
