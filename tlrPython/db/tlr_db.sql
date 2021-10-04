DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS milestones;
DROP TABLE IF EXISTS smashs;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS minihabits;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE goals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  goal_date DATE NOT NULL,
  users_id INT REFERENCES users(id)
);

CREATE TABLE milestones (
  id SERIAL PRIMARY KEY,
  mile_desc VARCHAR(255),
  mile_date DATE NOT NULL,
  goal_id INT REFERENCES goals(id)
);

CREATE TABLE smashs (
  id SERIAL PRIMARY KEY,
  problem VARCHAR,
  solution VARCHAR,
  goal_id INT REFERENCES goals(id)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  task_name VARCHAR(255),
  task_desc VARCHAR(255),
  task_date VARCHAR(255),
  goal_id INT REFERENCES goals(id)
);

CREATE TABLE minihabits (
  id SERIAL PRIMARY KEY,
  mini_desc VARCHAR(255),
  mini_score INT,
  users_id INT REFERENCES users(id)
);
