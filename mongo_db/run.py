from mongo_db.src.addressbook import main as run_app
from mongo_db.src.seeds import create_contact

'''
Для старту потрібно запустити контейнер Docker MongoDB
docker run -d -p 27017:27017 --name mongo_app mongo
'''

if __name__ == '__main__':
    create_contact(5)  # Заповнення
    run_app()
