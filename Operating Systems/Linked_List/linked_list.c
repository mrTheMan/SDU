/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
#include <stdio.h>
#include "linked_list.h"
#define NULL 0


linked_list *init_linked_list()
{
    
    linked_list *newList;
    newList = malloc( sizeof( newList ) );
    
    newList->data = NULL;
    newList->next = NULL;
    newList->previous = NULL;
    
    printf("Empty linked list pointer created\n");
    
    return &newList;
}

void add_element( linked_list *list, void *element)
{
    int count = 1;
    while(list->next != 0 )
    {
        printf("print from inside loop %i", count);
        count++;
    }
     
}

