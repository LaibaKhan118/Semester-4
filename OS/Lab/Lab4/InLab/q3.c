#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>

void printUId() {
  printf("User ID = %d\n", getuid());
}
int main() {
	printf("ppid=%d\npid=%d\n", getppid(), getpid());
	printUId();
	return 0;
}
