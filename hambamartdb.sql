-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 25, 2024 at 01:03 PM
-- Server version: 10.5.26-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hambamartdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `AdminID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `password` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`AdminID`, `Name`, `Email`, `is_active`, `is_staff`, `is_superuser`, `last_login`, `password`) VALUES
(1, 'Tasfia Zaman', 'tasfia.zaman@g.bracu.ac.bd', 1, 1, 1, '2024-09-25 10:08:50.735233', 'pbkdf2_sha256$870000$x2j7C5hkagLJ8Smz5uL8Go$gssmHwqDiBDq/iPcvi9nGd/EA5q4NlZZALhNIquarrY='),
(2, 'Al Irfan Alve', 'al.irfan.alve@g.bracu.ac.bd', 1, 1, 1, '2024-09-25 08:27:03.443880', 'pbkdf2_sha256$870000$ouvJ8qyvQ6beypgXa5hqVV$2ThZY/vzjF9S9b96Y+aqtDkoiRrm2EBGONCWDXhK6EU='),
(3, 'Md. Rezaur Rahman Bhuiyan', 'rezaur.rahman.bhuiyan@g.bracu.ac.bd', 1, 1, 1, NULL, 'pbkdf2_sha256$870000$L1n7JC4Q3fSpdzTWswL9TU$taY2PMQn80rfmRPaLFeW2pt/htSaDOq/g9mhZ2WngoE=');

-- --------------------------------------------------------

--
-- Table structure for table `admin_groups`
--

CREATE TABLE `admin_groups` (
  `id` bigint(20) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admin_user_permissions`
--

