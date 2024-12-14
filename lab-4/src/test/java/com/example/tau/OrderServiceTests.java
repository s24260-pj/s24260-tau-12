package com.example.tau;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.*;

public class OrderServiceTests {
    private OrderService orderService;
    private PaymentService paymentService;
    private InventoryService inventoryService;
    private NotificationService notificationService;

    @BeforeEach
    void setUp() {
        paymentService = mock(PaymentService.class);
        inventoryService = mock(InventoryService.class);
        notificationService = mock(NotificationService.class);

        orderService = new OrderService(paymentService, inventoryService, notificationService);
    }

    @Test
    void shouldOrderSuccessfullyPlaced() {
        // given
        Integer productId = 1;
        Integer userId = 1;

        // when
        when(inventoryService.isProductAvailable(productId)).thenReturn(true);
        when(paymentService.processPayment(userId, productId)).thenReturn(true);

        boolean result = orderService.placeOrder(userId, productId);

        // then
        assertTrue(result);
        verify(inventoryService).isProductAvailable(productId);
        verify(paymentService).processPayment(userId, productId);
        verify(notificationService).sendNotification(userId, "Order has been successfully placed");
    }

    @Test
    void shouldOrderFailsWhenProductNotAvailable() {
        // given
        Integer productId = 1;
        Integer userId = 1;

        // when
        when(inventoryService.isProductAvailable(productId)).thenReturn(false);

        boolean result = orderService.placeOrder(userId, productId);

        // then
        assertFalse(result);
        verify(inventoryService).isProductAvailable(productId);
        verifyNoInteractions(paymentService);
        verify(notificationService).sendNotification(userId, "Product is not available.");
    }

    @Test
    void shouldOrderFailsWhenPaymentFails() {
        // given
        Integer productId = 1;
        Integer userId = 1;

        // when
        when(inventoryService.isProductAvailable(productId)).thenReturn(true);
        when(paymentService.processPayment(userId, productId)).thenReturn(false);

        boolean result = orderService.placeOrder(userId, productId);

        // then
        assertFalse(result);
        verify(inventoryService).isProductAvailable(productId);
        verify(paymentService).processPayment(userId, productId);
        verify(notificationService).sendNotification(userId, "Payment failed.");
    }

    @Test
    void shouldOrderHandlesPaymentServiceException() {
        // given
        Integer productId = 1;
        Integer userId = 1;

        // when
        when(inventoryService.isProductAvailable(productId)).thenReturn(true);
        when(paymentService.processPayment(userId, productId)).thenThrow(new RuntimeException("Payment service error"));

        boolean result = orderService.placeOrder(userId, productId);

        // then
        assertFalse(result);
        verify(inventoryService).isProductAvailable(productId);
        verify(paymentService).processPayment(userId, productId);
        verify(notificationService).sendNotification(userId, "An error occurred while processing your order.");
    }
}
