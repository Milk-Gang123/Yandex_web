from werkzeug.security import check_password_hash

print(check_password_hash('pbkdf2:sha256:260000$erYmWaxUEAhHA8Op$6da6c56fcfb71c8d63ded2a2ed6ac555e60d179fa7153f7e301e3351ff637e0f', '12345'))