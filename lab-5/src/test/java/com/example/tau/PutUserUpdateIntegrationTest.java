package com.example.tau;

import com.example.tau.entity.User;
import com.example.tau.repository.UserRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class PutUserUpdateIntegrationTest {
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
    public void shouldUpdateUser() throws Exception {
        String userJson = """
            {
                "name": "jacek",
                "email": "jacek@jacek.com"
            }
            """;

        this.mockMvc.perform(put("/users/" + savedUser.getId())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(userJson))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("jacek"))
                .andExpect(jsonPath("$.email").value("jacek@jacek.com"));
    }

    @Test
    public void shouldThrowNotFoundException() throws Exception {
        String userJson = """
            {
                "name": "jacek",
                "email": "jacek@jacek.com"
            }
            """;

        this.mockMvc.perform(put("/users/2")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(userJson))
                .andExpect(status().isNotFound());
    }
}
