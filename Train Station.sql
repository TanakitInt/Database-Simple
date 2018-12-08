CREATE DATABASE TRAIN_LINE;

CREATE TABLE STATIONS
(
    station_id      int(4)          NOT NULL,
    station_name    varchar(32)     NOT NULL default '',
    station_locale  varchar(32)     NOT NULL default '',
    PRIMARY KEY (station_id)
);

CREATE TABLE LOCALE
(
    Zone            varchar(32)     NOT NULL default ''
);
