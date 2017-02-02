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

struct ListItem
{
  int num;

  struct ListItem *next;
  
};

/*
 * Methods
 */

int rand_range(int min_n, int max_n)
{
    return rand() % (max_n - min_n + 1) + min_n;
}

void Add(struct ListItem **root, int num)
{
       
    struct ListItem item;
    item.num = num;
    item.next = *root;
    
    *root = &item;
}

struct ListItem Find_Last_Element(struct ListItem *root) {
    struct ListItem *current = &root;

    int count = 0;
    while (current != NULL) {
        printf("%d -> %d \n", count, current->num);
        current = current->next;
        count++;
    }
    
    return *current;
}
 
void print_list(struct ListItem *root) {
    struct ListItem *current = &root;
    int count = 0;
    while (current != NULL) {
        printf("%d -> %d\n", count , current->num);
        current = current->next;
        count++;
    }
}

int main(int argc, char** argv) {
    
    struct ListItem root;
    root.num = rand_range(0,100);
    root.next = NULL;
    
    Add(&root, rand_range(0,100));
    
    printf("Root num is %d \n", root.num);
    
    Add(&root, rand_range(0,100));
    
    printf("Root num is %d\n", root.num);
    
    Add(&root, rand_range(0,100));
    
    printf("Root num is %d\n", root.num);
    
    return (EXIT_SUCCESS);
}

