#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid == 0) {
        printf("Child: running 'mkdir testdir', pid=%d, ppid=%d\n", getpid(), getppid());
        execlp("mkdir", "mkdir", "testdir", (char *) NULL);
        perror("execlp failed");
        exit(EXIT_FAILURE);
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }
    
    pid_t pid1 = fork();
    if (pid1 < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid1 == 0) {
        printf("Child: running 'cp input.txt testdir/input.txt', pid=%d, ppid=%d\n", getpid(), getppid());
        execlp("cp", "cp", "input.txt", "testdir/input.txt", NULL);
        perror("execlp failed");
        exit(EXIT_FAILURE);
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }
    pid_t pid2 = fork();

    if (pid2 < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid2 == 0) {
        printf("Child: running 'ls -l', pid=%d, ppid=%d\n", getpid(), getppid());
        execlp("ls", "ls", "-l", NULL);
        perror("execlp failed");
        exit(EXIT_FAILURE);
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }
    pid_t pid3 = fork();

    if (pid3 < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid3 == 0) {
        printf("Child: running 'rmdir testdir', pid=%d, ppid=%d\n", getpid(), getppid());
        execlp("rm", "rm", "-rf", "testdir", (char*) NULL);
        perror("execlp failed");
        exit(EXIT_FAILURE);
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }
    return 0;
}
