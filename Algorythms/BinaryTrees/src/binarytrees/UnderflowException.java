/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package binarytrees;

/**
 *
 * @author Alexandros
 */

public class UnderflowException extends RuntimeException
{
    /**
     * Construct this exception object.
     * @param message the error message.
     */
    
    public UnderflowException(  )
    {
    }

    public UnderflowException( String message )
    {
        super( message );
    }

    
}

