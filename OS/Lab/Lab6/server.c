#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define REQ_FIFO "/tmp/bank_req"
#define RES_FIFO "/temp/bank_res"

int main() {
	int req_fd, res_fd;
	char buffer[100], accNum[20], pin[20];
	mkfifo(REQ_FIFO, 0644);
	mkfifo(RES_FIFO, 0644);
	printf("Server listening...\n");
	while(1){
		req_fd=open(REQ_FIFO, O_RDONLY);
		read(req_fd, buffer, sizeof(buffer));
		close(req_fd);
		sscanf(buffer, "%s %s", accNum, pin);
		printf("Received: Acc=%s, Pin=%s\n",accNum, pin);
		char response[100];
		if(strcmp(accNum, "1234")==0 && strcmp(pin, "1234")==0){
			strcpy(response, "Valid, Balance: $5000");
		} else {
			strcpy(response, "Invalid Credentials");
		}
		res_fd=open(RES_FIFO, O_WRONLY);
		write(res_fd, response, strlen(response)+1);
		close(res_fd);
	}
	return 0;
}