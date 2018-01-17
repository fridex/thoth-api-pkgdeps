thoth-api-pkgdeps
-----------------

A simple API service for the `thoth-pkgdeps tool <https://github.com/fridex/thoth-pkgdeps>`_.

To run a local setup, just fire:

.. code-block:: console

  $ docker-compose up

The api service will be available at http://localhost:34000/. You can send a JSON to be analyzed to /api/v1/extract-build-log. See OpenAPI/Swagger documentation available in OpenAPI/Swagger UI at http://localhost:34000/api/v1/ui.

