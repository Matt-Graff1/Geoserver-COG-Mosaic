import boto3
import botocore
import sys
import os

from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
SECURE = os.getenv("SECURE")
HOST = os.getenv("HOST")
print(HOST)

DEFAULT_BUCKET = os.getenv("DEFAULT_BUCKET")

#* -----FUNCTIONS-----

try:
     s3 = boto3.client('s3', aws_access_key_id =ACCESS_KEY_ID, aws_secret_access_key=SECRET_KEY, use_ssl=SECURE, endpoint_url=HOST)
     print('s3 Client object created...')
except Exception as e:
        print('Error, s3 client object creation failed!')
        print(e)

def upload_file(file_path: str, 
                bucket_name: str, 
                object_name=None, 
                permissions='public-read'):
    """
    This function takes a file name, a bucket name, an object name, and permissions and 
    returns a boolean of whether or not the upload was a success.

    Arguments:
        file_path: String of path of file to be uploaded to the specified bucket (e.g. 'W:/ilmb/vic/geobc/_project_folder_template/Project_Summary.xlsx')
        bucket_name: String of name of the bucket
        object_name: String of name of desired object name that is uploaded to 
        the bucket. By default, this will be a only the filename.
        permissions: Permissions of access to this file. (Note: by default, the permissions are set to public read-only - unless otherwise specified)

    Returns:
        Boolean (true/false) of the result of the upload (success/fail).
        
    Raises: 
        Exceptions raised will display an error message and be logged in the export.log file 

    """
    if object_name is None:
        object_name = os.path.basename(file_path)
    try:
        print(f'Uploading object: {object_name}')
        response = s3.upload_file(file_path, bucket_name, object_name, ExtraArgs={'ACL': permissions})
        print('File uploaded successfully')
    except Exception as e:
        print('Cannot upload file:')
        print(e)
        return False
    return response

def multi_upload(input_dict: dict, 
                 bucket_name: str, 
                 permissions='public-read'):
    """
    This function takes a dictionary of filepaths and object names, a bucket name, and permissions 
    and returns a string message of whether or not the upload was a success.

    Arguments:
        input_dict: Dictionary in the format of - Path of file to be uploaded to the specified bucket, 
        and desired object name for said file (e.g. {'W:/ilmb/vic/geobc/_project_folder_template/Project_Summary.xlsx':'_project_folder_template/Project_Summary.xlsx'})
        bucket_name: String of name of the bucket
        permissions: Permissions of access to these files. (Note: by default, the permissions are set to public read-only - unless otherwise specified)

    Returns:
        String message of whether or not the upload was a success
        
    Raises: 
        Exceptions raised will display an error message and be logged in the export.log file 

    """
    amount_success = 0
    amount_fail = 0
    links = []
    for file_name, object_name in input_dict.items():
        # arcpy.AddMessage.debug('Uploading object: ' + object_name)
        try:
            if amount_fail <= 2:
                response = s3.upload_file(file_name, bucket_name, object_name, ExtraArgs={'ACL': permissions})
            else:
                print('To many failed attempts. Exiting process!')
                sys.exit()
        except Exception as e: 
            amount_fail += 1
            print('Cannot upload file:')
            print(e) 
        else:
            amount_success += 1
            print(f'successfully uploaded: {file_name}')
            links.append(create_url(bucket_name, object_name))
        # finally:
        #     arcpy.AddMessage(f'Multi-upload in progress... {amount_success} successful, {amount_fail} failed.')
    print(f'Multi-upload completed. {amount_success} successful, {amount_fail} failed.')
    return links

def export_url_list(bucket_name: str, 
                    folderpath=str):
    """
    This function takes a bucket name and generates a URL download link for every object (that is not a "directory")
    and lists them all in a CSV file output. 

    Arguments:
        bucket_name: String of name of the bucket
        folderpath: Folderpath of url CSV export

    Returns:
        Nothing
        
    Raises: 
        Exceptions raised will display an error message and be logged in the export.log file 
    """
    try:
        output_dict = {}
        objects = s3.list_objects_v2(Bucket=bucket_name)
        for object in objects['Contents']:
                object = object['Key']
                if not object.endswith('/'):
                    output_dict[object] = create_url(bucket_name, object)

        with open(f'{folderpath}/url_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["Object Name", "URL"]

            writer.writerow(field)
            for key, value in output_dict.items():
                writer.writerow([key, value])
    except Exception as e:
        print('Could not generate URL list')
        print(e)
    print(f'URLs have been generated and written to file: {folderpath}/url_list.csv')


def create_url(bucket_name: str,
            object_name: str):
 
    """
            #? can add expiration eventually
    This function takes a bucket name, an object name, and an expiration time (in seconds) and generates a URL download link for the object.

    Arguments:
        bucket_name: String of name of the bucket
        object_name: Name of the object (key) that the URL will be pointed to

    Returns:
        Link of output (object download) URL
        
    Raises: 
        Exceptions raised will display an error message and be logged in the export.log file
    """
    try:
        response = HOST + bucket_name + '/' + object_name
    except:
        print('failed to create URL')
        return None
    # arcpy.AddMessage.debug(f'The url has been generated for {object_name}') 
    return response

#* -----MAIN-----

# Will display objects in the default bucket if GetConnection.py is run as a script
if __name__ == '__main__':
    target_bucket = DEFAULT_BUCKET

    try:
        objects = s3.list_objects_v2(Bucket=target_bucket)
        for object in objects['Contents']:
            print(object['Key'])        
        print('success!')
    except botocore.exceptions.ClientError as e:
        print('There is a AWS error message from the server:')
        print(e)
    except botocore.exceptions.ConnectionClosedError as e:
        print('Server closed the connection!')
        print(e)
    except Exception as e:
        print('Unhandled exception!')
        print(e)