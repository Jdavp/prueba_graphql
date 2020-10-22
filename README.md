# Prueba BackEnd - LQN
Desarrollo de API GraphQL para un sitio web para los fanáticos de Star Wars.

#Tecnologías:

**Python / Django.** <img src="https://img.icons8.com/color/48/000000/python.png"/>

**GraphQl.** <img src="https://img.icons8.com/color/48/000000/graphql.png"/>

**Graphene** 

**Relay** 

**Django Filter**

**La aplicación esta desarrollada en Python y el framework Django permite al usuario
ver un listado de todos los personajes relacionadas con el universo de star wars, cada
personaje permite ver las películas en las que dicho personaje participa, cada película
tiene un detalle donde se muestra un texto apertura, los planetas que se muestran en
cada película, el director y los productores.**


## Instalación : 
* Clona este repositorio: `git clone "https://github.com/Jdavp/.git"`
* Si no tiene python puede instalar acadonda para su OS : https://docs.anaconda.com/anaconda/install/
* pip install -r requeriments.txt
* python characters-script (para general el archivo json starwars data consultando swapi)
* python manage.py makemigrations
* python manage.py migrate
* python manage.py loaddata starwars
* Ejecute index.py: verifique en localhost:8000/graphql

## Queries de Prueba :

*query all characters names

```
query all characters names
{
  allCharacters{
    edges {
      node {
        name
      }
    }
  }
}
query character filter by id
{
  character(id:"Q2hhcmFjdGVyTm9kZTox"){
    name
  }
}
query all characters filter by name can also use name_Icontains:
name_Istartswith:
{
  allCharacters(name:"Sly Moore"){
    edges {
      node {
        id,
        name
      }
    }
  }

query character films
  character(id:"Q2hhcmFjdGVyTm9kZTox"){
    films {
      edges {
        node {
          id
          filmTitle
        }
      }
    }
  }
}

query all plants in film where a character appear
  allCharacters{
   edges{
    node{
      name
      films {
        edges {
          node {
            id
            filmTitle
            planets{
              edges{
                node{
                  name
                	}
              	}
            	}
            }
          }
        }
      }
    }
  }
}

```
*mutation createCharacter

```
mutation {
  createCharacter(name: "nuevo",) {
    name{
      id
    }
  }
}

```
mutation {
  createFilm(filmTitle:"nuevo"){
    filmTitle{
      id
      filmTitle
    }
  }   
}

'''
mutation {
  createPlanet(name:"nuevo"){
    name{
      id
      name
    }
  }   
}

## Autor
Juan Diego Alejandro Valencia Peña - [Github](https://github.com/Jdavp) / [Twitter](https://twitter.com/jdavp)

