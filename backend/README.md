# miro-podcast-studio

This project cotains API codebase for Miro Podcast Studio.

API provides endpoints to create a podcast voice with given mindmap structure.

![Architecture](images/architecture.png)

## Endpoints

### `POST /podcast`

This endpoint takes mindmap and other configurations in order to create a podcast. An example input paramter is as follows;
```json
{
    "mindmap": [], //An array structure given from miro 
    "presenter_name": "sarah", // sarah | ryan,
    "podcast_name": "Techy Talks",
    "podcast_language": "en" // en | tr | fr | de | pt | it
}
```
### Mindmap Structure
This endpoint basically takes mindmap as a parameter which in same format in miro which is an array of dictionaries.
<details>
  <summary>Example Mind Map Structure</summary>

```json
[
    {
        "type": "mindmap_node",
        "id": "3458764576255007807",
        "parentId": "3458764576255007799",
        "origin": "center",
        "relativeTo": "parent_center",
        "createdAt": "2024-01-20T13:23:13.542Z",
        "createdBy": "3458764575467351574",
        "modifiedAt": "2024-01-20T13:30:50.551Z",
        "modifiedBy": "3458764575467351574",
        "connectorIds": [],
        "x": 291.5000000000001,
        "y": 52,
        "width": 144,
        "height": 36,
        "nodeView": {
            "type": "text",
            "content": "Customer feedback",
            "style": {}
        },
        "childrenIds": [],
        "isRoot": false,
        "layout": "horizontal",
        "direction": "end"
    },
    {
        "type": "mindmap_node",
        "id": "3458764576255007799",
        "parentId": "3458764576254974741",
        "origin": "center",
        "relativeTo": "parent_center",
        "createdAt": "2024-01-20T13:23:13.541Z",
        "createdBy": "3458764575467351574",
        "modifiedAt": "2024-01-20T13:30:50.551Z",
        "modifiedBy": "3458764575467351574",
        "connectorIds": [],
        "x": 368.5,
        "y": 260,
        "width": 238.99999999999997,
        "height": 36,
        "nodeView": {
            "type": "text",
            "content": "Monitor and analyze performance",
            "style": {}
        },
        "childrenIds": [
            "3458764576255007802",
            "3458764576255007805",
            "3458764576255007807"
        ],
        "isRoot": false,
        "layout": "horizontal",
        "direction": "end"
    },
]
```

</details>  

### CSV Creation
Then creates a CSV file to represent that mindmap in text format. This CSV will be added to prompt for ChatGPT.

We implemented Depth First Search tree traversal algorithm in order to create CSV from given mindmap structure.

<details>
  <summary>Example Mind Map CSV</summary>

    ```csv
    0,1,2,
    MainTopic,,
    MainTopic,SubTopic,SubSubTopic
    MainTopic,SubTopic2,
    MainTopic,SubTopic3,SubSubTopic
    ```

</details>  

### Creating Podcast Text
In order to create podcast text we utilize ChatGPT. We prompted ChatGPT to create podcast text within given Mind Map CSV and other additional parameters like language and podcast name.

You can find out prompts at `utils/minmap.py` file. And here is an example of them.

```
Use English rest of the text.I have a mind map, I want to create a podcast from the following mindmap.  Act as a podcast presenter called {presenter_name} from {podcast_name} and creat podcast transcript. I will use your output to create a podcast. Use friendly lang:. Don't include additional text only content to read. It should be less than 1 minute. Dont use too long transcript.
```

### Podcast Voiceover Generation
After the podcast text generation step we utilize a text2speech engine called ElevenLabs in order to create podcast voice from given text input.


### Intro and Outro Musics
After podcast voice generation we add intro and outro music to that voice to make podcast feeling more realistic. After that step we push our generation to AWS S3 to serve files efficiently. Here is an example podcast that is created by us.


https://miro-to-podcast.s3.eu-west-2.amazonaws.com/podcast_cf0326eb-3831-4f41-99a7-339626f15702.mp3