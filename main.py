import functions
import click


@click.group()
@click.version_option(version="v1.0", prog_name="Link Checker")
def cli():
    """
    Command-line tool to consider if urls are good, bad, or unknown
    """
    pass


@click.command()
@click.option("-i", "--ignore", is_flag=True, help="Ignores list of urls in file")
def print_urls(ignore):
    if ignore:
        urls_list = functions.read_urls_from_file("urls.txt")

        print("@@@@@")
    click.echo(str(functions.read_urls_from_file("urls.txt")))


@click.command()
def ignore_urls():
    pass


@click.command()
@click.argument("endpoint")
@click.option("-i", "--ignorfile", type=click.Path(), default=None)
def check_urls(endpoint, ignorfile):
    """
    Check urls retrieved from ENDPOINT.
    """
    ignore_urls = set(functions.get_urls_from_file(ignorfile)) if ignorfile else set()

    urls = functions.get_urls_from_url(endpoint)
    urls = set(urls).difference(set(ignore_urls))
    links_with_status_code = functions.check_urls(urls)
    for result in links_with_status_code:
        url = list(result.keys())[0]
        status = str(list(result.values())[0])
        if status == "200":
            click.secho(url + " : " + status, fg="green")
        elif status == "400" or status == "404":
            click.secho(url + " : " + status, fg="red")
        else:
            click.secho(url + " : " + status, fg="yellow")


cli.add_command(print_urls)
cli.add_command(check_urls)

if __name__ == "__main__":
    cli()
