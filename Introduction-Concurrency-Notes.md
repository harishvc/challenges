#Introduction to Concurrency


## Notes

### Thread vs Process
A process is an executing instance of an application. A thread is a path of execution within a process. A process can contain many threads. 
* Threads are easy to create, consume less resources since they share the same address space as the process creating the threads
* Threads are used for small tasks, whereas processes are used for more ‘heavyweight’ tasks – basically the execution of applications - threads are light weight processes.
* Threads within the same process share the same address space, whereas different processes do not. This allows threads to read from and write to the same data structures and variables, and also facilitates communication between threads. Communication between processes – also known as IPC, or inter-process communication – is quite difficult and resource-intensive
* Processes are independent of each other.  Threads, since they share the same address space are interdependent

### Concurrency vs Parallel   
* A parallel program is one that uses a multiplicity of computational hardware (e.g. multiple processor cores) in order to perform computation more quickly. Different parts of the computation are delegated to different processors that execute at the same time (in parallel), so that results may be delivered earlier than if the computation had been performed sequentially. Parallel programming is concerned only with efficiency
* Concurrency is a program-structuring technique in which there are multiple threads of control. Here threads share and modify shared resources. Concurrent program can execute on a single processor or on multiple physical processors.
* Concurrency is hard to implement and slow since it involves Kernal transition (mutex,semaphores) and by definition block other threads.

### Mutex vs Conditional Variables  
* Mutex are designed to provide exclusive access to a shared resource - synchronized resource access. Mutexes weren't designed for use as a notification/synchronization mechanism.
* Conditional variable is used for waiting for a condition to be true (state)
* Mutex: Involves Kernal transition, two states - taken, free All waiters are woken up
* Conditional Variables: Associated with mutex, ONE waiter is woken on free, Yield and re-wait on a state  

## References
* [Introduction to Concurrency](http://cs.lmu.edu/~ray/notes/introconcurrency/)
