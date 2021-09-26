import click

from lxml import html
from requests import request


@click.command()
@click.option('-l', '--link', required=True, help='Link to a song in some of the Music Services')
@click.option('-s', '--services', envvar='SW_SERVICES',
			  help='Comma separated list of Music Services to be shown in output')
@click.option('-o', '--output', default='markdown', envvar='SW_OUTPUT',
			  type=click.Choice(['markdown', 'hyphen'], case_sensitive=False), help='Output template')
def main(output, link, services):
	template = get_output_template(output)
	service_link_dict = get_links(link)

	if services is not None:
		services = services.split(",")

	for service, link in service_link_dict.items():
		if services is not None:
			if any(map(service.__eq__, services)):
				print(template.format(service, link))
		else:
			print(template.format(service, link))


def get_output_template(output):
	if output == 'hyphen':
		template = '{} - {}'
	elif output == 'markdown':
		template = '[{}]({})'
	else:
		raise click.BadOptionUsage(output, 'Unsupported output type', ctx=None)
	return template


def get_links(initial_link):
	url = "https://songwhip.com/"
	response = request("POST", url, data=initial_link)
	links_page = request("GET", response.json()['url'])
	doc = html.fromstring(links_page.content)
	elements = doc.xpath("//div/a[contains(@href,'http')][not(contains(@href,'songwhip'))]")
	service_link_dict = {el.xpath("div[contains(@class,'regular')]")[0].text: el.get('href') for el in elements}
	return service_link_dict


if __name__ == "__main__":
	main()
