package com.example.tau;

public class OrderService {
    private final PaymentService paymentService;
    private final InventoryService inventoryService;
    private final NotificationService notificationService;

    public OrderService(PaymentService paymentService, InventoryService inventoryService, NotificationService notificationService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public boolean placeOrder(Integer userId, Integer productId) {
        try {
            if (!inventoryService.isProductAvailable(productId)) {
                notificationService.sendNotification(userId, "Product is not available.");
                return false;
            }

            boolean paymentSuccess = paymentService.processPayment(userId, productId);
            if (!paymentSuccess) {
                notificationService.sendNotification(userId, "Payment failed.");
                return false;
            }

            notificationService.sendNotification(userId, "Order has been successfully placed");
            return true;
        } catch (Exception e) {
            notificationService.sendNotification(userId, "An error occurred while processing your order.");
            return false;
        }
    }
}
