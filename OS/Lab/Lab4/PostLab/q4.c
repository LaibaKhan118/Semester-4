#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/stat.h>
#include<dirent.h>
#include<string.h>

void listDir(char* path) {
  DIR *dir;
  struct dirent *entry;
  dir=opendir(path);
  if(dir == NULL) {
    perror("Error in opening Directory");
    exit(EXIT_FAILURE);
  }
  while((entry=readdir(dir))!=NULL) {
    if(strcmp(entry->d_name, ".")==0 || strcmp(entry->d_name, "..")==0) {continue;}
    
    char fullPath[1024];
    sprintf(fullPath, "%s/%s", path, entry->d_name);
    struct stat fileStat;
    if((stat(fullPath, &fileStat))==-1) {
      perror("stat failed!");
      continue;
    }
    if(S_ISDIR(fileStat.st_mode)) {
      printf("Directory: %s\n", fullPath);
      listDir(fullPath);
    }
    else {
      printf("File: %s\n", fullPath);
    } 
  }
  
  closedir(dir);
}

int main() {
  printf("Current Directory:\n\n");
  listDir(".");
  return 0;
}
