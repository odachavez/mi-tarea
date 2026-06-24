/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.espe.paymentsystem;

/**
 *
 * @author Odalys Chavez, CodeBreakers, @ESPE
 */
public class OnlinePayment {
    protected String transactionId;

    public OnlinePayment(String transactionId) {
        this.transactionId = transactionId;
    }

    public String getTransactionId() {
        return transactionId;
    }
    
    
}
