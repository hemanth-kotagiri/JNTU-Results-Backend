<h1 align="center"><a href="http://results.jntuh.ac.in/" target="_blank">JNTU</a> Results REST-API</h1>

The JNTU Results REST-API is a RESTFul Service that allows you to fetch results
for all regulations, and of all types (regular and supplementary exams), based
on a given specific valid roll number.

<h4 align="center">We need your help!</h4>
Currently, we only provide JNTU, Hyerabad results in our website, and the
backend also only serves JNTUH results as of now. Since we are coming from JNTU
Hydrabad background, for us to expand to JNTU-A and JNTU-K, we need someone to
teach us on how you fetch your results in your portal.

1. JNTU, Hyderabad ✅ - Providing and improving
2. JNTU, Kakinada ⌛- Working to add to this API
3. JNTU, Anantapur ⌛ - Working to add to this API

**If you are a JNTU-A or JNTU-K affiliated student, please reach out to us at
jnturesultsindia@gmail.com. We need your help in creating the website for you!**

## General Questions

Q. **What are we currently working on?**

- Currently, we are working on improving JNTU, Hyderabad Engineering Results.
- We are also working to expand to JNTUH B.Pharmacy results as well providing
  the same features just like we did for Engineering Results.
- Soon, we are planning to expand to other JNT, Universities across Andhra
  Pradesh such as JNTU-Kakinada and JNTU-Anantapur.

## Features

We have a lot of features that we provide, but the below is the most used one.
- Fetch regular and supplementary exam results for a specific roll number.
- Retrieve detailed information about each result, including subject-wise marks,
  total marks, and grade.

## Documentation

An official documentation website for the API is available at [JNTU API
Documentation](https://hemanth-kotagiri.github.io/sgpa-rest-api-docs/). Please
check it out for more information.

**Note that the response is in the form of JSON only**

## Endpoints

```
- /                   - This is where you are right now.
- /all-r18            - Fetch all semester results of R18 batch students
- /result             - A query parameter specific endpoint.
- /calculate          - Fetch the SGPA along with other details.
- /new/all            - Fetch all results links (Supplementary and Regular).
- /new/all/regular    - Fetch all regular results links.
- /new/all/supply     - Fetch all regular supplementary links.
- /api                - A Query parameter endpoint to get result of an exam given hallticket, date of birth, degree, examCode, eType, type and result.
- /api/calculate      - A Query parameter endpoint to get result of an exam given hallticket, date of birth, degree, examCode, eType, type and result with sgpa.
- /api/bulk/calculate - A Query parameter endpoint to get results of multiple halltickets given other parameters such as degree, examCode, eType, type, result and grade along with SGPA.
- /new/               - Returns all results links in unordered fashion
- /notifications      - Returns all the latest released notifications
```

Refer to the official documentation for detailed API Reference. Below is
just a sample from one endpoint. Please click
[here](https://hemanth-kotagiri.github.io/sgpa-rest-api-docs/).

## Running Locally

To run the API locally in development mode, follow these steps:

1. Clone the repository:

<pre> git clone https://github.com/JNTU-Results/JNTU-Results-Backend </pre>

2. Install the required dependencies:

<pre> pip install -r requirements.txt </pre>

3. Start the development server:

<pre> uvicorn results.main:app --reload

</pre>

The API will be accessible at `http://localhost:8000`.

## Need Help or Found a Bug?

If you need assistance with setup, deployment, or implementing special features,
or if you simply want to chat with the developers, feel free to contact us via
email at [jnturesultsindia@gmail.com](mailto:jnturesultsindia@gmail.com).

If you discover any bugs or issues with the API, please [submit an
issue](https://github.com/JNTU-Results/JNTU-Results-Backend/issues) on GitHub.
We appreciate your feedback and contributions.

## License

The JNTU RESULTS REST API is open-source software licensed under the [GNU
General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). You
are free to use, modify, and distribute this software in accordance with the
terms and conditions of the GPL-3.0 license.

## Contributing

Contributions are always welcome! If you would like to contribute bug fixes, new
features, or improvements, please submit a pull request to the `develop` branch.

**⚠️ Make sure to follow the contribution guidelines provided in the repository.**

By contributing to this project, you agree to abide by the [Code of
Conduct](https://github.com/JNTU-Results/JNTU-Results-Backend/blob/main/CODE_OF_CONDUCT.md)
and the terms outlined in the [Contributor License
Agreement](https://github.com/JNTU-Results/JNTU-Results-Backend/blob/main/CONTRIBUTING.md).

We appreciate and value your contributions to make this project better!
