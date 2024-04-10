-- mysqldump: [Warning] Using a password on the command line interface can be insecure.
-- MySQL dump 10.13  Distrib 8.0.19, for Linux (x86_64)
--
-- Host: localhost    Database: BHARATINDEX
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `i_detail`
--

DROP TABLE IF EXISTS `i_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `i_detail` (
  `i_id` varchar(20) DEFAULT NULL,
  `i_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `i_detail`
--

LOCK TABLES `i_detail` WRITE;
/*!40000 ALTER TABLE `i_detail` DISABLE KEYS */;
INSERT INTO `i_detail` VALUES ('BH01','BHARATINDEX');
/*!40000 ALTER TABLE `i_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `i_price`
--

DROP TABLE IF EXISTS `i_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `i_price` (
  `i_id` varchar(20) DEFAULT NULL,
  `i_ttime` timestamp NULL DEFAULT NULL,
  `i_price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `i_price`
--

LOCK TABLES `i_price` WRITE;
/*!40000 ALTER TABLE `i_price` DISABLE KEYS */;
/*!40000 ALTER TABLE `i_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s_detail`
--

DROP TABLE IF EXISTS `s_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s_detail` (
  `s_id` varchar(20) DEFAULT NULL,
  `s_name` varchar(20) DEFAULT NULL,
  `s_min` int DEFAULT NULL,
  `s_max` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s_detail`
--

LOCK TABLES `s_detail` WRITE;
/*!40000 ALTER TABLE `s_detail` DISABLE KEYS */;
INSERT INTO `s_detail` VALUES ('BT001','BATA',20,30),('TT001','TATA',40,55);
/*!40000 ALTER TABLE `s_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `s_price`
--

DROP TABLE IF EXISTS `s_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `s_price` (
  `s_id` varchar(20) DEFAULT NULL,
  `s_ttime` timestamp NULL DEFAULT NULL,
  `s_price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `s_price`
--

LOCK TABLES `s_price` WRITE;
/*!40000 ALTER TABLE `s_price` DISABLE KEYS */;
/*!40000 ALTER TABLE `s_price` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-06 18:20:51
