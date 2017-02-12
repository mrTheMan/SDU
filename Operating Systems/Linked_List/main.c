/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.c
 * Author: Alexandros
 *
 * Created on February 2, 2017, 10:35 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"


/*
 * Methods
 */

int rand_range(int min_n, int max_n)
{
    return rand() % (max_n - min_n + 1) + min_n;
}

int main(int argc, char** argv) {
    
    linked_list *list1;
    list1 = init_linked_list();
    
    int num = 14;
    
    add_element(list1, num);
     
    int num2 = 17;
    add_element(list1, num2);
    
    int num3 = 19;
    add_element(list1, num3);
    
    int num4 = 21;
    add_element(list1, num4);
    
    
    print_all(list1);
    
    printf("Size: %i \n", linked_list_size(list1));
    
    printf("Removed: %i \n", (int) remove_first(list1) );
    
    printf("Size: %i \n", linked_list_size(list1));
    
    int removed = remove_element(list1, 15);
    if(removed == 0)
    {
        printf("Item not found \n");
    } else {
        printf("Removed: %i \n", removed);
    }
    
    print_all(list1);
    
    printf("Size: %i \n", linked_list_size(list1));
    
    return (EXIT_SUCCESS);
}



