USE `hourly`;

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
