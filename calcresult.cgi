#!"F:\xampp\perl\bin\perl.exe"
use strict;
use URI;
use feature 'switch';
print "Content-type: text/html\r\n\r\n";
my $message=<<"EOF";
<!DOCTYPE HTML>
<html>
<head>
<meta name="author" content="Sai Pc">
<title>Calculation Results</title>
<link href="/xampp/xampp.css" rel="stylesheet" type="text/css">
</head>
<body><h1>Calculation Results</h1>
EOF

print $message;

my $path=$ENV{REQUEST_URI};
my $meth=$ENV{REQUEST_METHOD};
my $page_url = 'http';
$page_url .= "://";
if ($ENV{SERVER_PORT} != "80") {
    $page_url .= $ENV{SERVER_NAME}.":".$ENV{SERVER_PORT}.$path;
} else {
    $page_url .= $ENV{SERVER_NAME}.$path;
}

my $url=URI->new($page_url);

my @query=split("&",$url->query);
my @params;
my @value;
for(my $i=0;$i<scalar @query;$i++){
@params[$i]=(split /=/,@query[$i])[0];
@value[$i]=(split /=/,@query[$i])[1];
}

my $a=@value[0];
my $b=@value[1];
my $op=@value[2];
#print $op;
$op =~ s/%(..)/sprintf("%c",hex $1)/eg;
#print $op;
my $op_full;
print "Inputs were ".@query[0]." and ".@query[1]."<br>";


my $result;
$result="Not available";
$op_full="No operation";
given( $op ) {
    when('+'){$result=$a+$b;$op_full="Addition";}
    when('-'){$result=$a-$b;$op_full="Subtraction";}
    when('*'){$result=$a * $b ;$op_full="Multiplication";}
    when('/'){if($b!=0) { $result=$a / $b;$op_full="Division";} }
    }

print "Operation selected was ".$op_full."<br>";
print "Result is ".$result."<br>";

print "</body></html>";