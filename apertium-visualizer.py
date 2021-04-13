import re
from lxml import etree
from graphviz import Digraph

class Analyser:

	def __init__(self):
		pass

	def analyse(word: str) -> list[tuple[str, int]]:
		"""
		Perform a simple morphological analysis lookup.

		Parameters
		----------
		- word: The word to analyse

		Returns
		-------
		list of tuples with analysis string and weight
		"""		
		pass

	def parse_anaysis(analysis: str) -> dict:
		"""
		Parse the analysis string and return a dict with structured data.

		Parameters
		----------
		- analysis : The analysis string

		Returns
		-------
		Dictionary with the following structure
		```example
		{
	    morphemes: [
        {root:"rootword1", pos:[pos1, pos2] }
        {root:"rootword2", pos:[pos1, pos2] }
	    ]
	    weight: 200
		}
		```
		"""		
		pass

	def generate_graph(analysed: dict) -> bool:
		"""
		Generate Graphviz file.

		Parameters
		----------
		- analysed : The structured analysis Dictionary

		Returns
		-------
		True, create a file with the same name
		```
			digraph {
				A
				B
				A -> B
			}
		```
		"""		
		pass		

def fun(txt):
	return txt if len(txt) else 'ε'

def main():
	dot = Digraph(format='png')
	filename = 'apertium-tet.tet'
	tree = etree.parse(f'examples/{filename}.dix')
	root = tree.getroot()

	for section in root.findall('section'):
		for e in section.findall('e'):
			node = e.findtext('i')
			print(node)
			dot.node(node)
	
	for pardef in root.findall('pardefs/pardef'):
		if re.search ('__adj', pardef.attrib['n']):
			for e in pardef.findall('e/p'):
				surface_form = fun(e.findtext('l'))
				lexical_unit = fun(e.findtext('r'))
				dot.edge(surface_form, lexical_unit)

	dot.render(f'{filename}.gv')

if __name__ == '__main__':
	main()