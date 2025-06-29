# Arthur

Arthur is a job search bot that automates searching and filtering job postings based on user defined criteria and key words. Users pay for Arthur's services under a pay-as-you-go subscription model, and are allowed to create new job searches of their interest combining keywords, locations and job posting providers. Arthur runs weekly, gathering results for each of their job searches, which can then be viewed from the UI or directly sent to their email.

## Development

Local development is done in a dedicated Docker container using Docker Compose. However, Podman is preferred as the container provider.
Run commands for frontend via `podman compose exec frontend <command>`. Yarn is used over npm for managing dependencies and running commands.
