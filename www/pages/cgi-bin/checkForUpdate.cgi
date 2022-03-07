#!/bin/sh

curl -k -o /tmp/gitVersion https://raw.githubusercontent.com/LOKisGithub/LokisAsicTester/main/version
if cmp -s /tmp/gitVersion /mnt/card/version; then
	echo "Your Version is up2date"
else
	echo "New Version available (check https://github.com/LOKisGithub/LokisAsicTester for update)"
fi
