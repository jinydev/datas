$path = 'd:\site\jinydev\datas\src\numpy\index.md'
$text = [IO.File]::ReadAllText($path, [Text.Encoding]::Default)
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[IO.File]::WriteAllText($path, $text, $utf8NoBom)
