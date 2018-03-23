
- To run the image:
```bash
    docker run --rm -tid --name <some-name> -v ${PWD}/armbook:/app/public/ -p 80:80 -p 443:443 <image-name>
```
