$exclude = @("venv", "RPAChallenge.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPAChallenge.zip" -Force