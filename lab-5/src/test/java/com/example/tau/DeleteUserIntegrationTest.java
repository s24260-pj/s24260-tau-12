package com.example.tau;


import com.example.tau.entity.User;
import com.example.tau.repository.UserRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class DeleteUserIntegrationTest {
    @Autowired
    MockMvc mockMvc;

    @Autowired
    UserRepository userRepository;

    private User savedUser;

    @BeforeEach
    public void setUp() {
        User user = new User();
        user.setEmail("test@test.com");
        user.setName("test tester");

        savedUser = this.userRepository.save(user);
    }

    @AfterEach
    public void tearDown() {
        this.userRepository.deleteAll();
    }

    @Test
    public void shouldDeleteUser() throws Exception {
        this.mockMvc.perform(delete("/users/" + this.savedUser.getId()))
                .andExpect(status().isNoContent());

        this.mockMvc.perform(get("/users/" + this.savedUser.getId()))
                .andExpect(status().isNotFound());
    }
}
