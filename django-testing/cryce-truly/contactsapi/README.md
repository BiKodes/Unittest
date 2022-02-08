## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)



## Table of contents

* [About](#about)

* [Acknowledgements](#acknowledgements)

* [API Reference](#api-reference)

* [Features](#features)

* [Tech Stack](#tech-stack)

* [Local Development](#local-development)

* [Environment Variables](#environment-variables)

* [Run Locally](#run-locally)

* [Running Tests](#running-tests)

* [Demo](#demo)

* [Lessons Learned](#lessons-learned)

* [Feedback](#feedback)

* [License](#license)

# About

**Version 1.0.0**

This is a RESTFUL API that manages personal contacts of the user and maps every single contact to its owner with their specific images respectively.


## Acknowledgements

I am blessed to be surrounded by many extraordinary people in my life.Without them, it would not be possible for me to do what I do and advance in my mission of being an apristine Software Craftsman. I am deeply grateful.

I must offer special thanks to: 

- Engineer [Josephat Macharia](https://gitlab.com/joemash) 

Whom I count on in so very many ways and whose enthusiasm for software development always inspires me.


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.



## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform



<!-- # Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)   -->

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`



## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express

## Running Tests

To run tests, run the following command

```bash
  npm run test
```

## Demo

Insert gif or link to demo

## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


## Feedback

If you have any feedback, please reach out to us at fake@fake.com

## License

[MIT](https://choosealicense.com/licenses/mit/)