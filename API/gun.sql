-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2022 at 05:09 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Table structure for table `gun`
--

CREATE TABLE `gun` (
  `nogun` int(5) NOT NULL,
  `uname` varchar(20) CHARACTER SET utf8 NOT NULL,
  `pickup` int(2) NOT NULL,
  `broken` int(2) NOT NULL,
  `lost` int(2) NOT NULL,
  `remaining` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gun`
--

INSERT INTO `gun` (`nogun`, `uname`, `pickup`, `broken`, `lost`, `remaining`) VALUES
(1, 'A', 0, 1, 0, 0),
(2, 'B', 1, 0, 0, 0),
(3, 'C', 0, 1, 0, 0),
(4, 'D', 0, 0, 1, 0),
(5, 'E', 0, 0, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gun`
--
ALTER TABLE `gun`
  ADD PRIMARY KEY (`nogun`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
