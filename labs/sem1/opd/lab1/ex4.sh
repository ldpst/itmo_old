cd lab0
echo -e '\n========4.1========\n'
wc -m beheeyem4 >> beheeyem4 2>&1
cat beheeyem4
echo -e '\n========4.2========\n'
ls -Rl 2>&1 | grep 't$' | sort -k 9 | tail -n 2
echo -e '\n========4.3========\n'
cat */h* 2> /dev/null | sort 1> tmp123
cat -n tmp123
rm tmp123
echo -e '\n========4.4========\n'
ls -ltR 2>tmp | grep " a"
echo -e '\n========4.5========\n'
ls -lrRS | grep -ve "/" -ve "итог" -ve "^$" -ve ":$" | sort -gk 5 | tail -n 2
echo -e '\n========4.6========\n'
cat *6 2>tmp | sort
echo
cd - >/dev/null 
