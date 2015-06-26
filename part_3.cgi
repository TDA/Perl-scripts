#!"F:\xampp\perl\bin\perl.exe"

  print "Content-type: text/html\n\n";

my ($buffer, @pairs, $pair, $name, $value, %FORM);
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	$buffer = $ENV{'QUERY_STRING'};

	local $single_cgi = 'http';
	if ($ENV{HTTPS} = "on") {
		$single_cgi .= "s";
	}
	$page_url .= "://";
	if ($ENV{SERVER_PORT} != "80") {
		$single_cgi .= $ENV{SERVER_NAME}.":".$ENV{SERVER_PORT}.$ENV{REQUEST_URI};
	} else {
		$single_cgi .= $ENV{SERVER_NAME}.$ENV{REQUEST_URI};
	}	

	@pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%(..)/pack("C", hex($1))/eg;
	$FORM{$name} = $value;        
	}
	
if ($single_cgi =~ m/calculator/ or $single_cgi =~ m/operation=/)
	{
	
	$res = $FORM{method};
	$first_value = $FORM{a};
    	$second_value  = $FORM{b};

	if ($res eq '+'){
		 $result = $first_value + $second_value;
		} 
		elsif ($res eq '-')
		{
		$result = $first_value - $second_value;
		} 
		elsif ($res eq '*')
		{
		$result = $first_value * $second_value;
		}
		elsif ($res eq '/')
		{
		$result = $first_value / $second_value;
		}
		
		print "<input type='text' value='$result' size='7' disabled>";  
		
		print <<End1;
		<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset=utf-8>
	<title>Calculator</title>
	</head>		
		<form action="../part_3.cgi/calculator" name="calculator" method = "GET" >
		<br>
	<input type = "text" name = "a" >
	<input type = "text" name = "b" >
	<select name = 'method'>
	<option value = "+" selected>+</option>
	<option value = "-">-</option>
	<option value = "*">*</option>
	<option value = "/">/</option>
	</select>
	<input type = "submit" value = "submit" >
</form>
</body>
</html>
End1
		
}

else{
$name = $FORM{name};
	
	my $comment  = $FORM{comment};
	
	my $input = 'input.txt';
	open(sol, '+>>' , $input) or die " File could not be opened";
	print sol "$name $comment";
	print sol "\n";
	seek ( sol, 0, 0);
	while(my $var = <sol> )
	{
	print "$var \n\n\n";
	print "<br>";
	print "\n";
	
	}
	close (sol);
	
		print <<End2;
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset=utf-8>
	<title>GuestBook</title>
	</head>
	<body>
		<form action="../part_3.cgi/guestbook" name="guestbook" method = "GET" >
	name 
	<input type = "text" name = "name" ><br>
	comment
	<textarea rows="4" cols="50" name = "comment"></textarea>
	<input type = "submit" value = "submit" >
</form>
</body>
</html>

End2


}		
		
		
	 
	1;
		
		
	
	
	
