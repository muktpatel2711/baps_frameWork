import json
import pandas as pd
import requests
import asyncio

excel_file ="C:\\Users\\supportadmin\\Desktop\\MDS\\MDS_final.xlsx"
data = pd.read_excel(excel_file)

url_column_name = 'Final API URL with filter param and filter value'
statuscode_column_name = 'Actual HTTP Status Code'
message_column_name = 'Actual API Message Code'
Response_message = 'API Response Message Text'
Total_count = 'Total Results Page Count'

async def process_row(index, row):
    url = row[url_column_name]
    if isinstance(url, str) and url.startswith(('http://', 'https://')):
        try:
            # Make API request
            response = await asyncio.to_thread(requests.get, url)
            Status_code = response.status_code
            if Status_code != 404:
                response_json = response.json()
                value = response_json["messages"][0]["responseMessages"][0].get("text")
                response_message = value
                pagination = response_json.get('pagination')
                total_count = pagination.get('totalCount') if pagination else None
                print(value)
                message_type = None
                if 'messages' in response_json and response_json['messages']:
                    for message in response_json['messages']:
                        if 'responseMessages' in message and message['responseMessages']:
                            message_type = message['responseMessages'][0].get('type')
                            if message_type:
                                break
                data.at[index, statuscode_column_name] = Status_code
                data.at[index, message_column_name] = message_type
                data.at[index, Response_message] = response_message
                data.at[index, Total_count] = total_count
            else:
                print("Not Found")
        except Exception as e:
            # Handle exceptions, for example, print an error message
            print(f"Error processing URL '{url}': {e}")
    else:
        # Handle invalid URLs or NaN values, for example, print a warning
        print(f"Invalid URL found at index {index}")

async def main():
    tasks = [process_row(index, row) for index, row in data.iterrows()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

# Save the updated data to the Excel file
data.to_excel(excel_file, index=False)
