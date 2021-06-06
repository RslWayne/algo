from threading import Thread
import requests
import time
start = time.time()
url = 'https://reqres.in/api/users?page=2'
results = []
def get_response(url):
    response = requests.get(url)
    results.append(response.json())
def main():
    threads = []
    for i in range(5000):
        process = Thread(target = get_response,args=(url,))
        process.start()
        threads.append(process)
    for i in threads:
        i.join()
main()
print(time.time() - start)
print(len(results))

