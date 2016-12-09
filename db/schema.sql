DROP DATABASE IF EXISTS hourly;

CREATE DATABASE `hourly` DEFAULT CHARACTER SET utf8;
USE `hourly`;

CREATE TABLE `user` (
  `twitter_id` varchar(100) NOT NULL             ,
  `since_id`   varchar(100) NULL     DEFAULT NULL,
  PRIMARY KEY (`twitter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `history_twitter` (
  `twitter_id` varchar(100) NOT NULL,
  `time_id`    char(13)     NOT NULL,
  `data`       TEXT         NOT NULL,
  PRIMARY KEY (`twitter_id`, `time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tweet` (
  `tweet_id` varchar(100) NOT NULL,
  `tweet`    TEXT         NOT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (twitter_id) VALUES ('10449052');
