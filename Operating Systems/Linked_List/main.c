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
    
    add_element(&list1, &num);
    
    int num2 = 17;
    add_element(&list1, &num2);
    
    /*
    int num3 = 19;
    add_element(&list1, &num3);
    */
    
    return (EXIT_SUCCESS);
}



