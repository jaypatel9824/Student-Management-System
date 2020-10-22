#!C:\Strawberry\perl\bin\perl.exe -Tw
use strict;
use DBI;
use DBD::mysql;
use HTML::TEMPLATE;
use CGI ':standard';

#print $q->header;
our $platform = "mysql";
our $database = "test";
our $host = "localhost";
our $port = "3306";
our $tablename = "inform";
our $user = "root";
our $pw = "";
print "\n";
my $dsn = "DBI:mysql:database=$database;host=$host"; 
my $connect_me = DBI->connect($dsn, $user, $pw);

my $run_query = $connect_me->prepare("SELECT * FROM $tablename");
$run_query->execute();

print <<HTML_PAGE;
<html>
<head>
<title>Students Table</title>
</head>
<body>
<h3>Printing list of Students information from database</h3>
<table style="border:2px solid black; text-align: center; border-collapse: collapse;">
<thead style="background: #6BBEF4; border-bottom: 5px solid #FFFFFF;">
<tr style="border:2px solid black; padding: 3px 2px; font-weight: bold;">
<th style="border:2px solid black; padding: 3px 2px;">Id</th>
<th style="border:2px solid black; padding: 3px 2px;">FirstName</th>
<th style="border:2px solid black; padding: 3px 2px;">LastName</th>
<th style="border:2px solid black; padding: 3px 2px;">Home</th>
<thead>
</tr>
HTML_PAGE


while(my $que=$run_query->fetchrow_hashref()) {
  #print "<b>Value returned:</b> $que->{time}\n";
} 


$run_query->execute();
while(my @que = $run_query->fetchrow_array()){
print "<tr>
<td style='border:2px solid black; border-collapse: collapse;'>
$que[0]\n\t
</td>
<td style='border:2px solid black; border-collapse: collapse;'>
$que[1]\n\t
</td>
<td style='border:2px solid black; border-collapse: collapse;'>
$que[2]\n\t
</td>
<td style='border:2px solid black; border-collapse: collapse;'>
$que[3]\n\t
</td>";
}
print "</tr>";
print "</table>";
exit;