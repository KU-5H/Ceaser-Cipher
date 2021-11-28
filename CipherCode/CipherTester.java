package CipherCode;

/****************************************************************
Name: Kush Patel
Due Date: 2021/09/2021

Description: Aims to create a encryption message using the Ceaser 
Cipher method. Uses the ACSII table to convert alpha values into 
values
****************************************************************/

//Create a scanner
import java.util.Scanner;

public class MyProgram
{
    public static void main(String[] args)
    {
        //Input Scanner
        Scanner input = new Scanner(System.in);
        
        //Title
        System.out.println("---------------------------------");
        System.out.println("    Ceaser Cipher - Kush Patel   ");
        System.out.println("---------------------------------");
        System.out.println("");
        
        //Ask user for message (converts to uppercase)
        System.out.println("Enter a message");
        String message = input.nextLine();
        
        //Ask user for shift value
        System.out.println("\nEnter the shift value");
        int shift = input.nextInt();
        System.out.println("");
        
        //Call the method
        Cipher userShift = new Cipher(message, shift);
        
        /*Set code if needed
        userShift.setShift(1);
        userShift.setMessage("\ntest");
        System.out.println(userShift.encode());
        */
    }
}