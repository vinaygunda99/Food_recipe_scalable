-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2025 at 08:35 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recipe_generator`
--

-- --------------------------------------------------------

--
-- Table structure for table `recipe`
--

CREATE TABLE `recipe` (
  `recipe_id` int(11) NOT NULL,
  `recipe_name` varchar(500) NOT NULL,
  `recipe_content` varchar(500) NOT NULL,
  `recipe_ingredients` varchar(500) NOT NULL,
  `recipe_image` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recipe`
--

INSERT INTO `recipe` (`recipe_id`, `recipe_name`, `recipe_content`, `recipe_ingredients`, `recipe_image`) VALUES
(1, 'Pasta Carbonara', 'Boil pasta until al dente., Fry pancetta until crispy., Mix eggs with cheese and black pepper., Combine pasta with pancetta and egg mixture., Serve immediately with extra cheese.', '350g spaghetti, 150g pancetta or guanciale, diced, 3 large eggs, 75g Pecorino Romano cheese, grated, Freshly ground black pepper', 'static\\css\\images\\abc.jpg'),
(2, 'Fluffy Pancakes', 'Mix dry ingredients together., Whisk in milk, egg, and butter until smooth., Heat a pan and pour batter to form pancakes., Cook until bubbles appear, then flip., Serve warm with syrup.', '1 cup all-purpose flour, 2 tbsp sugar, 1 tsp baking powder, 1/2 tsp salt, 3/4 cup milk, 1 egg, 2 tbsp melted butter', 'static\\css\\images\\pan.jpg'),
(5, 'Caesar Salad', 'Chop the lettuce and place in a bowl, Add croutons and Parmesan cheese, Drizzle with Caesar dressing and toss, Serve immediately.', '1 head romaine lettuce, chopped, 1/2 cup croutons, 1/4 cup grated Parmesan cheese, 1/2 cup Caesar dressing', 'static\\css\\images\\salad.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user_master`
--

CREATE TABLE `user_master` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(500) NOT NULL,
  `user_email` varchar(500) NOT NULL,
  `user_password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_master`
--

INSERT INTO `user_master` (`user_id`, `user_name`, `user_email`, `user_password`) VALUES
(1, 'prince', 'projectmail2223@gmail.com', '123'),
(2, 'prince', 'projectmail2223@gmail.com', '123'),
(3, 'user1', 'test@gmail.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `recipe`
--
ALTER TABLE `recipe`
  ADD PRIMARY KEY (`recipe_id`);

--
-- Indexes for table `user_master`
--
ALTER TABLE `user_master`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `recipe`
--
ALTER TABLE `recipe`
  MODIFY `recipe_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_master`
--
ALTER TABLE `user_master`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