CREATE TABLE `admin_user_permissions` (
  `id` bigint(20) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cart', 7, 'add_cart'),
(26, 'Can change cart', 7, 'change_cart'),
(27, 'Can delete cart', 7, 'delete_cart'),
(28, 'Can view cart', 7, 'view_cart'),
(29, 'Can add cart product', 8, 'add_cartproduct'),
(30, 'Can change cart product', 8, 'change_cartproduct'),
(31, 'Can delete cart product', 8, 'delete_cartproduct'),
(32, 'Can view cart product', 8, 'view_cartproduct'),
(33, 'Can add customer', 9, 'add_customer'),
(34, 'Can change customer', 9, 'change_customer'),
(35, 'Can delete customer', 9, 'delete_customer'),
(36, 'Can view customer', 9, 'view_customer'),
(37, 'Can add admin', 10, 'add_admin'),
(38, 'Can change admin', 10, 'change_admin'),
(39, 'Can delete admin', 10, 'delete_admin'),
(40, 'Can view admin', 10, 'view_admin'),
(41, 'Can add product', 11, 'add_product'),
(42, 'Can change product', 11, 'change_product'),
(43, 'Can delete product', 11, 'delete_product'),
(44, 'Can view product', 11, 'view_product'),
(45, 'Can add product tags', 12, 'add_producttags'),
(46, 'Can change product tags', 12, 'change_producttags'),
(47, 'Can delete product tags', 12, 'delete_producttags'),
(48, 'Can view product tags', 12, 'view_producttags'),
(49, 'Can add order product', 13, 'add_orderproduct'),
(50, 'Can change order product', 13, 'change_orderproduct'),
(51, 'Can delete order product', 13, 'delete_orderproduct'),
(52, 'Can view order product', 13, 'view_orderproduct'),
(53, 'Can add orders', 14, 'add_orders'),
(54, 'Can change orders', 14, 'change_orders'),
(55, 'Can delete orders', 14, 'delete_orders'),
(56, 'Can view orders', 14, 'view_orders'),
(57, 'Can add payment', 15, 'add_payment'),
(58, 'Can change payment', 15, 'change_payment'),
(59, 'Can delete payment', 15, 'delete_payment'),
(60, 'Can view payment', 15, 'view_payment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `Cart_ID` int(11) NOT NULL,
  `CustomerID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cart_product`
--

CREATE TABLE `cart_product` (
  `Product_ID` int(11) NOT NULL,
  `CustomerID` int(11) NOT NULL,
  `Cart_ID` int(11) NOT NULL,
  `Quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `CustomerID` int(11) NOT NULL,
  `FName` varchar(255) NOT NULL,
  `MName` varchar(255) DEFAULT NULL,
  `LName` varchar(255) NOT NULL,
  `Address` text DEFAULT NULL,
  `Phone` varchar(20) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `password` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`CustomerID`, `FName`, `MName`, `LName`, `Address`, `Phone`, `Email`, `is_active`, `is_staff`, `is_superuser`, `last_login`, `password`) VALUES
(1, 'Adrita', NULL, 'Zaman', NULL, '01521735832', 'adrita.03.zaman@gmail.com', 1, 0, 0, '2024-09-24 20:31:54.859579', 'pbkdf2_sha256$870000$UQf8cXD6RLJoODwIXrZsFM$Ds1AMYwiJA9LOPVzoPH+aO1+yMy4taEV8iZPAkDM6XA=');

-- --------------------------------------------------------

--
-- Table structure for table `customer_groups`
--

CREATE TABLE `customer_groups` (
  `id` bigint(20) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customer_user_permissions`
--

CREATE TABLE `customer_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'customers', 'cart'),
(8, 'customers', 'cartproduct'),
(9, 'customers', 'customer'),
(13, 'orders', 'orderproduct'),
(14, 'orders', 'orders'),
(15, 'orders', 'payment'),
(10, 'products', 'admin'),
(11, 'products', 'product'),
(12, 'products', 'producttags'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-09-20 02:59:46.540905'),
(2, 'auth', '0001_initial', '2024-09-20 02:59:46.916303'),
(3, 'admin', '0001_initial', '2024-09-20 02:59:46.993346'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-09-20 02:59:47.009305'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-09-20 02:59:47.053303'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-09-20 02:59:47.111303'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-09-20 02:59:47.148312'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-09-20 02:59:47.167307'),
(9, 'auth', '0004_alter_user_username_opts', '2024-09-20 02:59:47.180308'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-09-20 02:59:47.220305'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-09-20 02:59:47.222305'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-09-20 02:59:47.234302'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-09-20 02:59:47.253303'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-09-20 02:59:47.268313'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-09-20 02:59:47.282304'),
(16, 'auth', '0011_update_proxy_permissions', '2024-09-20 02:59:47.292302'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-09-20 02:59:47.305303'),
(18, 'customers', '0001_initial', '2024-09-20 02:59:47.310304'),
(19, 'orders', '0001_initial', '2024-09-20 02:59:47.314307'),
(20, 'products', '0001_initial', '2024-09-20 02:59:47.319302'),
(21, 'sessions', '0001_initial', '2024-09-20 02:59:47.336547'),
(22, 'customers', '0002_alter_customer_options', '2024-09-23 01:34:45.617606'),
(23, 'products', '0002_alter_admin_options', '2024-09-23 01:34:45.631471'),
(24, 'customers', '0003_customer_groups_customer_is_active_customer_is_staff_and_more', '2024-09-23 06:16:39.713363'),
(25, 'products', '0003_admin_groups_admin_is_active_admin_is_staff_and_more', '2024-09-23 06:16:39.968788'),
(26, 'customers', '0004_remove_customer_password', '2024-09-23 07:16:13.580675'),
(27, 'products', '0004_remove_admin_password', '2024-09-23 07:16:27.880734'),
(28, 'customers', '0005_alter_customer_password', '2024-09-23 07:26:28.417598'),
(29, 'products', '0005_alter_admin_password', '2024-09-23 07:26:28.434778'),
(30, 'customers', '0006_alter_customer_password', '2024-09-23 07:38:39.138235'),
(31, 'products', '0006_alter_admin_password', '2024-09-23 07:38:39.153797'),
(32, 'products', '0007_alter_admin_is_staff', '2024-09-24 10:38:38.419098');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cdwvhygpzof073xzh9w4w8wk66nbx9y1', '.eJxVi8sOwiAQRf-FtWnakcfg0n4IGQYQNW0TKCvjv4tJF7q6ybnnvISjtmfXaizuHsRFTOL0yzzxM67fIzxovW0LlX04YB3mVvdtieV6WH9pppp7pxMZsJwAGQNGg1JNPEoiL_uCijYm1AEkgBk9s9WpJ2wTnVEZMuL9AZvJNlw:1ssetf:e0vrApSRQwGuLL37WhxrabWC_OTZUSj65wmSYR34F8w', '2024-10-07 08:58:19.177663'),
('j5riwrjxj5a9pi3jnj7xcnewdokn4vt3', '.eJxVi0sOwiAQQO_C2jQzI5_iTi9CBgakmmJS2pXx7qZJF7p9n7cKvK01bD0vYRJ1UahOvyxyeua2C3lwu79mXtbhgH24yjy125H8fZV73Scu5IAEPRPkeDYZjRcHo-hINrriEa3TQNqmFE0qJAlJxlSAEDSpzxe4_jQw:1stOvr:v6uJVnbaIwFihCCUGqFq5_MAO9tCJw15AxK-ENtNaIw', '2024-10-09 10:07:39.278499'),
('pc61gq1hayz97ij709nj7fnobdk1qcvi', '.eJxVi8sOwiAQRf-FtWnakcfg0n4IGQYQNW0TKCvjv4tJF7q6ybnnvISjtmfXaizuHsRFTOL0yzzxM67fIzxovW0LlX04YB3mVvdtieV6WH9pppp7pxMZsJwAGQNGg1JNPEoiL_uCijYm1AEkgBk9s9WpJ2wTnVEZMuL9AZvJNlw:1sseoQ:XgDEz4AkudlEiqEzgDFqXYJ7hZ4l62_Ik4hpeoomseE', '2024-10-07 08:52:54.920810'),
('pddrj15saielhnr7zs06xoedmrpn7c6s', '.eJxVi80OwiAMgN-Fs1kKG1i86YuQUlqZZjMZ28n47mqyg16_n6dJtK01bU2WNBZzMs4cflkmvsv8FeVG8_Ux0bJ2O2zduUzjfNmTv69Sq59JoRcqrkfL6G0QZQwRwEMWoUFzJKfsxR1JRcFLxEGQEYuNIXsG83oD2D41TQ:1stJX5:OUfXP-QagjlOZUuhCaoxGciJ47rUe2YGiQV4TLzzOGU', '2024-10-09 04:21:43.086297'),
('peogp5nmq6l85qrr5lroix89zsa9qs5q', '.eJxVi80OwiAMgN-Fs1kKG1i86YuQUlqZZjMZ28n47mqyg16_n6dJtK01bU2WNBZzMs4cflkmvsv8FeVG8_Ux0bJ2O2zduUzjfNmTv69Sq59JoRcqrkfL6G0QZQwRwEMWoUFzJKfsxR1JRcFLxEGQEYuNIXsG83oD2D41TQ:1stNMV:tB0LF2aC6fKwSwfK24ZJ6zEc40xy9uw8p_iok_iJIK0', '2024-10-09 08:27:03.445380'),
('v8euvdd3uqpvqjdv37d94san1z9jpnww', '.eJxVi0sOwiAQQO_C2jQzI5_iTi9CBgakmmJS2pXx7qZJF7p9n7cKvK01bD0vYRJ1UahOvyxyeua2C3lwu79mXtbhgH24yjy125H8fZV73Scu5IAEPRPkeDYZjRcHo-hINrriEa3TQNqmFE0qJAlJxlSAEDSpzxe4_jQw:1stOx0:TMdaw3KLdwz9JDUfRZxJVLmHC6kMVvs8WVxtvYYA2xQ', '2024-10-09 10:08:50.739324');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int(11) NOT NULL,
  `Total_Price` decimal(10,2) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `Address` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_product`
--

CREATE TABLE `order_product` (
  `Product_ID` int(11) NOT NULL,
  `Order_ID` int(11) NOT NULL,
  `product_quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `P_ID` int(11) NOT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `Order_ID` int(11) DEFAULT NULL,
  `Amount` decimal(10,2) NOT NULL,
  `Method` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_ID` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Description` text DEFAULT NULL,
  `Stock` int(11) DEFAULT NULL,
  `Price` decimal(10,2) NOT NULL,
  `product_img` varchar(255) DEFAULT 'https://linklog.com/wp-content/uploads/2023/08/no-image.jpg',
  `AdminID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_ID`, `Title`, `Description`, `Stock`, `Price`, `product_img`, `AdminID`) VALUES
(1, '2X 3MM Thick Brown Rustic Jute Twine Hessian String Cord Rope for Hand Craft 250gm', 'The jute twine string is perfect for crafts, scrapbooking, sewing, gardening projects and especially great for vintage, rustic wedding decorations\nEnjoy the fun with craft\nMaterial: Jute\nColor: Brown\nDiameter: Approx. 3mm/ 0.12 inch\n\nTotal Length: Approx. 50m\nPackage Included:\n2 x Jute Twine\n\nOnly the above package content, other products are not included.\nNote: different displays may cause the color of the item in the picture a little different from the real thing. The measurement allowed error is +/- 1-3cm.', 5, 80.00, 'https://img.lazcdn.com/3rd/q/aHR0cHM6Ly9zdGF0aWMtMDEuZGFyYXouY29tLmJkL3AvNTY5MWFkZGU4ZjBhM2Y2ZWM1OGVmNmJhYTVkOTM4MmMuanBn_200x200q75.png_.webp', NULL),
(6, 'Sahiwal Bull 415Kg', 'Age: 2.6 Year\r\nWeight: 415Kg till Eid\r\n\r\nThis Sahiwal bull is a breed of Indian Zebu cattle found in the states of Punjab, Haryana and Rajasthan, also this breed of cow is now being reared in Bangladesh. There is a lot of demand during this cow sacrifice in our country. These bulls eat grass, weeds and other food like native cows, so this beef is very tasty like native beef.', 1, 260000.00, 'https://cdn.bdstall.com/product-image/giant_273901.jpg', NULL),
(7, 'Automatic Cow Body Cleaning Brush', 'This automatic cow body cleaning brush is important for growth health and beauty of cows. This brush also improves animal health by increasing blood circulation. It helps to keep the cow clean and fresh. It help to prevent cow skin diseases as well.\r\n\r\nFull Specification:\r\nAutomatic on / off control\r\nLow energy consumption\r\nSwings freely in all directions\r\nThe brush rotating on demand\r\nEasy to keep clean\r\nSuitable for 50-60 cows\r\nQuick and easy to install\r\nFlexible ​to place on the wall\r\nAutomatic stop it within 10 seconds after use\r\nBracket size is 1200 x 500 x 1000 mm\r\nThe brush size is 500 x 600 mm\r\nSpeed is 22 RPM\r\nCompatible voltage is 220V / 50HZ / 100W\r\nBristle material is nylon\r\nComes in a round shape\r\nWeight is 10kg\r\nMade in Singapore', 3, 65000.00, 'https://cdn.bdstall.com/product-image/giant_175203.jpg', NULL),
(8, '100 Pieces Ear Tag for Cow', 'Plastic material, sign with the word cattle cow ear tag, 1-100 number, TPU material, durable, laser type with no fade, copper head earring.\r\n\r\nFull Specification\r\nLength: Approx.5cm / 1.97 inch\r\nWidth: Approx.4cm / 1.57 inch\r\nGreen color available\r\nMaterial: Plastic', 40, 4500.00, 'https://cdn.bdstall.com/product-image/giant_114363.jpg', NULL),
(9, 'Kota Goat K0143', 'Basically, Kota goats are large size animal with long legs. Coat color of Kota goat is predominantly black with white spots on ears and muzzle. However, a few white, brown and spotted goats are also found. The body of Kota goat is covered densely with hair which is short and coarse\r\n\r\nSpecification:\r\nAge : 2 Year(s)\r\nGender : Male\r\nWeight : 35 kg', 1, 42636.61, 'https://s3.ap-south-1.amazonaws.com/pashushala.com/scaled/fe3042df3a7b5cfb38eba74fadcd991a239b0e0bdfe1604d15609354fcc64af2.jpg', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `product_tags`
--

CREATE TABLE `product_tags` (
  `Product_ID` int(11) NOT NULL,
  `Tag` varchar(255) NOT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_tags`
--

INSERT INTO `product_tags` (`Product_ID`, `Tag`, `id`) VALUES
(6, '415KG', NULL),
(6, 'Bull', NULL),
(6, 'Cattle', NULL),
(6, 'Cow', NULL),
(6, 'Cows', NULL),
(6, 'Indian Zebu Breed', NULL),
(6, 'Sahiwal', NULL),
(7, 'Brush', NULL),
(7, 'Cleaning Brush', NULL),
(7, 'Cow', NULL),
(7, 'Cows', NULL),
(7, 'Tools & Equipment', NULL),
(8, 'Cattle', NULL),
(8, 'Cow', NULL),
(8, 'Ear Tag', NULL),
(8, 'Ear Tags', NULL),
(8, 'Plastic', NULL),
(8, 'Tag', NULL),
(8, 'Tags', NULL),
(9, 'Goat', NULL),
(9, 'Goats', NULL),
(9, 'Indian', NULL),
(9, 'Kota', NULL),
(9, 'Rajasthan', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`AdminID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `admin_groups`
--
ALTER TABLE `admin_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_groups_admin_id_group_id_e89f9ce4_uniq` (`admin_id`,`group_id`),
  ADD KEY `admin_groups_group_id_d2f1d5d5_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `admin_user_permissions`
--
ALTER TABLE `admin_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_user_permissions_admin_id_permission_id_484ee295_uniq` (`admin_id`,`permission_id`),
  ADD KEY `admin_user_permissio_permission_id_a515643a_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`Cart_ID`,`CustomerID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Indexes for table `cart_product`
--
ALTER TABLE `cart_product`
  ADD PRIMARY KEY (`Product_ID`,`CustomerID`,`Cart_ID`),
  ADD KEY `CustomerID` (`CustomerID`),
  ADD KEY `Cart_ID` (`Cart_ID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`CustomerID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `customer_groups`
--
ALTER TABLE `customer_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_groups_customer_id_group_id_95d0ab85_uniq` (`customer_id`,`group_id`),
  ADD KEY `customer_groups_group_id_902232a5_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `customer_user_permissions`
--
ALTER TABLE `customer_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_user_permission_customer_id_permission_i_be5423b4_uniq` (`customer_id`,`permission_id`),
  ADD KEY `customer_user_permis_permission_id_2c3e834e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`Order_ID`);

--
-- Indexes for table `order_product`
--
ALTER TABLE `order_product`
  ADD PRIMARY KEY (`Product_ID`,`Order_ID`),
  ADD KEY `Order_ID` (`Order_ID`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`P_ID`),
  ADD KEY `CustomerID` (`CustomerID`),
  ADD KEY `Order_ID` (`Order_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`Product_ID`),
  ADD KEY `AdminID` (`AdminID`);

--
-- Indexes for table `product_tags`
--
ALTER TABLE `product_tags`
  ADD PRIMARY KEY (`Product_ID`,`Tag`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `AdminID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `admin_groups`
--
ALTER TABLE `admin_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `admin_user_permissions`
--
ALTER TABLE `admin_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `Cart_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `CustomerID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customer_groups`
--
ALTER TABLE `customer_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_user_permissions`
--
ALTER TABLE `customer_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `Order_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `P_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `Product_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_groups`
--
ALTER TABLE `admin_groups`
  ADD CONSTRAINT `admin_groups_admin_id_79611eb0_fk_admin_AdminID` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`AdminID`),
  ADD CONSTRAINT `admin_groups_group_id_d2f1d5d5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `admin_user_permissions`
--
ALTER TABLE `admin_user_permissions`
  ADD CONSTRAINT `admin_user_permissio_permission_id_a515643a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `admin_user_permissions_admin_id_cbffc929_fk_admin_AdminID` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`AdminID`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE;

--
-- Constraints for table `cart_product`
--
ALTER TABLE `cart_product`
  ADD CONSTRAINT `cart_product_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `cart_product_ibfk_2` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE,
  ADD CONSTRAINT `cart_product_ibfk_3` FOREIGN KEY (`Cart_ID`) REFERENCES `cart` (`Cart_ID`) ON DELETE CASCADE;

--
-- Constraints for table `customer_groups`
--
ALTER TABLE `customer_groups`
  ADD CONSTRAINT `customer_groups_customer_id_db50a81a_fk_customer_CustomerID` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`CustomerID`),
  ADD CONSTRAINT `customer_groups_group_id_902232a5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `customer_user_permissions`
--
ALTER TABLE `customer_user_permissions`
  ADD CONSTRAINT `customer_user_permis_customer_id_26a7437e_fk_customer_` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`CustomerID`),
  ADD CONSTRAINT `customer_user_permis_permission_id_2c3e834e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `order_product`
--
ALTER TABLE `order_product`
  ADD CONSTRAINT `order_product_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`),
  ADD CONSTRAINT `order_product_ibfk_2` FOREIGN KEY (`Order_ID`) REFERENCES `orders` (`Order_ID`) ON DELETE CASCADE;

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE SET NULL,
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`Order_ID`) REFERENCES `orders` (`Order_ID`) ON DELETE SET NULL;

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`AdminID`) REFERENCES `admin` (`AdminID`) ON DELETE SET NULL;

--
-- Constraints for table `product_tags`
--
ALTER TABLE `product_tags`
  ADD CONSTRAINT `product_tags_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
