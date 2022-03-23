# BahiaRT-GYM
 Ambiente customizado para otimização de agentes do tipo NAO simulados através do RCSSSERVER3D

## Requisitos

 **1. Ubuntu 18.04**
 
 **2. Python 3.7**
 
 **3. OpenAI Gym package**
 
 **4. PyTorch**
 
 **5. Stable-Baselines3**

## Detalhes dos requisitos
 O Stable-Baselines3 requer o uso do Python 3.7+ e do PyTorch >= 1.8.1. Até o momento (16/03/2022) a versão mais atual do PyTorch (1.11.0) não suporta o Python 3.8, portanto o mais recomendado é se manter no Python 3.7

## Instalação do Python 3.7 e criação do venv
 Para instalar o ambiente, recomenda-se o uso de um ambiente virtual do python (venv), para evitar conflito entre bibliotecas presentes no sistema. O tutorial a seguir explica como realizar a instalação utilizando o venv do python 3.7

 1) Adicionar o repositório do python e instalar o 3.7:
   ```bash
   sudo apt update
   sudo apt install software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt install python3.7
   ```
 2) Criar ambiente virtual:
   ```bash
   python3.7 -m venv venv
   ```

   Isso irá criar uma pasta chamada venv no diretorio atual. Caso queira mudar o nome da pasta, altere o segundo "venv".

 3) Entre no ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

   Agora você está no ambiente virtual do python 3.7. Caso queira sair basta usar o comando:
   ```bash
   deactivate
   ```
 4) Atualize o pip dentro do venv.
   ```bash
   pip install --upgrade pip
   ```
A partir de agora, todos os comandos utilizando o pip ou o próprio python, devem ser realizados dentro do ambiente virtual. Assim, quaisquer bibliotecas instaladas não irão conflitar com as do seu sistema.
## Instalando o PyTorch

A instalação do PyTorch vai depender do seu sistema.

Caso você utilize núcleos CUDA, o seguinte comando irá instalar o Torch na versão 1.11.0 com suporte a CUDA 10.2 no linux via PiP:
```bash
   pip install torch torchvision torchaudio
```
Caso faça uso apenas da CPU, o comando para instalar a mesma versão do Torch é o seguinte:
```bash
   pip install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
```
Para outras combinações de versões do Torch, verifique na página oficial: https://pytorch.org/get-started/locally/

## Instalando o Gym e o Stable-Baselines3

Para instalar o gym, utilize o seguinte comando:
```bash
   pip install gym
```
Para instalar o Stable-Baselines3, utilize o seguinte comando:
```bash
   pip install stable-baselines3[extra]
```
A versão [extra] é muito útil pois nos permite utilizar o tensorboard para avaliar os modelos treinados.

## Clonando o ambiente e instalando o BahiaRT-Gym

Para clonar o ambiente, vá para a mesma pasta onde está o seu ambiente virtual e utilize o comando:
```bash
   git clone {repositório público}
```
Assim o diretório deve ficar parecido com esse:
```
   sua-pasta/
    venv/
    bahiart-gym/
```
Agora, dentro da pasta do bahiart-gym, utilize o seguinte comando para instalar o pacote:
```bash
   pip install -e .
```
Agora o pacote do BahiaRT-Gym está instalado em seu ambiente virtual python.

## Testando o ambiente demo do BahiaRT-Gym
No arquivo "demo_test.py" você pode conferir um exemplo de script para realizar o teste do ambiente demo, junto a explicações de cada linha de código. Sinta-se a vontade para explorar e modificar as linhas para diversificar o teste.

## Exemplo de arquitetura de processos

![Arquitetura de Processos](/img/kickEnvSteps.png)