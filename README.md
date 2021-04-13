
tested on python version 3.9.4

docker build --tag apertium .

docker run --interactive --tty \
--name apertium-visualizer \
--mount type=bind,source=`pwd`,target=/app \
apertium

docker exec -it apertium-visualizer bash

```bash
$ # filter languages for drawing directed graphs
$ # dot - filter for drawing directed graphs
$ # neato - filter for drawing undirected graphs
$ # twopi - filter for radial layouts of graphs
$ # circo - filter for circular layout of graphs
$ # fdp - filter for drawing undirected graphs
$ # sfdp - filter for drawing large undirected graphs
$ FILENAME=apertium-tet.tet
$ echo 'seluk:seluk<adj>' | apertium-visualizer FILENAME.dix
$ dot -Tpng FILENAME.gv -o FILENAME.png
```

`apertium-visualizer` will create a `apertium.en.en.gv` graphviz file

using dot you can choose between different format like png, svg, pdf

using this approach we can use the `gv` file to work with web visualizations

