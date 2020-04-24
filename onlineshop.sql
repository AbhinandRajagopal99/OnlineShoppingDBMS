-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: onlineshop
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cart` (
  `ord_no` int(11) NOT NULL AUTO_INCREMENT,
  `cus_id` int(11) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  PRIMARY KEY (`ord_no`),
  KEY `cus_id` (`cus_id`),
  CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`cus_id`) REFERENCES `Customers` (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
INSERT INTO `Cart` VALUES (1,1001,'2019-04-07'),(2,1002,'2019-04-07'),(3,1001,'2019-04-12'),(5,1001,'2019-04-13');
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `cus_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(25) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `customer_address` varchar(50) DEFAULT NULL,
  `login` int(11) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1001,'Subramanian S','9790672211','5v loyola ',1,'allons'),(1002,'Shyala M','8917929899','2a nahar apts, seaview, mumbai',0,NULL),(1003,'Mani J','8921399899','66 land marvel, indiranagar, bngalore',0,NULL);
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Feedbacks`
--

DROP TABLE IF EXISTS `Feedbacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Feedbacks` (
  `cus_id` int(11) DEFAULT NULL,
  `pdt_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  KEY `cus_id` (`cus_id`),
  KEY `pdt_id` (`pdt_id`),
  CONSTRAINT `Feedbacks_ibfk_1` FOREIGN KEY (`cus_id`) REFERENCES `Customers` (`cus_id`),
  CONSTRAINT `Feedbacks_ibfk_2` FOREIGN KEY (`pdt_id`) REFERENCES `ProductDetails` (`pdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feedbacks`
--

LOCK TABLES `Feedbacks` WRITE;
/*!40000 ALTER TABLE `Feedbacks` DISABLE KEYS */;
INSERT INTO `Feedbacks` VALUES (1001,7001,4,NULL),(1001,7002,5,NULL),(1001,7001,3,'Really Good'),(1001,7001,1,''),(1001,7001,3,'Great'),(1001,7001,1,''),(1001,7001,1,''),(1001,7001,1,'');
/*!40000 ALTER TABLE `Feedbacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderDetails`
--

DROP TABLE IF EXISTS `OrderDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderDetails` (
  `ord_no` int(11) DEFAULT NULL,
  `pdt_id` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  KEY `ord_no` (`ord_no`),
  KEY `pdt_id` (`pdt_id`),
  CONSTRAINT `OrderDetails_ibfk_1` FOREIGN KEY (`ord_no`) REFERENCES `Cart` (`ord_no`),
  CONSTRAINT `OrderDetails_ibfk_2` FOREIGN KEY (`pdt_id`) REFERENCES `ProductDetails` (`pdt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderDetails`
--

LOCK TABLES `OrderDetails` WRITE;
/*!40000 ALTER TABLE `OrderDetails` DISABLE KEYS */;
INSERT INTO `OrderDetails` VALUES (1,7001,2),(1,7002,1),(2,7004,3),(3,7004,2),(5,7007,1);
/*!40000 ALTER TABLE `OrderDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderStatus`
--

DROP TABLE IF EXISTS `OrderStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderStatus` (
  `ord_no` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `reason_for_return` varchar(25) DEFAULT NULL,
  `cancel_desc` varchar(50) DEFAULT NULL,
  `ret_or_rep` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  KEY `ord_no` (`ord_no`),
  CONSTRAINT `OrderStatus_ibfk_1` FOREIGN KEY (`ord_no`) REFERENCES `Cart` (`ord_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderStatus`
--

LOCK TABLES `OrderStatus` WRITE;
/*!40000 ALTER TABLE `OrderStatus` DISABLE KEYS */;
INSERT INTO `OrderStatus` VALUES (1,'Cancelled','ORDERED BY MISTAKE','','RETURN & REFUND',NULL),(2,'shipped','','','','2018-05-12'),(3,'Cancelled','ITEM NOT MATCHING','','REPLACE','2019-05-13');
/*!40000 ALTER TABLE `OrderStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PaymentDetails`
--

DROP TABLE IF EXISTS `PaymentDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PaymentDetails` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `ord_no` int(11) DEFAULT NULL,
  `price` float(7,2) DEFAULT NULL,
  `mode` varchar(10) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`pay_id`),
  KEY `ord_no` (`ord_no`),
  CONSTRAINT `PaymentDetails_ibfk_1` FOREIGN KEY (`ord_no`) REFERENCES `Cart` (`ord_no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PaymentDetails`
--

LOCK TABLES `PaymentDetails` WRITE;
/*!40000 ALTER TABLE `PaymentDetails` DISABLE KEYS */;
INSERT INTO `PaymentDetails` VALUES (1,1,14548.00,'card','2019-04-07'),(2,5,3495.23,'card','2019-04-13'),(3,5,3495.23,'COD','2019-04-13'),(4,5,3495.23,'card','2019-04-13'),(5,5,3495.23,'COD','2019-04-13'),(6,3,9040.00,'COD','2019-04-13');
/*!40000 ALTER TABLE `PaymentDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProductDetails`
--

DROP TABLE IF EXISTS `ProductDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProductDetails` (
  `pdt_id` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(25) DEFAULT NULL,
  `price` float(7,2) DEFAULT NULL,
  `category_name` varchar(20) DEFAULT NULL,
  `availability` int(11) DEFAULT NULL,
  `sup_id` int(11) DEFAULT NULL,
  `imgAddress` varchar(75) DEFAULT NULL,
  `imgFile` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pdt_id`),
  KEY `sup_id` (`sup_id`),
  CONSTRAINT `ProductDetails_ibfk_1` FOREIGN KEY (`sup_id`) REFERENCES `Suppliers` (`sup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7012 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProductDetails`
--

LOCK TABLES `ProductDetails` WRITE;
/*!40000 ALTER TABLE `ProductDetails` DISABLE KEYS */;
INSERT INTO `ProductDetails` VALUES (7001,'FADB Paint Sprayer',3299.25,'Maintainance',11,4001,NULL,NULL),(7002,'Kingfisher Cupboard',7949.50,'Interior Dec',9,4002,NULL,NULL),(7003,'Lenovo Ideapad',6850.00,'Consumer Ele',22,4001,NULL,NULL),(7004,'Nodiac Headphones',4520.00,'Consumer Ele ',17,4003,NULL,NULL),(7005,'BlackOut',599.00,'Gaming ',19,4002,NULL,NULL),(7007,'Guitar GREG Benette',3495.23,'Music',2,4002,NULL,NULL),(7011,'Lego Undercover',599.00,'Gaming',4,4004,NULL,NULL);
/*!40000 ALTER TABLE `ProductDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShippingDetails`
--

DROP TABLE IF EXISTS `ShippingDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ShippingDetails` (
  `ship_id` int(11) NOT NULL AUTO_INCREMENT,
  `ord_no` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tracking` varchar(15) DEFAULT NULL,
  `ship_add` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ship_id`),
  KEY `ord_no` (`ord_no`),
  CONSTRAINT `ShippingDetails_ibfk_1` FOREIGN KEY (`ord_no`) REFERENCES `Cart` (`ord_no`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShippingDetails`
--

LOCK TABLES `ShippingDetails` WRITE;
/*!40000 ALTER TABLE `ShippingDetails` DISABLE KEYS */;
INSERT INTO `ShippingDetails` VALUES (1,1,'2019-04-21','Cancelled',''),(3,3,'2019-04-21','Cancelled','Basin Bridge');
/*!40000 ALTER TABLE `ShippingDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suppliers`
--

DROP TABLE IF EXISTS `Suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Suppliers` (
  `sup_id` int(11) NOT NULL AUTO_INCREMENT,
  `sup_add` varchar(50) DEFAULT NULL,
  `supplier_name` varchar(25) DEFAULT NULL,
  `login` int(11) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4005 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suppliers`
--

LOCK TABLES `Suppliers` WRITE;
/*!40000 ALTER TABLE `Suppliers` DISABLE KEYS */;
INSERT INTO `Suppliers` VALUES (4001,'4a balakrishnan apts, mylapore, chennai','Vivek K',0,'delta'),(4002,'53 anand apts, santhome, chennai','Krishnan R',0,NULL),(4003,'5a, Loyal Road, Gwailor','Raman B',0,NULL),(4004,'55 vadanemeli','shravan',0,'allons');
/*!40000 ALTER TABLE `Suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-13  9:48:31
