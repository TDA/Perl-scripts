#!"F:\xampp\perl\bin\perl.exe"

use IO::Compress::Gzip qw(gzip);
use CGI qw('
$message= <<"END_OF_MESSAGE";
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Untitled Document</title>
</head>

<body>
<h1>Calculator App</h1>
<form action='perltest.cgi' method='get' name="calculator">
<label for="a">Operand 1</label>
<input type="text" name="a">

<label for="b">Operand 2</label>
<input type="text" name="b">

<label for="method">Operator</label>
<select name="method">
<option value="add">+</option>
<option value="sub">-</option>
<option value="mul">*</option>
<option value="div">/</option>
</select>

<input type='submit' value='calculate'>
</form>

</body>
</html>


END_OF_MESSAGE

print "Content-type: text/html";
print "\n\n";
print $message;


