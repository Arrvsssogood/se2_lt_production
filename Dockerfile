  build-docker:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: check-code            # Wait for lint+test to pass first!

    steps:
      - name: Get the code
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t my-app .

      - name: Verify image was created
        run: docker images | grep my-app
