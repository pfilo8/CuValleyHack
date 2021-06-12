# Górnicy Carla Friedricha Team
> CuValleyHack - stabilizacja pracy pieca zawiesiniowego.

## Spis treści
* [Informacje ogóle](#general-info)
* [Nasze rozwiązanie](#our-solution)
* [ControlRoom - symulacje działania](#controlRoom)
* [Contact](#contact)

## Informacje ogóle

![Hackathon](imges/hackathon.jpeg)

> Piec zawiesinowy to serce huty miedzi, które napędza jej działanie. 
Serce to jest niezwykle gorące, dlatego poziom odbioru ciepła w szybie reakcyjnym musi być stale monitorowany oraz stabilizowany. 

**Cel:** Stwórz model empiryczny, który wesprze stabilizację poziomu ciepła w szybie reakcyjnym i usprawni produktywną pracę pieca.

## Nasze rozwiązanie


## ControlRoom - symulacje działania

Poza samym mechanizmem sterowania parametrami manipulacyjnymi wystawionym w postaci RESTapi, przygotowaliśmy również symulator który odpytuje w czasie rzeczywistym nasz algorytm korzystając z danych historycznych. Wyniki przedstawiane przez symulator działania pozwalają ocenić słuszność decyzji podejmowanych przez mechanizm sterujący oraz czas potrzebny na uzyskanie odpowiedzi. Zarówno główna aplikacja, jak i sam symulator, zostały przygotowane wraz z plikami umożliwiającymi ich łatwe uruchomienie. Wykonaj poniższe kroki, aby zobaczyć działanie symulatora na własne oczy!

Uwaga! Poniższa instrukcja zawiera komendy do wpisania w terminalu. Upewnij się również, że na swojej maszynie posiadasz zainstalowanego
dockera oraz docker-compose. Jeśli nie miałeś/aś jeszcze okazji korzystać to [tutaj](https://docs.docker.com/compose/install/) instrukcja instalacji ;) 

1. Uruchomienie mechanizmu sterującego:
 - cd CuValleyHack/app
 - sudo docker-compose up
2. Uruchomienie ControlRoom'u (rozpoczęcie symulacji):
 - cd CuValleyHack/simulator (w nowym terminalu)
 - sudo docker-compose up

Teraz czas otworzyć paczę popcorn'u i cieszyć się przewijającymi się przez Twój ekran wynikami symulacji! :D 

Skoro już udało nam się uruchomić nasz mechanizm sterujący to wykorzystamy go żeby pokazać jak działa RESTapi od podszewki i w jaki sposób można użyć go poza symulatorem. Nasz konterer posiada wystawiony port na "0.0.0.0:1234", natomiast interesującą nas funkcje znajdziemy pod nazwą getNewParams/. Pozostaje nam podać parametry z sensorów w danym momencie w czasie. Jest ich łącznie 27 i dla uproszeczenia nazwiemy je zmienna0,...,zmienna26. Korzystając z przeglądarki możemy wyslać zapytanie typu GET do naszego mechanizmu sterującego. Wystarczy w tym celu wkleić poniższy adres URL do przeglądarki

http://0.0.0.0:1234/getNewParams/?zmienna0=2021-04-19%2000:00:00&zmienna1=1&zmienna2=2&zmienna3=3&zmienna4=4&zmienna5=5&zmienna6=6&zmienna7=7&zmienna8=8&zmienna9=9&zmienna10=10&zmienna11=22&zmienna12=22&zmienna13=22&zmienna14=22&zmienna15=22&zmienna16=22&zmienna17=22&zmienna18=22&zmienna19=22&zmienna20=22&zmienna21=22&zmienna22=22&zmienna23=22&zmienna24=22&zmienna25=22&zmienna26=22

W odpowiedzi dostaliśmy wartości zmian parametrów manipulowalnych jakie powinniśmy wprowadzić. 


## Contact
Created by [Jakub Galik](https://www.linkedin.com/in/jakub-galik-467b6b136/), [Łukasz Łaszczuk](https://www.linkedin.com/in/%C5%82ukasz-%C5%82aszczuk-141361187/), [Robert Benke](https://www.linkedin.com/in/robert-benke-396b56175/) i [Patryk Wielopolski](https://www.linkedin.com/in/patryk-wielopolski/) - masz pytania? Napisz! ;) 
