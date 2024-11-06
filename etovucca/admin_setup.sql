DROP TABLE IF EXISTS admin_passwords;
CREATE TABLE admin_passwords (
  id INTEGER PRIMARY KEY,
  password TEXT NOT NULL,
  password_hash TEXT NOT NULL
);
INSERT INTO admin_passwords(id,password,password_hash) VALUES (1, 'admin', '21232f297a57a5a743894a0e4a801fc3');
