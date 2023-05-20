# JNTU RESULTS REST API

The JNTU RESULTS REST API is a web API that allows you to scrape results for both regular and supplementary exams, based on a given roll number.

## Features

- Fetch regular and supplementary exam results for a specific roll number.
- Retrieve detailed information about each result, including subject-wise marks, total marks, and grade.

## Running Locally

To run the API locally in development mode, follow these steps:

1. Clone the repository:

<pre>
git clone https://github.com/JNTU-Results/JNTU-Results-Backend
</pre>

2. Install the required dependencies:

<pre>
pip install -r requirements.txt
</pre>

3. Start the development server:

<pre>
uvicorn results.main:app --reload

</pre>

The API will be accessible at `http://localhost:8000`.

## Documentation

For detailed information about the available endpoints and how to use the API, refer to the [API documentation](API_DOCUMENTATION.md). The documentation provides examples and explanations of each endpoint and the expected response format.

## Need Help or Found a Bug?

If you need assistance with setup, deployment, or implementing special features, or if you simply want to chat with the developers, feel free to contact us via email at [jnturesultsindia@gmail.com](mailto:jnturesultsindia@gmail.com).

If you discover any bugs or issues with the API, please [submit an issue](https://github.com/JNTU-Results/JNTU-Results-Backend/issues) on GitHub. We appreciate your feedback and contributions.

## License

The JNTU RESULTS REST API is open-source software licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). You are free to use, modify, and distribute this software in accordance with the terms and conditions of the GPL-3.0 license.

## Contributing

We welcome contributions to the JNTU RESULTS REST API! If you would like to contribute bug fixes, new features, or improvements, please submit a pull request to the `develop` branch. Make sure to follow the contribution guidelines provided in the repository.

By contributing to this project, you agree to abide by the [Code of Conduct](https://github.com/JNTU-Results/JNTU-Results-Backend/blob/main/CODE_OF_CONDUCT.md) and the terms outlined in the [Contributor License Agreement](https://github.com/JNTU-Results/JNTU-Results-Backend/blob/main/CONTRIBUTING.md).

We appreciate and value your contributions to make this project better!


We appreciate and value your contributions to make this project better!
