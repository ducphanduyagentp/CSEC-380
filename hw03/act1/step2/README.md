- The python scripts are put in the root directory of the container. The images are saved to /a1.2-images
- The code is being run 100 times by the container as requested.
- To be able to view the images after running the container, one of the following ways can be used:
    - Recommended:
    `docker run --rm -v "$(pwd)"/images:/a1.2-images <image-name>`
    The images will be saved to `./images`
    - Interact with the container:
    `docker run --rm -ti <image-name> /bin/sh`