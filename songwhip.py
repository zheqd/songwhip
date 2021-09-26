import click

from lxml import html
from requests import request


@click.command()
@click.option('-o', '--output', default='markdown', envvar='SW_OUTPUT',
			  type=click.Choice(['markdown', 'hyphen'], case_sensitive=False), help='Output template')
@click.option('-l', '--link', help='Link to a song in some of the music services')
def main(output, link):
	if output == 'hyphen':
		template = '{} - {}'
	elif output == 'markdown':
		template = '[{}]({})'
	else:
		raise click.BadOptionUsage(output, 'Unsupported output type', ctx=None)

	url = "https://songwhip.com/"
	response = request("POST", url, data=link)
	links_page = request("GET", response.json()['url'])
	doc = html.fromstring(links_page.content)

	elements = doc.xpath("//div/a[contains(@href,'http')][not(contains(@href,'songwhip'))]")
	service_link_dict = {el.xpath("div[contains(@class,'regular')]")[0].text: el.get('href') for el in elements}

	# to remove service from output - comment or remove it from output_services list
	output_services = [
		'Amazon Music',
		'Apple Music',
		'Deezer',
		'Napster',
		'Spotify',
		'Tidal',
		'Yandex',
		'YouTube',
		'YouTube Music',
	]

	for service, link in service_link_dict.items():
		if any(map(service.__eq__, output_services)):
			print(template.format(service, link))


if __name__ == "__main__":
	main()
