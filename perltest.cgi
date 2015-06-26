#!"F:\xampp\perl\bin\perl.exe"
use URI;
use Data::Dumper qw(Dumper);
print "Content-type: text/html\r\n\r\n";
print '<!DOCTYPE HTML>';
print '<html>';
print '<head>';
print '<meta name="author" content="Sai Pc">';
print '<link href="/xampp/xampp.css" rel="stylesheet" type="text/css">';
print '</head>';
print "<body><h1>CGI working</h1>";

#print  "Stupid content here...";

foreach $key (sort(keys %ENV)) {
#    print "$key = $ENV{$key}<br>\n";
}

$path=$ENV{REQUEST_URI};
print "$path"."\n<br>";

$meth=$ENV{REQUEST_METHOD};
print "\n$meth"."\n<br>";


my $page_url = 'http';
$page_url .= "://";
if ($ENV{SERVER_PORT} != "80") {
    $page_url .= $ENV{SERVER_NAME}.":".$ENV{SERVER_PORT}.$path;
} else {
    $page_url .= $ENV{SERVER_NAME}.$path;
}

print $page_url."\n<br>";

$url=URI->new($page_url);

print $url."\n<br>";

print $url->query."\n<br>";

#print join(':',split("",$path));

#print join(':', split('b', 'abc')), "<br>";

@query=split("&",$url->query);
@params;
@value;
for($i=0;$i<scalar @query;$i++){
#print @query[$i];
print "<br>";
@params[$i]=(split /=/,@query[$i])[0];
@value[$i]=(split /=/,@query[$i])[1];

}

print @params;
print @value;

print "</body></html>";