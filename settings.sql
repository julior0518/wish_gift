-- settings.sql
CREATE DATABASE wish_gift;
CREATE USER wish_gift_user WITH PASSWORD 'wish_gift';
GRANT ALL PRIVILEGES ON DATABASE wish_gift TO wish_gift_user;