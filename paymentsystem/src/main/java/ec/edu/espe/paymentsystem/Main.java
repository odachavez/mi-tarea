/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.espe.paymentsystem;

/**
 *
 * @author Odalys Chavez, CodeBreakers, @ESPE
 */
public class Main {
    public static void main(String[] args) {

        Customer customer = new Customer("Odalys");
        Payment payment = new CreditCard(customer,"TX001");

        PaymentProcessor processor = new PaymentProcessor();

        processor.processPayment(payment, 150.00);
        Customer customer2= new Customer("Hilda");
        Payment payment1;
        payment1 = new CreditCard(customer2,"TX001");

        

        processor.processPayment(payment1, 150.35);
    }
    
}
