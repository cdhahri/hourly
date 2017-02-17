DROP DATABASE IF EXISTS hourly;

CREATE DATABASE `hourly` DEFAULT CHARACTER SET utf8;
USE `hourly`;

-- TWITTER
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

-- RUNKEEPER
ALTER TABLE `user` ADD `runkeeper_url` varchar(200);

CREATE TABLE `history_runkeeper` (
  `twitter_id` varchar(100) NOT NULL,
  `time_id`    char(13)     NOT NULL,
  `data`       TEXT         NOT NULL,
  PRIMARY KEY (`twitter_id`, `time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- FITBIT
ALTER TABLE `user` ADD `fitbit_url` varchar(200);

CREATE TABLE `history_fitbit` (
  `twitter_id` varchar(100) NOT NULL,
  `time_id`    char(13)     NOT NULL,
  `data`       TEXT         NOT NULL,
  PRIMARY KEY (`twitter_id`, `time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

UPDATE `user` SET fitbit_url = 'http://fitbit.com/user/22CK8B' WHERE twitter_id = '10449052';

-- FOURSQUARE
ALTER TABLE `user` ADD `foursquare_id` varchar(100);
ALTER TABLE `user` ADD `foursquare_last` char(13);

CREATE TABLE `history_foursquare` (
  `twitter_id` varchar(100) NOT NULL,
  `time_id`    char(13)     NOT NULL,
  `data`       TEXT         NOT NULL,
  PRIMARY KEY (`twitter_id`, `time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tip` (
  `tip_id` varchar(100) NOT NULL,
  `tip`    TEXT         NOT NULL,
  PRIMARY KEY (`tip_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

UPDATE `user` SET foursquare_id = '151172' WHERE twitter_id = '10449052';

-- TWEET WITH SENTIMENT
CREATE TABLE `tweet_sentiment` (
  `tweet_id` varchar(100) NOT NULL,
  `tweet`    TEXT         NOT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
