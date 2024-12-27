package com.example.tau.advice;

import com.example.tau.exception.IncorrectDataException;
import com.example.tau.exception.NotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class UserAdvice {
    @ResponseStatus(HttpStatus.NOT_FOUND)
    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<String> handleNotFoundException(NotFoundException exception) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
                .body("Exception occurrence on request. Exception message: " + exception.getLocalizedMessage());
    }

    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ExceptionHandler(IncorrectDataException.class)
    public ResponseEntity<String> incorrectDataException(IncorrectDataException exception) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                .body("Bad request: " + exception.getLocalizedMessage());
    }
}
