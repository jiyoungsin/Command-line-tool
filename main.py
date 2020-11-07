import os
import click
import functions


@click.group()
@click.version_option(version="v1.0", prog_name="Link Checker")
def cli():
    """
    Command-line tool to consider if urls are good, bad, or unknown
    """


@click.command()
@click.option("-i", "--ignore", is_flag=True, help="Ignores list of urls in file")
def print_urls(ignore):
    """
    Prints the urls on terminal
    """
    # if ignore:
    #     urls_list = functions.get_urls_from_file("urls.txt")
    if not ignore:
        click.echo(str(functions.get_urls_from_file("urls.txt")))


@click.command()
def ignore_urls():
    """
    Command-line tool to ignore urls
    """


@click.command()
@click.argument("endpoint")
@click.option("-i", "--ignorfile", type=click.Path(), default=None)
def check_urls(endpoint, ignorfile):
    """
    Check urls retrieved from ENDPOINT.
    """
    ignore_urls_set = set(functions.get_urls_from_file(ignorfile)) if ignorfile else set()

    urls = functions.get_urls_from_url(endpoint)
    urls = set(urls).difference(set(ignore_urls_set))
    links_with_status_code = functions.check_urls(urls)
    for result in links_with_status_code:
        url = list(result.keys())[0]
        status = str(list(result.values())[0])
        if status == "200":
            click.secho(url + " : " + status, fg="green")
        elif status in ("400", "404"):
            click.secho(url + " : " + status, fg="red")
        else:
            click.secho(url + " : " + status, fg="yellow")


@click.command()
@click.option("-f", "--format-files", is_flag=True, help="Formats all python files")
def format_code(format_files):
    """
    Format our python scripts
    """
    if not format_files:
        os.system("black *.py")


@click.command()
@click.option("-l", "--lint", is_flag=True, help="Lint's all python files")
def lint_code(lint):
    """
    Format our python scripts
    """
    if not lint:
        os.system("pylint *.py")


cli.add_command(print_urls)
cli.add_command(check_urls)
cli.add_command(lint_code)
cli.add_command(format_code)


if __name__ == "__main__":
    cli()
