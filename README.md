# Delivery Order Pricing Service

This project provides a

## Features

1. Calculate delivery fees based on distance
2. Apply surcharge for small orders.
3. Handle API requests for venue data.
4. Return JSON responses with pricing details.

## Installation

1. Install dependencies: `pip install -r requirements.txt `
2. run the flask server: ` python main.py`
3. the service will run at `http://localhost:8000`

## API Usage

### Endpoint

`GET /api/v1/delivery_order_price`

### Query Parameters:

| Parameter  | Type   | Required | Description                    |
| ---------- | ------ | -------- | ------------------------------ |
| venue_slug | string | Yes      | Unique identifier of the venue |
| cart_value | int    | Yes      | The total cart value           |
| user_lat   | float  | Yes      | User's latitude                |
| user_lon   | float  | Yes      | User's longitude               |

## Example Request:

`curl "http://localhost:8000/api/v1/delivery_order_price?venue_slug=test-venue&cart_value=50&user_lat=60.1699&user_lon=24.9384" `

## Example Response:

```
{
    "cart_value": 1000,
    "delivery": {
        "distance": 176,
        "fee": 190
    },
    "small_order_surcharge": 0,
    "total_price": 1190
}
```
