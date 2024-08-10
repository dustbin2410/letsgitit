# Get current ID
python util.py --nextbr brlog
val=`cat brlog`
rm -rf brlog

echo Curr branch: $val

# Update new ID
val=`expr $val + 1`
echo Next branch: $val

# Creating new branch
name="br$val"

# Commit the change
echo "Check current status"
echo "----------------------------------------"
git status
echo "----------------------------------------"
git branch $name
git checkout $name
echo "----------------------------------------"
git branch
echo "----------------------------------------"