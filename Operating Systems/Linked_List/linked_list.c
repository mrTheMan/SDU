/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"


linked_list *init_linked_list()
{
    
    linked_list *newList;
    newList = (linked_list*)malloc( sizeof( linked_list ) );
    
    newList->data = 0;
    newList->next = 0;
    newList->previous = 0;
    
    
    return newList;
}

void add_element( linked_list *list, int element)
{
    
    if(list->data != 0)
    {
        while(list->next != 0)
        {
            list = list->next;
        }
        
        linked_list *temp = malloc( sizeof( linked_list ) );
        temp->data = element;
        temp->next = 0;
        temp->previous = list;
        list->next = temp;
        
    } else{
        list->data = element;
        list->next = 0;
    }
}

void print_all(linked_list *list)
{
    while(list != 0)
    {
        printf("Value: %i \n", (int)list->data);
        list = list->next;
    }
}

int linked_list_size(linked_list *list)
{
    int count = 0;
    while(list != 0)
    {
        list = list->next;
        count++;
    }
    
    return count;
}

void *remove_first(linked_list *list)
{
    int value = list->data;
    
    *list = *list->next;
    
    return value;
}

int remove_element(linked_list *list, int element)
{
    int count = 0;
    while(list != 0)
    {
        int num = (int)list->data;
        if(num == element)
        {
            // if it is not the first element
            if(count > 0)
            {
                if(list->previous->next != 0 && list->next != 0)
                {
                    *list->previous->next = *list->next;
                } else {
                    list->previous->next = 0;
                }
                return num; 
            } else{
                // count == 0, therefore remove first element
                return (int)remove_first(list);
            }
        } 
        
        count++;
        list = list->next;
    }
    
    return 0;
}