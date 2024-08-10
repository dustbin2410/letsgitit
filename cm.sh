
python util.py --currbr brname
name=`cat brname`
rm -rf brname


# Get current ID
dat='./cur_id.txt'
val=`cat $dat`
echo Curr index: $val

# Update new ID
val=`expr $val + 1`
echo Next index: $val
echo -n $val > $dat

# Changing source code
nmsg="Add message $name:$val"
echo >> zmsg.txt
echo -n $nmsg >> zmsg.txt

# Commit the change
echo "Check current status"
echo "----------------------------------------"
git status
echo "----------------------------------------"
git add .
git commit -m "$nmsg"
echo "----------------------------------------"
git log --oneline
echo "----------------------------------------"
