#use strict;
#use warnings;

use HTTP::Response;
use IO::Compress::Gzip qw(gzip);

my $data = '';

#print STDERR $gzipped_data;

$data.='<!DOCTYPE HTML>';
$data.='<html>';
$data.='<head>';
$data.='<meta name="author" content="Sai Pc">';
$data.='<link href="/xampp/xampp.css" rel="stylesheet" type="text/css">';
$data.='</head>';
$data.='<body><p><h1>CGI working</h1>';

$data.="Stupid content here...</body></html>";

my $gzipped_data;
my $gzip = gzip \$data => \$gzipped_data;

my $response = HTTP::Response->new;

$response->code( 200 );
$response->header( 'Content-type'     => 'text/html' );
$response->header( 'Content-encoding' => 'gzip' );
$response->header( 'Content-length'   => length $gzipped_data );


$response->content( $gzipped_data );

print $response->as_string;
