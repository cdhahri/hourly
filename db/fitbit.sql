USE `hourly`;

ALTER TABLE `user` ADD `fitbit_url` varchar(200);

CREATE TABLE `history_fitbit` (
  `twitter_id` varchar(100) NOT NULL,
  `time_id`    char(13)     NOT NULL,
  `data`       TEXT         NOT NULL,
  PRIMARY KEY (`twitter_id`, `time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

UPDATE `user` SET fitbit_url = 'http://fitbit.com/user/22CK8B' WHERE twitter_id = '10449052';
