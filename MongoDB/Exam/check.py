import docker

def is_container_running(container_name):
    try:
        # Connect to Docker
        client = docker.from_env()
        
        # Get the container by name
        container = client.containers.get(container_name)
        
        # Check if the container is running
        if container.status == 'running':
            print(f"The container '{container_name}' is running.")
            return True
        else:
            print(f"The container '{container_name}' is not running. Status: {container.status}")
            return False
    except docker.errors.NotFound:
        print(f"The container '{container_name}' does not exist.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Check if the MongoDB container is running
is_container_running("my_mongo")


mongoimport -d sample -c books --authenticationDatabase admin --username datascientest --password dst123 --file data/db/books.json



scp ubuntu@3.251.6.163:/home/username/example.txt ~/Downloads/

scp -i data_enginering_machine.pem ubuntu@3.251.6.163:/home/ubuntu/exam_MongoDB_STUTZENBERGER.tar ~/Downloads/



