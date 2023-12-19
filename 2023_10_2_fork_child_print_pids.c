#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
    // error detection, not 2 arguments
    if (argc != 2)
    {
        printf("Incorrect number of arguments...\n");
        exit(-1);
    }
  
    // take in integer, define pid var
    int n = atoi(argv[1]);
    pid_t pid;
  
    
    // fork n times
    for (int i = 0; i < n; i++)
    {
        int c_fd[2];    // create pipe
        pipe(c_fd);
        pid = fork();   // fork, both processes get a copy of EVERYTHING (even pipe)
       
        // parent process
        // pid = child_pid here if in parent process
        if (pid != 0)
        {
            // close read end, should be first thing you do
            close(c_fd[0]);
          
            // 3 args: fd, buffer, size of buffer
            // write parent pid to child
            pid_t parent_pid = getpid();
            write(c_fd[1], &parent_pid, sizeof(parent_pid));
          
            // wait for child to terminate
            int status;
            waitpid(pid, &status, 0);

            // close write pipe end, and break
            close(c_fd[1]);
            break;
        }
      
        // child process: reading
        else
        {
            close(c_fd[1]);      // close the writing end of pipe of the child process
            pid_t parent_pid;    // create parent_pid variable to hold the parent process id
            
            char final_result[1000] = "";
            
            // while loop to read data from parent, add to big char array
            while(read(c_fd[0], &parent_pid, sizeof(parent_pid))){
                char temp[64];
                sprintf(temp, "%d ", parent_pid);
                strcat(final_result, temp);
            }

            close(c_fd[0]);
          
            // if final process
            if(i == (n-1)) {
            	int f_fd = open("out.txt", O_WRONLY, 100 );   // open out.txt
                
                // replace stdout with our out.txt FD
                dup2(f_fd, STDOUT_FILENO);                    // STDOUT_FILENO is from <unistd.h>
            	printf("%s", final_result);
                close(f_fd);
               
                dup2(STDOUT_FILENO, f_fd);                    // reset FDs
            }
            break;
        }
    }
      
       
    return 0;
}