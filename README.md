<h1 align="center">Turtlebot Gazebo</h1>
<h6 align="center"> Projeto desenvolvido na disciplina de Robótica Móvel</h6>

Este trabalho foi desenvolvido com o objetivo de implementar o controle e detecção de colisão de um robô diferencial.

<h4>ROS, o que é?</h4>
O Robot Operating System (ROS) é uma estrutura flexível para escrever software robô. É uma coleção de ferramentas, bibliotecas e convenções que visam simplificar a tarefa de criar um comportamento robô complexo e robusto em uma ampla variedade de plataformas robóticas.

Porque? Porque criar um software robô verdadeiramente robusto e de uso geral é difícil. Do ponto de vista do robô, problemas que parecem triviais para os humanos muitas vezes variam descontroladamente entre instâncias de tarefas e ambientes. Lidar com essas variações é tão difícil que nenhum indivíduo, laboratório ou instituição pode esperar fazê-lo por conta própria.

[fonte: www.ros.org](https://www.ros.org/about-ros/)

<h4>TurtleBot3</h4>
TurtleBot3 é um pequeno robô móvel, acessível, programável e baseado em ROS para uso em educação, pesquisa, hobby e prototipagem de produtos. O objetivo do TurtleBot3 é reduzir drasticamente o tamanho da plataforma e baixar o preço sem ter que sacrificar sua funcionalidade e qualidade, ao mesmo tempo em que oferece expansão. O TurtleBot3 pode ser personalizado de várias maneiras, dependendo de como você reconstrói as peças mecânicas e usa peças opcionais, como o computador e o sensor. Além disso, o TurtleBot3 é desenvolvido com SBC econômico e de pequeno porte que é adequado para sistema embarcado robusto, sensor de distância de 360 graus e tecnologia de impressão 3D. 

[fonte: turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview)


<h4>Pré-requisitos do sistema:</h4>

- Instalação do ROS 

- Instalação do Turtlebot3

<h4>Instruções de execução do Projeto:</h4>

1. Após realizar o download do repositório execute o seguinte comando para acessar o workspace do projeto: 

```
cd ~/turtlebot-gazebo
```
2. Para configurar o repositório como um workspace, execute o comando:
```
gedit ~/.bashrc
```
4. Um arquivo será aberto, e insira ao final a linha com o caminho para o arquivo setup.bash dentro da pasta devel:
```
source /home/[seu usuário aqui]/turtlebot-gazebo/devel/setup.bash
```
5. Após isso, execute: 
```
source ~/.bashrc
```
6. Em seguida, para rodar o simulador Gazebo e a aplicação para controlar o robô, execute o comando:
```
roslaunch desafio3 controletb3.launch
```
3. E pronto! Para fazer com que o robô se movimente, insira as coordenadas quando solicitado.


<h4 align="center">Tecnologias utilizadas</h4>


<h4>Desenvolvido por:</h4>

[Anderson Rodrigues Pereira](https://github.com/ander5onPereira)

[Guilherme Santos da Silva](https://github.com/guilhermess98)

[Tatiany Keiko Mori](https://github.com/keikomori)
