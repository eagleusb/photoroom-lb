# Photoroom Inference Load Balancing

## Testing

```sh
curl -XPOST -H 'Content-Type: application/json' -d@test/model.json 0:5000/inference
```
