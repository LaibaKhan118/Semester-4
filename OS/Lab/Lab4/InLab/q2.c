#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>

int main() {
	pid_t p1;
	
	p1 = fork();
	if(p1 < 0) {
		perror("Fork Failed!");
		exit(EXIT_FAILURE);
	}
	if(p1 == 0) {
		for(int i=0; i<100; i++) {
		  printf("I am a child process\n");
		}
		exit(EXIT_SUCCESS);
	}
	for(int i=0; i<100; i++) {
	  printf("I am a parent process\n");
	}
	return 0;
}
