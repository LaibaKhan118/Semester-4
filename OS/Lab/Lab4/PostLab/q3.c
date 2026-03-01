#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include<fcntl.h>
#include<sys/types.h>
#include<errno.h>

int main(int argc, char* argv[]) {
  if(argc != 3) {
    printf("Usage: %s \'path to source file\' \'path to destination file\'\n", argv[0]);
    return 1;
  }
  char* source = argv[1];
  char* dest = argv[2];
  int fd, fd2, n, m;
  char buffer[1024];
  fd = open(source, O_RDONLY);
  if(fd<0) {
    perror("Error opening source file");
    exit(EXIT_FAILURE);
  }
  fd2 = open(dest, O_WRONLY | O_CREAT | O_TRUNC, 0644);
  if(fd2<0) {
    perror("Error opening destination file");
    close(fd);
    exit(EXIT_FAILURE);
  }
  
  while ((n=read(fd, buffer, sizeof(buffer))) > 0) {
    m = write(fd2, buffer, n);
    if(m != n) {
      perror("Error in Read/Write");
      if (close(fd2) < 0) {
        perror("Error closing input file");
      }
      if (close(fd) < 0) {
          perror("Error closing output file");
      }
      exit(1);
    }
  }
  if (n == -1) {
      perror("Error reading from source file");
      if (close(fd2) < 0) {
        perror("Error closing input file");
      }
      if (close(fd) < 0) {
          perror("Error closing output file");
      }
      exit(1);
  }

    if (close(fd2) < 0) {
      perror("Error closing input file");
    }
    if (close(fd) < 0) {
        perror("Error closing output file");
    }
    printf("Contents successfully copied from %s to %s\n", argv[1], argv[2]);
  return 0;
}
