#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/wait.h>
#define MAX 100

int main(int argc, char* argv[]) {
	if(argc != 2) {
	  printf("Usage: %s \'num1$num2$num3\'...\n", argv[0]);
          return 1;
	}
	int arr[MAX];
	int count=0;
	char input[1024];
	strcpy(input, argv[1]);
	
	char* token = strtok(input, "$");
	while(token && count < MAX) {
	  arr[count++] = atoi(token);
	  token=strtok(NULL, "$");
	}
	
	pid_t p1, p2, p3;
	p1=fork();
	if(p1 < 0) {
	  perror("Fork Failed!");
	  exit(EXIT_FAILURE);
	}
	if(p1 == 0) {
	  long int sum =0;
	  for(int i=0; i<count; i++) {
	    sum += arr[i];
	  }
	  printf("Sum = %ld\n", sum);
	  exit(0);
	}
	p2=fork();
	if(p2 < 0) {
	  perror("Fork Failed!");
	  exit(EXIT_FAILURE);
	}
	if(p2 == 0) {
	  long int sum =0;
	  for(int i=0; i<count; i++) {
	    sum += arr[i];
	  }
	  double avg= (double)sum/count;
	  printf("Average = %.2lf\n", avg);
	  exit(0);
	}
	p3=fork();
	if(p3 < 0) {
	  perror("Fork Failed!");
	  exit(EXIT_FAILURE);
	}
	if(p3 == 0) {
	  int max = arr[0];
	  for(int i=1; i<count; i++){
	    if(max < arr[i]){
	      max = arr[i];
	    }
	  }
	  printf("Max = %d\n", max);
	  exit(0);
	}
	
	wait(NULL);
	wait(NULL);
	wait(NULL);
	
	return 0;
}
