#include "stdio.h"
#include "stdint.h"

int main() {
    void* stack[1];
#if defined(__i386__)
    printf("%p ", stack[5]);
    void* printf_address = **(void***)((char*)printf + 2);
#else
    printf("%p ", stack[3]);
    void* printf_address = *(void**)((char*)printf + *(int32_t*)((char*)printf + 2) + 6);
#endif
    printf("%p\n", printf_address);
    return 0;
}

