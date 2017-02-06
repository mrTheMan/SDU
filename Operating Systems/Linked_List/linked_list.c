/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

#define NULL_POINTER ( (void *) 0)

linked_list *head = NULL_POINTER;


linked_list *init_linked_list()
{
    
    linked_list *newList;
    newList = (linked_list*)malloc( sizeof( linked_list ) );
    
    if(newList == 0)
    {
        printf("%d\n", *newList);
    }
    
    newList->data = malloc( sizeof( newList->data ) );
    newList->next = malloc( sizeof( newList->next ) );
    newList->next = NULL_POINTER;
    newList->previous = malloc( sizeof( newList->previous ) );
    newList->previous = NULL_POINTER;
    
    printf("Empty linked list pointer created\n");
    
    return &newList;
}

void add_element( linked_list *list, void *element)
{
    if(list->data != 0)
    {
        int count = 1;
        linked_list *temp;
        temp = (linked_list*)malloc( sizeof( linked_list ) );
        temp = &list;
        
        while(list->next != 0 )
        {
            printf("print from inside loop: %i\n", count);
            if(&temp->next != 0)
            {
                printf("list->next: %i \n", &temp->next->data);
            }
            temp = temp->next;
            count++;
        }
        
        
        linked_list *newList;
        newList = (linked_list*)malloc( sizeof( linked_list ) );

        newList->data = malloc( sizeof( newList->data ) );
        newList->data = element;
        newList->next = malloc( sizeof( newList->next ) );
        newList->next = NULL_POINTER;
        newList->previous = malloc( sizeof( newList->previous ) );
        newList->previous = &temp;
        
        temp->next = &newList;
        
        
        
        
    } else {
        
        list->data = element;
    
    }
    
     
}

