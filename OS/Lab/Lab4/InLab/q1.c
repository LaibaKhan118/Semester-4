#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>

int main() {
	pid_t p1, p2;
	
	p1 = fork();
	if(p1 < 0) {
		perror("First Fork Failed!");
		exit(EXIT_FAILURE);
	}
	if(p1 == 0) {
		printf("\npid=%d\n", getpid());
		exit(EXIT_SUCCESS);
	}
	
	p2 = fork();
	if(p2 < 0) {
		perror("Second Fork Failed!");
		exit(EXIT_FAILURE);
	}
	if(p2 == 0) {
		printf("ppid=%d\n", getppid());
	}
	wait(NULL);
	wait(NULL);
	return 0;
}
