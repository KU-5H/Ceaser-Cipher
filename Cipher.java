/****************************************************************
Name: Kush Patel
Due Date: 2021/09/2021

Description: Aims to create a encryption message using the Ceaser 
Cipher method. Uses the ACSII table to convert alpha values into 
values
****************************************************************/

public class Cipher {
    
    //Instance Variables
    private String message;
    private int num;
    
    //Variables used in the class
    private char tempChar;
    
    //Public object that gets values
    public Cipher(String userMessage, int userNum) {
        
        //Change values to user entered ones 
        this.message = userMessage;
        this.num = userNum;
        
        //Send values to the encode method
        encode();
    }
    
    //Method that encrypts the message
    public void encode() 
    {
        //Make new message
        message = message.toUpperCase();
        String newMessage = "";
        
        //Change value of num if the shift value is greater than 25
        num = num % 26;
        
        //For loop to encode the message
        for(int i = 0; i < message.length(); i++) 
        {
            //Variable used in for loop
            boolean noChange = true;
            
            //If the character is not a letter it is ignored
            if((int)message.charAt(i) < 65 || (int)message.charAt(i) > 90) {
                noChange = false;
            }
            
            //Gets the character value of the string
            if(noChange) {
                tempChar = message.charAt(i);
                
                //Shift the value
                tempChar += num;
            
                //loops back to the beginning of the alphabet
                if((int)tempChar > 90) {
                    tempChar -= 26;
                } else if ((int)tempChar < 65) {
                    tempChar += 26;
                }
                
                //Add letter to the text
                newMessage += (char)tempChar;
            }
        }
        
        //Calls helper method to format the encrypted message
        newMessage = helper(newMessage);
        
        //Output message
        System.out.println("Here is the shifted message: ");
        System.out.println(newMessage);
    }
    
    //Method that is used to help with the formatting of the encoded message
    public String helper(String properMessage) {
        
        //New variable to make the message
        String finalMessage = "";
        String endMessage = "";
        
        //For loop to change spacing
        for(int i = 0; i < properMessage.length(); i++) {
            
            //Add the message to the variable
            finalMessage += properMessage.charAt(i);
            endMessage += properMessage.charAt(i);
            
            //Adds space if there are 5 characters
            if(finalMessage.length() % 5 == 0) {
                endMessage += " ";
            }
            
            //New line after 50 characters
            if(finalMessage.length() % 50 == 0) {
                endMessage += "\n";
            }
        }
        
        //Return message
        return endMessage;
    }
    
    //Getter for shift value
    public int getShift() {
        return this.num;
    }
    
    //Getter for message 
    public String getMessage() {
        return this.message;
    }
    
    //Setter for shift value
    public void setShift(int shift) {
        this.num = shift;
    }
    
    //Setter for message
    public void setMessage(String userMessage) {
        this.message = userMessage;
    }
}