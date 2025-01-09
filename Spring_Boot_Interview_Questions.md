# Spring Boot Interview Questions

## 1. What is Spring Boot?
Spring Boot is a Java-based framework used to create stand-alone, production-ready applications. It offers additional support for auto-configuration, embedded application servers like Tomcat and Jetty.

## 2. Features of Spring Boot
- Creates stand-alone Spring applications with minimal configuration.
- Embedded Tomcat and Jetty for running the application with just code.
- Provides production-ready features such as metrics, health checks, and externalized configuration.
- No requirement for XML configuration.

## 3. What are the Spring Boot key components?
- Spring Boot Auto-Configuration
- Spring Boot CLI
- Spring Boot Starter POMs
- Spring Boot Actuators

## 4. What is the starter dependency?
Spring Boot Starter is a Maven template that contains a collection of all relevant transitive dependencies required to start a particular functionality. For example:
- `spring-boot-starter-web` for creating a web application.
- Data JPA starter.
- Test Starter.
- Security starter.
- Web starter.
- Mail starter.
- Thymeleaf starter.

## 5. How does Spring Boot work?
Spring Boot automatically configures your application based on the dependencies added to the project using annotations. The entry point of a Spring Boot application is the class containing the `@SpringBootApplication` annotation and the `main` method.

## 6. What is `@SpringBootApplication`?
The `@SpringBootApplication` annotation is a combination of:
- `@Configuration` – Indicates the class contains Spring configuration.
- `@EnableAutoConfiguration` – Automatically enables the configuration of the Spring application based on dependencies and environment.
- `@ComponentScan` – Automatically scans and initializes beans and packages when the application starts.

## 7. What is Spring Initializer?
Spring Initializer is a web-based application that helps you create an initial Spring Boot project structure, providing a Maven or Gradle file to build your code.

## 8. What is Spring Boot CLI and what are its benefits?
Spring Boot CLI is a command-line interface that allows you to create Spring-based Java applications using Groovy.

## 9. What is Spring Boot dependency management?
Spring Boot Dependency Management automatically manages the versions of dependencies without needing you to specify them, simplifying your project's configuration.

## 10. How to disable a specific auto-configuration class?
You can disable a specific auto-configuration class using the `@EnableAutoConfiguration` annotation with the `exclude` attribute:
```java
@EnableAutoConfiguration(exclude = SomeAutoConfigurationClass.class)

