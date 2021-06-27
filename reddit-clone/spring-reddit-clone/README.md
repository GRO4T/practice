# Reddit Clone
### Tutorial URL
https://www.youtube.com/watch?v=DKlTBBuc32c

#### Swagger Docs URL
http://localhost:8080/swagger-ui.html

### Dependencies and technologies in use
#### Core
* **Spring Web**

#### Database
* **MySQL** (setting up MySQL server https://dev.mysql.com/doc/mysql-getting-started/en/)
* **JPA**
* **MapStruct** to map requests to database
* **Flyway** database migration tool

#### Security
* **Spring Security**
* **JSON Web Token**

#### HTML
* **Thymeleaf** template engine

#### Docs
* **Swagger** https://www.baeldung.com/swagger-2-documentation-for-spring-rest-api

#### Misc
* **timeago** https://github.com/marlonlom/timeago (it needs kotlin-maven-plugin https://kotlinlang.org/docs/reference/using-maven.html)
* **Lombok** library for code generation (getters, setters, ...)
* **Java Mail Sender** https://bykowski.pl/spring-boot-20-konfigurowanie-klienta-pocztowego/

### Things to check out
* Message queues (RabbitMQ or ActiveMQ) as an alternative to async processing
* Java keystore (resources/springblog.jks)

### How to run tests from multiple modules together
https://stackoverflow.com/questions/11469122/run-unit-tests-in-intellij-idea-from-multiple-modules-together
regexp for finding the first occurence of word 'Test'
```bash
^(.*?)(Test)(.*)$
```
### CORS
I've encountered an issue where server was rejecting client OPTIONS request. The solution was to add this to SecurityConfig:
```java
httpSecurity.cors().and() // <-- new line
        .csrf().disable()
        .
        .
        .
```


