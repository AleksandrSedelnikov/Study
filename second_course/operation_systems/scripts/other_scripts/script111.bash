while true
do
  read -r lineA <&4
  read -r lineB <&5
  if [ -z "$lineA" -o -z "$lineB" ]; then
    break
  fi
  var=$(($lineA^$lineB))
  echo "Значение 1 из первого файла: "$lineA
  echo "Значение 2 из второго файла: "$lineB
  echo "Сложение по модулю 2 этих значений: "$var
done 4<text1 5<text2
