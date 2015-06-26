#!"F:\xampp\perl\bin\perl.exe"
use strict;
use URI;
use Fcntl qw(:flock); 
use feature 'switch';

my $path=$ENV{REQUEST_URI};
my $meth=$ENV{REQUEST_METHOD};
my $page_url = 'http';
$page_url .= "://";
if ($ENV{SERVER_PORT} != "80") {
    $page_url .= $ENV{SERVER_NAME}.":".$ENV{SERVER_PORT}.$path;
} else {
    $page_url .= $ENV{SERVER_NAME}.$path;
}
print "Content-type: text/html";
print "\r\n\r\n";

my $url=URI->new($page_url);
#print $url->path."<br>";
my @parts=(split "/",$url->path);
my $app=@parts[scalar @parts -1];
#print $app;
my @query;
my @params;
my @value;

if(!($url->query) eq ""){
@query=split("&",$url->query);
for(my $i=0;$i<scalar @query;$i++){
@params[$i]=(split /=/,@query[$i])[0];
@value[$i]=(split /=/,@query[$i])[1];
}
}

my $op_full;
my $result;
    
my $calculator_header= <<"END_OF_MESSAGE";
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Calculator App</title>
<link rel="stylesheet" href="../styles.css">
</head>
<body>
<h1>Calculator App</h1>
END_OF_MESSAGE

my $calculator_form=<<"END_OF_MESSAGE";
<form action='../calculator.cgi/calculator' method='get' name="calculator" id="calculator">
<label for="a">Operand 1</label>
<input type="text" name="a" id="a" required pattern="\\d+([\.]\\d+)?" placeholder="Enter 1st number">
<label for="b">Operand 2</label>
<input type="text" name="b" id="b" required pattern="\\d+([\.]\\d+)?" placeholder="Enter 2nd number">
<label for="method">Operator</label>
<select name="method" id="method">
<option value="+" selected>+</option>
<option value="-">-</option>
<option value="*">*</option>
<option value="/">/</option>
</select>
<input type='submit' value='calculate'>
</form>
END_OF_MESSAGE

my $calculator_footer=<<"END_OF_MESSAGE";

</body>
</html>

END_OF_MESSAGE




my $guestbook_header=<<"END_OF_MESSAGE";
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Guestbook App</title>
<link rel="stylesheet" href="../guest.css">
</head>
<body>
<h1>Guestbook App</h1>
END_OF_MESSAGE


my $gbook='<div id="gbook">';



my $guestbook_footer=<<"END_OF_MESSAGE";
<form action='../calculator.cgi/guestbook' method='get' name="guestbook" id="guestbook">
<label for="name">Name(maxlength 12 characters):</label>
<input type="text" name="name" id="name" placeholder="Your name here" required maxlength="12">
<label for="comment">Comments:</label>
<textarea name="comment" id="comment" placeholder="Type your comment here, max length is of an sms: 160 characters" rows="8" cols="30" maxlength="160" required></textarea>
<input type='submit' value='Add entry'>
</form>
</body>
</html>
END_OF_MESSAGE

print $calculator_header;

    if(($url->query eq "")){
    print $calculator_form;
    }
    else{
    my $a=@value[0];
    my $b=@value[1];
    my $op=@value[2];
    $op =~ s/%(..)/sprintf("%c",hex $1)/eg;
    
    print "Inputs were ".@query[0]." and ".@query[1]."<br>";

    $result="Not available";
    $op_full="Invalid operation";
    given( $op ) {
    when('+'){$result=$a+$b;$op_full="Addition";}
    when('-'){$result=$a-$b;$op_full="Subtraction";}
    when('*'){$result=$a * $b ;$op_full="Multiplication";}
    when('/'){if($b!=0) { $result=$a / $b;$op_full="Division";} }
    }

    print "Operation selected was ".$op_full."<br>";
    print "Result is ".$result."<br>";

    }

print $calculator_footer;
print $guestbook_header;

$gbook.='</div>';
print $gbook;
print $guestbook_footer;

