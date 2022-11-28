from recipe_scrapers import scrape_me

import json
import requests


def createRecipe(database_id, headers, name, servings, time, children, url, image, icon):
    createUrl = 'https://api.notion.com/v1/pages'
    payload = {
        "parent": {
            "database_id": database_id
        },
        "cover": {
            "type": "external",
            "external": {
                "url": image
            }
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Servings": {
                "rich_text": [
                    {
                        "text": {
                            "content": servings
                        }
                    }
                ]
            },
            "Time": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(time)
                        }
                    }
                ]
            },
            "URL": {
                "url": str(url)
            },
        },
        "children": children,
        "icon": {
            "type": "emoji",
            "emoji": icon
        },

    }

    data = json.dumps(payload)
    res = requests.request("POST", createUrl, headers=headers, data=data)

    return ([res.status_code, res.text])
    print(res.status_code)
    print(res.text)
    # recipe = mapNotionResultToMovie(r.json())
    # return recipe


def children_format(ing, inst):
    children = []
    # ingredients
    children.append(
        {
            "object": 'block',
            "type": 'heading_2',
            "heading_2": {
                    "rich_text": [
                        {
                            "type": 'text',
                            "text": {
                                "content": 'Ingredients',
                            },
                        },
                    ],
            },
        },
    )
    for i in ing:
        children.append(
            {
                "object": 'block',
                "type": 'to_do',
                "to_do": {
                    "rich_text": [
                          {
                              "type": 'text',
                              "text": {
                                  "content": str(i),
                              },
                          },
                    ],
                    "checked": False,
                },
            },)

    children.append(
        {
            "object": 'block',
            "type": 'heading_2',
            "heading_2": {
                    "rich_text": [
                        {
                            "type": 'text',
                            "text": {
                                "content": 'Instructions',
                            },
                        },
                    ],
            },
        },
    )
    inst = inst.splitlines()
    for x in inst:
        children.append(
            {
                "object": 'block',
                "type": 'paragraph',
                "paragraph": {
                    "rich_text": [
                          {
                              "type": 'text',
                              "text": {
                                  "content": str(x),
                              },
                          },
                    ],
                },
            },)
    return children


def main(input1, token, database_id, icon):
    scraper = scrape_me(input1)
    #token = 'secret_Q1mFXfdB9azYxEoTWBAubBIyGDhBs2xKEgwIF5lvtM6'
    #database_id = '6165fd1b85d942ea96264d99b61cc241'

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    return (createRecipe(database_id, headers, scraper.title(),
                         scraper.yields(), scraper.total_time(), children_format(scraper.ingredients(), scraper.instructions()), input1, scraper.image(), icon))
