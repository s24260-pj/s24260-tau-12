package com.example.tau.repository;

import com.example.tau.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    List<User> findAll();

    Optional<User> findById(long id);

    User save(User user);

    void deleteById(long id);
}
