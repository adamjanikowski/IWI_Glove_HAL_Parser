#!/usr/bin/env python

import click

from hal_parser.utils.dictionary_reader import parse_dictionary


@click.group()
def cli():
    pass


@cli.command('parse')
@click.option('--ofile', '-o', help='Output file', default='output.txt', type=click.STRING)
@click.option('--gfile', '-g', help='Glove file', default='', type=click.STRING)
@click.option('--input', '-i', help='Input words. Can be delimited by `,` and specified multiple times', multiple=True, type=click.STRING)
def parse(ofile, gfile, input):
    parsed_input = []
    for i in input:
        parsed_input += i.split(',')
    parse_dictionary(parsed_input, ofile, gfile)


if __name__ == '__main__':
    cli()

