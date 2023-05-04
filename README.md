```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗                       
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║                       
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║                       
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║                       
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║                       
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                       
                                                                            
██████╗  ██████╗  ██████╗ ████████╗███████╗████████╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║   ██║██║   ██║   ██║   ███████╗   ██║   ██████╔╝███████║██████╔╝
██╔══██╗██║   ██║██║   ██║   ██║   ╚════██║   ██║   ██╔══██╗██╔══██║██╔═══╝ 
██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████║   ██║   ██║  ██║██║  ██║██║     
╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
```

# Python Bootstrap

[![language:Python](https://img.shields.io/badge/language-Python-blue)]()

## Environmental Variables

Required environment variables:

| Name    | Example          | Description |
| ------- | ---------------- | ----------- |
| CONTEXT | DEV, STAGE, PROD | environment |

## Running locally

After cloning down the repository run `run-dev-api.sh` to drop into a python
environment.

To start flask you must run the following.

```
flask run --host=0.0.0.0
```

## Testing

After cloning down the repository run `pytest.sh` to drop into a python test
environment.

```
pytest tests/e2e/*.py -rP -s
```

## Building

[TODO]

## Deployment

[TODO]

## License

Apache License, Version 2.0

# Version

0.1

## Contributing

1. Fork it (<https://github.com/ethandunford/python-bootstrap/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Contributors

- [ethandunford](https://github.com/ethandunford) Ethan Dunford - Creator
