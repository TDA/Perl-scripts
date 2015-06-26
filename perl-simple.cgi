#!"F:\xampp\perl\bin\perl.exe"

use IO::Compress::Gzip qw(gzip);

$message= <<"END_OF_MESSAGE";
<!DOCTYPE HTML>
<HTML>
<HEAD>
<meta charset="utf-8">
<TITLE>
Hello World
<\/TITLE>
<\/HEAD>
<BODY>
<H1>Greetings, Terrans!<\/H1>
<p>message
mess
<\/p>
<\/BODY>
<\/HTML>
END_OF_MESSAGE

my $msg= "hi i am sai";

my $gzipped_data;
my $gzipped_data2;

my $gzip = gzip \$message => \$gzipped_data;
my $gzip2 =gzip \$msg => \$gzipped_data2;

print "Content-type: text/html\r\n";
if(index($ENV{HTTP_ACCEPT_ENCODING},'gzip')!=-1){
print "Content-encoding: gzip\r\n";
#print "Transfer-Encoding: chunked";
#print "Content-length: ".length $gzipped_data;


print "\r\n\r\n";
#print hex length $gzipped_data2."\r\n";
print $gzipped_data2."\r\n";
#print "0\r\n";
#print "\r\n";


}
else{
print "Transfer-Encoding: chunked";
print "\r\n\r\n";

print hex length $gzipped_data2."\r\n";
print $gzipped_data2."\r\n";

print "10\r\n";
print "0123456789ABCDEF\r\n";
print "10\r\n";
print "0123456789ABCDEF\r\n";
print "0\r\n";
print "\r\n";

}

#<form action='perltest' method='get'>
#<input type='submit' value='click'>
#<\/form>
