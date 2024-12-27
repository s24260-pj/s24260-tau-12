package com.example.tau.service;

import com.example.tau.entity.User;
import com.example.tau.exception.IncorrectDataException;
import com.example.tau.exception.NotFoundException;
import com.example.tau.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAll() {
        return this.userRepository.findAll();
    }

    public Optional<User> getById(Long id) {
        Optional<User> user = this.userRepository.findById(id);

        if (user.isEmpty()) {
            throw new NotFoundException("User not found");
        }

        return user;
    }

    public User create(User user) {
        if (user.getEmail() == null || user.getName() == null) {
            throw new IncorrectDataException("Incorrect data provided!");
        }

        return this.userRepository.save(user);
    }

    public User update(Long id, User user) {
        Optional<User> searchUser = this.userRepository.findById(id);

        if (searchUser.isEmpty()) {
            throw new NotFoundException("User not found");
        }

        if (user.getEmail() == null || user.getName() == null) {
            throw new IncorrectDataException("Incorrect data!");
        }

        if (user.getId() == null) {
            user.setId(id);
        }

        return this.userRepository.save(user);
    }

    public void delete(Long id) {
        this.userRepository.deleteById(id);
    }
}
