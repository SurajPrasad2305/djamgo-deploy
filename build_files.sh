echo "BUILD_START"
python3.9 -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo "BUILD_END"