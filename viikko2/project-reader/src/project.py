class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        formatted= lambda dependencies_list: '\n'.join([f"- {i}" for i in dependencies_list])
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: \n{formatted(self.authors)}\n"
            f"\nDependencies: \n{formatted(self.dependencies)}\n"
            f"\nDevelopment dependencies: \n{formatted(self.dev_dependencies)}\n"
        )