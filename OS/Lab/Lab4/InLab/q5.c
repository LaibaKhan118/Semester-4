#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/wait.h>
#include <errno.h>

int main() {
  int fd, fd2;
  char buffer[100];
  fd = open("input.txt", O_RDONLY);
  if(fd<0) {
    perror("Error opening input.txt");
    exit(EXIT_FAILURE);
  }
  fd2 = open("output.txt", O_WRONLY|O_CREAT, 0644);
  if(fd<0) {
    perror("Error opening input.txt");
    close(fd);
    exit(EXIT_FAILURE);
  }
  int n = read(fd, buffer, 98);
  if (n < 0) {
      perror("Error reading input.txt");
      if (close(fd) < 0) {
        perror("Error closing input file");
      }

      if (close(fd2) < 0) {
          perror("Error closing output file");
      }
      exit(EXIT_FAILURE);
  }

  int m = write(fd2, buffer, n);
  if(m < 0) {
    perror("Error writing to output.txt");
    if (close(fd) < 0) {
        perror("Error closing input file");
    }

    if (close(fd2) < 0) {
        perror("Error closing output file");
    }
    exit(EXIT_FAILURE);
  }
  if (close(fd) < 0) {
        perror("Error closing input file");
  }

  if (close(fd2) < 0) {
      perror("Error closing output file");
  }

  printf("File copied successfully.\n");

}

