-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.6.21-log - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             8.0.0.4396
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for twitterdata
DROP DATABASE IF EXISTS `twitterdata`;
CREATE DATABASE IF NOT EXISTS `twitterdata` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `twitterdata`;


-- Dumping structure for table twitterdata.classifiedtweets
DROP TABLE IF EXISTS `classifiedtweets`;
CREATE TABLE IF NOT EXISTS `classifiedtweets` (
  `tweet_id` bigint(20) NOT NULL,
  `trafficInfo` tinyint(4) NOT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='whether or not tweets having traffic info\r\ntrafficInfo coloumn will be used as flag : 0 - no traffic info, 1- traffic info';

-- Dumping data for table twitterdata.classifiedtweets: ~0 rows (approximately)
DELETE FROM `classifiedtweets`;
/*!40000 ALTER TABLE `classifiedtweets` DISABLE KEYS */;
/*!40000 ALTER TABLE `classifiedtweets` ENABLE KEYS */;


-- Dumping structure for table twitterdata.processedtweets
DROP TABLE IF EXISTS `processedtweets`;
CREATE TABLE IF NOT EXISTS `processedtweets` (
  `tweet_id` bigint(20) NOT NULL,
  `tweet_text` mediumtext,
  `longitude` float DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `location_name` char(50) DEFAULT NULL,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='table for processed tweets having information like tweet_text, tweetId ,location of tweets, geo location';

-- Dumping data for table twitterdata.processedtweets: ~0 rows (approximately)
DELETE FROM `processedtweets`;
/*!40000 ALTER TABLE `processedtweets` DISABLE KEYS */;
/*!40000 ALTER TABLE `processedtweets` ENABLE KEYS */;


-- Dumping structure for table twitterdata.tweets
DROP TABLE IF EXISTS `tweets`;
CREATE TABLE IF NOT EXISTS `tweets` (
  `tweet_id` bigint(20) NOT NULL,
  `tweet_text` mediumtext,
  `user_id` varchar(50) DEFAULT NULL,
  `tweet_date` timestamp NULL DEFAULT NULL,
  `language` char(50) DEFAULT NULL,
  `screen_name` varchar(50) DEFAULT NULL,
  `followers_count` mediumint(8) unsigned DEFAULT NULL,
  `friends_count` mediumint(8) unsigned DEFAULT NULL,
  `time_zone` tinytext,
  PRIMARY KEY (`tweet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tweet table contains user tweets information like tweet_id, user_id, tweet_text, tweet_date, language, screen_name, followers_count, friends_count, time_zone';

-- Dumping data for table twitterdata.tweets: ~0 rows (approximately)
DELETE FROM `tweets`;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

# Uncomment below only when facing problem in storing emoticonsin the database
#More info
#http://andy-carter.com/blog/saving-emoticons-unicode-from-twitter-to-a-mysql-database

#SET NAMES utf8mb4;
#ALTER DATABASE twitterdata CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

#ALTER TABLE tweets CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

#ALTER TABLE tweets CHANGE tweet_text tweet_text  VARCHAR(140) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;

#REPAIR TABLE tweets;
#OPTIMIZE TABLE tweets;
