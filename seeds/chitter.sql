
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE,
    full_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    user_password VARCHAR(255)
);

INSERT INTO users (user_name, full_name, email, user_password) VALUES ('Duncan', 'Leonard Hofstadter', 'LeonardH@ihatesheldon.com','P3nny');
INSERT INTO users (user_name, full_name, email, user_password) VALUES ('Shelly','Sheldon Cooper', 'DrCopper@spockfanclub.com', 'DamnY0uWillWh3aton');
INSERT INTO users (user_name, full_name, email, user_password) VALUES ('Froot_loops','Howard Wolowitz', 'Wolowizard@Nasa.com', 'Br1sk3t');
INSERT INTO users (user_name, full_name, email, user_password) VALUES ('Raj', 'Rajesh Koothrappali', 'Raj@nerdsunited.com', 'Allth3singl3Ladies');
INSERT INTO users (user_name, full_name, email, user_password) VALUES ('Stewie', 'Stewart Bloom', 'StanL33Fan@thecomicshop.com', 'password');


CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id int,
    constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade,
    post_time TIMESTAMP
);

INSERT INTO posts (content, user_id, post_time) VALUES ('Sheldon your room mate agreement can suck it', 1, '2024-10-24 15:41:36.070985');
INSERT INTO posts (content, user_id, post_time) VALUES ('My intelligence, is the answer to why I deserve the noble prize', 2, '2024-10-24 15:41:36.070985');
INSERT INTO posts (content, user_id, post_time) VALUES ('Magic is NOT just for little kids', 3, '2024-10-24 15:41:36.070985');
INSERT INTO posts (content, user_id, post_time) VALUES ('Men get yourself some face cream, my face feels so soft!', 4, '2024-10-24 15:41:36.070985');
INSERT INTO posts (content, user_id, post_time) VALUES ('I am finally doing it! I have a stand at comic con, please visit me :(', 5, '2024-10-24 15:41:36.070985');
