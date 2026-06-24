/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.espe.paymentsystem;

/**
 *
 * @author Odalys Chavez, CodeBreakers, @ESPE
 */
public class CreditCard extends OnlinePayment implements Payment {

    private Customer customer;

    public CreditCard(Customer customer, String transactionId) {
        super(transactionId);
        this.customer = customer;
    }

    @Override
    public void pay(double amount) {
        System.out.println(customer.getName()
                + " paid $" + amount
                + " using Credit Card.");
    }
    
}
