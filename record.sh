echo "press y to start recording, press t to stop recording."
read op
if [ $op == "y" ]; then
    (adb shell getevent| grep -e "event.:" | awk '{print $2" " $3" " $4}' > log.txt) &
fi


read op
while [ $op != "t" ]; do
    read op
done

#kill getevent.
pkill -f "getevent"
echo "record finished."

echo "press p to replay recording."
read op
if [ $op != "p" ]; then
    read op
fi
#replay
python play.py
