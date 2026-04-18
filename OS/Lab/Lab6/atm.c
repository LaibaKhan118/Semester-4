#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>

#define REQ_FIFO "/temp/bank_req"
#define RES_FIFO "/temp/bank_res"

int main() {
	int req_fd, res_fd;
	char buffer[100], acc[20], pin[20];
	printf("Enter your account number: ");
	scanf("%s", acc);
	printf("Enter your pin: ");
	scanf("%s", pin);
	sprintf(buffer, "%s %s", acc, pin);
	red_fd=open(REQ_FIFO, O_WRONLY);
	write(req_fd, buffer, strlen(buffer)+1);
	close(req_fd);
	res_fd=open(RES_FIFO, O_RDONLY);
	read(res_fd, buffer, sizeof(buffer));
	printf("Server's Response: %s\n", buffer);
	close(res_fd);
	return 0;
}
