#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    printf("Before Fork, pId=%d\n", getpid());
    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid == 0) {
      printf("I am a child process\nMy PId is %d\nMy Parent's PId is %d\n", getpid(), getppid());
    }
    else {
        wait(NULL);
        printf("I am a Parent Process\nMy PId is %d\nMy child's pId was %d\n", getpid(), pid);
    }
    return 0;
}
