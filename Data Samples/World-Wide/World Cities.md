# World City Data

This is some helpful data for world cities. It includes the city name, country, continent, area, density, population. This data is useful for mapping and other geospatial applications. It is also useful for data analysis and visualization. The data is in PowerFx named-formula format. 

## Add This to Your Application

```PowerFx
    fxCities = [
        {
            ID: 1,
            City: "Tokyo",
            Country: "Japan",
            Continent: "Asia",
            Area: 6,
            Density: 146,
            Population: 9
        },
        {
            ID: 2,
            City: "Delhi",
            Country: "India",
            Continent: "Asia",
            Area: 15,
            Density: 78,
            Population: 18
        },
        {
            ID: 3,
            City: "Shanghai",
            Country: "China",
            Continent: "Asia",
            Area: 6,
            Density: 38,
            Population: 24
        },
        {
            ID: 4,
            City: "São Paulo",
            Country: "Brazil",
            Continent: "South America",
            Area: 19,
            Density: 79,
            Population: 15
        },
        {
            ID: 5,
            City: "Mumbai",
            Country: "India",
            Continent: "Asia",
            Area: 28,
            Density: 83,
            Population: 21
        },
        {
            ID: 6,
            City: "Beijing",
            Country: "China",
            Continent: "Asia",
            Area: 27,
            Density: 52,
            Population: 14
        },
        {
            ID: 7,
            City: "Cairo",
            Country: "Egypt",
            Continent: "Africa",
            Area: 31,
            Density: 39,
            Population: 12
        },
        {
            ID: 8,
            City: "Dhaka",
            Country: "Bangladesh",
            Continent: "Asia",
            Area: 18,
            Density: 112,
            Population: 20
        },
        {
            ID: 9,
            City: "Mexico City",
            Country: "Mexico",
            Continent: "North America",
            Area: 11,
            Density: 60,
            Population: 8
        },
        {
            ID: 10,
            City: "Osaka",
            Country: "Japan",
            Continent: "Asia",
            Area: 23,
            Density: 86,
            Population: 20
        },
        {
            ID: 11,
            City: "New York City",
            Country: "United States",
            Continent: "North America",
            Area: 8,
            Density: 107,
            Population: 8
        },
        {
            ID: 12,
            City: "Karachi",
            Country: "Pakistan",
            Continent: "Asia",
            Area: 33,
            Density: 64,
            Population: 21
        },
        {
            ID: 13,
            City: "Buenos Aires",
            Country: "Argentina",
            Continent: "South America",
            Area: 20,
            Density: 75,
            Population: 15
        },
        {
            ID: 14,
            City: "Istanbul",
            Country: "Turkey",
            Continent: "Asia",
            Area: 22,
            Density: 65,
            Population: 14
        },
        {
            ID: 15,
            City: "Kolkata",
            Country: "India",
            Continent: "Asia",
            Area: 28,
            Density: 67,
            Population: 19
        },
        {
            ID: 16,
            City: "Manila",
            Country: "Philippines",
            Continent: "Asia",
            Area: 21,
            Density: 95,
            Population: 20
        },
        {
            ID: 17,
            City: "Lagos",
            Country: "Nigeria",
            Continent: "Africa",
            Area: 24,
            Density: 98,
            Population: 23
        },
        {
            ID: 18,
            City: "Rio de Janeiro",
            Country: "Brazil",
            Continent: "South America",
            Area: 22,
            Density: 71,
            Population: 16
        },
        {
            ID: 19,
            City: "Tianjin",
            Country: "China",
            Continent: "Asia",
            Area: 19,
            Density: 78,
            Population: 15
        },
        {
            ID: 20,
            City: "Chicago",
            Country: "United States",
            Continent: "North America",
            Area: 22,
            Density: 75,
            Population: 17
        },
        {
            ID: 21,
            City: "London",
            Country: "United Kingdom",
            Continent: "Europe",
            Area: 16,
            Density: 54,
            Population: 8
        },
        {
            ID: 22,
            City: "Paris",
            Country: "France",
            Continent: "Europe",
            Area: 15,
            Density: 105,
            Population: 16
        },
        {
            ID: 23,
            City: "Bangkok",
            Country: "Thailand",
            Continent: "Asia",
            Area: 14,
            Density: 92,
            Population: 13
        },
        {
            ID: 24,
            City: "Seoul",
            Country: "South Korea",
            Continent: "Asia",
            Area: 6,
            Density: 172,
            Population: 10
        },
        {
            ID: 25,
            City: "Moscow",
            Country: "Russia",
            Continent: "Europe",
            Area: 25,
            Density: 48,
            Population: 12
        },
        {
            ID: 26,
            City: "Shenzhen",
            Country: "China",
            Continent: "Asia",
            Area: 21,
            Density: 91,
            Population: 19
        },
        {
            ID: 27,
            City: "Jakarta",
            Country: "Indonesia",
            Continent: "Asia",
            Area: 23,
            Density: 71,
            Population: 16
        },
        {
            ID: 28,
            City: "Lima",
            Country: "Peru",
            Continent: "South America",
            Area: 19,
            Density: 82,
            Population: 16
        },
        {
            ID: 29,
            City: "Berlin",
            Country: "Germany",
            Continent: "Europe",
            Area: 24,
            Density: 69,
            Population: 17
        },
        {
            ID: 30,
            City: "Toronto",
            Country: "Canada",
            Continent: "North America",
            Area: 20,
            Density: 81,
            Population: 16
        },
        {
            ID: 31,
            City: "Singapore",
            Country: "Singapore",
            Continent: "Asia",
            Area: 17,
            Density: 88,
            Population: 15
        },
        {
            ID: 32,
            City: "Guangzhou",
            Country: "China",
            Continent: "Asia",
            Area: 18,
            Density: 87,
            Population: 16
        },
        {
            ID: 33,
            City: "Los Angeles",
            Country: "United States",
            Continent: "North America",
            Area: 25,
            Density: 68,
            Population: 17
        },
        {
            ID: 34,
            City: "Madrid",
            Country: "Spain",
            Continent: "Europe",
            Area: 16,
            Density: 93,
            Population: 15
        },
        {
            ID: 35,
            City: "Bangalore",
            Country: "India",
            Continent: "Asia",
            Area: 16,
            Density: 85,
            Population: 14
        },
        {
            ID: 36,
            City: "Ho Chi Minh City",
            Country: "Vietnam",
            Continent: "Asia",
            Area: 24,
            Density: 68,
            Population: 16
        },
        {
            ID: 37,
            City: "Sydney",
            Country: "Australia",
            Continent: "Oceania",
            Area: 18,
            Density: 84,
            Population: 15
        },
        {
            ID: 38,
            City: "Santiago",
            Country: "Chile",
            Continent: "South America",
            Area: 20,
            Density: 79,
            Population: 16
        },
        {
            ID: 39,
            City: "Hong Kong",
            Country: "China",
            Continent: "Asia",
            Area: 12,
            Density: 168,
            Population: 20
        },
        {
            ID: 40,
            City: "Riyadh",
            Country: "Saudi Arabia",
            Continent: "Asia",
            Area: 13,
            Density: 82,
            Population: 11
        },
        {
            ID: 41,
            City: "Dallas",
            Country: "United States",
            Continent: "North America",
            Area: 24,
            Density: 70,
            Population: 17
        },
        {
            ID: 42,
            City: "Houston",
            Country: "United States",
            Continent: "North America",
            Area: 22,
            Density: 72,
            Population: 16
        },
        {
            ID: 43,
            City: "Barcelona",
            Country: "Spain",
            Continent: "Europe",
            Area: 20,
            Density: 83,
            Population: 17
        },
        {
            ID: 44,
            City: "Philadelphia",
            Country: "United States",
            Continent: "North America",
            Area: 17,
            Density: 90,
            Population: 15
        },
        {
            ID: 45,
            City: "Johannesburg",
            Country: "South Africa",
            Continent: "Africa",
            Area: 26,
            Density: 58,
            Population: 15
        },
        {
            ID: 46,
            City: "Munich",
            Country: "Germany",
            Continent: "Europe",
            Area: 25,
            Density: 67,
            Population: 17
        },
        {
            ID: 47,
            City: "Milan",
            Country: "Italy",
            Continent: "Europe",
            Area: 18,
            Density: 88,
            Population: 16
        },
        {
            ID: 48,
            City: "Prague",
            Country: "Czech Republic",
            Continent: "Europe",
            Area: 21,
            Density: 77,
            Population: 16
        },
        {
            ID: 49,
            City: "Dubai",
            Country: "United Arab Emirates",
            Continent: "Asia",
            Area: 15,
            Density: 95,
            Population: 14
        },
        {
            ID: 50,
            City: "Melbourne",
            Country: "Australia",
            Continent: "Oceania",
            Area: 21,
            Density: 77,
            Population: 16
        },
        {
            ID: 51,
            City: "Rome",
            Country: "Italy",
            Continent: "Europe",
            Area: 19,
            Density: 82,
            Population: 16
        },
        {
            ID: 52,
            City: "Athens",
            Country: "Greece",
            Continent: "Europe",
            Area: 17,
            Density: 89,
            Population: 15
        },
        {
            ID: 53,
            City: "Amsterdam",
            Country: "Netherlands",
            Continent: "Europe",
            Area: 25,
            Density: 69,
            Population: 17
        },
        {
            ID: 54,
            City: "Bogotá",
            Country: "Colombia",
            Continent: "South America",
            Area: 23,
            Density: 74,
            Population: 17
        },
        {
            ID: 55,
            City: "Vienna",
            Country: "Austria",
            Continent: "Europe",
            Area: 20,
            Density: 82,
            Population: 16
        },
        {
            ID: 56,
            City: "Stockholm",
            Country: "Sweden",
            Continent: "Europe",
            Area: 24,
            Density: 70,
            Population: 17
        },
        {
            ID: 57,
            City: "Copenhagen",
            Country: "Denmark",
            Continent: "Europe",
            Area: 19,
            Density: 84,
            Population: 16
        },
        {
            ID: 58,
            City: "Brussels",
            Country: "Belgium",
            Continent: "Europe",
            Area: 17,
            Density: 87,
            Population: 15
        },
        {
            ID: 59,
            City: "Lisbon",
            Country: "Portugal",
            Continent: "Europe",
            Area: 22,
            Density: 74,
            Population: 16
        },
        {
            ID: 60,
            City: "Dublin",
            Country: "Ireland",
            Continent: "Europe",
            Area: 20,
            Density: 81,
            Population: 16
        },
        {
            ID: 61,
            City: "Warsaw",
            Country: "Poland",
            Continent: "Europe",
            Area: 23,
            Density: 72,
            Population: 17
        },
        {
            ID: 62,
            City: "Helsinki",
            Country: "Finland",
            Continent: "Europe",
            Area: 22,
            Density: 73,
            Population: 16
        },
        {
            ID: 63,
            City: "Oslo",
            Country: "Norway",
            Continent: "Europe",
            Area: 16,
            Density: 91,
            Population: 15
        },
        {
            ID: 64,
            City: "Rotterdam",
            Country: "Netherlands",
            Continent: "Europe",
            Area: 18,
            Density: 83,
            Population: 15
        },
        {
            ID: 65,
            City: "Hamburg",
            Country: "Germany",
            Continent: "Europe",
            Area: 22,
            Density: 75,
            Population: 17
        },
        {
            ID: 66,
            City: "Frankfurt",
            Country: "Germany",
            Continent: "Europe",
            Area: 17,
            Density: 88,
            Population: 15
        },
        {
            ID: 67,
            City: "Zurich",
            Country: "Switzerland",
            Continent: "Europe",
            Area: 20,
            Density: 83,
            Population: 17
        },
        {
            ID: 68,
            City: "Manchester",
            Country: "United Kingdom",
            Continent: "Europe",
            Area: 21,
            Density: 77,
            Population: 16
        },
        {
            ID: 69,
            City: "Birmingham",
            Country: "United Kingdom",
            Continent: "Europe",
            Area: 24,
            Density: 71,
            Population: 17
        },
        {
            ID: 70,
            City: "Glasgow",
            Country: "United Kingdom",
            Continent: "Europe",
            Area: 18,
            Density: 86,
            Population: 15
        },
        {
            ID: 71,
            City: "Naples",
            Country: "Italy",
            Continent: "Europe",
            Area: 21,
            Density: 76,
            Population: 16
        },
        {
            ID: 72,
            City: "Casablanca",
            Country: "Morocco",
            Continent: "Africa",
            Area: 24,
            Density: 82,
            Population: 19
        },
        {
            ID: 73,
            City: "Nairobi",
            Country: "Kenya",
            Continent: "Africa",
            Area: 23,
            Density: 76,
            Population: 17
        },
        {
            ID: 74,
            City: "Addis Ababa",
            Country: "Ethiopia",
            Continent: "Africa",
            Area: 25,
            Density: 71,
            Population: 18
        },
        {
            ID: 75,
            City: "Cape Town",
            Country: "South Africa",
            Continent: "Africa",
            Area: 22,
            Density: 69,
            Population: 15
        },
        {
            ID: 76,
            City: "Auckland",
            Country: "New Zealand",
            Continent: "Oceania",
            Area: 20,
            Density: 74,
            Population: 15
        },
        {
            ID: 77,
            City: "Brisbane",
            Country: "Australia",
            Continent: "Oceania",
            Area: 19,
            Density: 72,
            Population: 14
        },
        {
            ID: 78,
            City: "Perth",
            Country: "Australia",
            Continent: "Oceania",
            Area: 21,
            Density: 68,
            Population: 14
        },
        {
            ID: 79,
            City: "Tehran",
            Country: "Iran",
            Continent: "Asia",
            Area: 17,
            Density: 88,
            Population: 15
        },
        {
            ID: 80,
            City: "Baghdad",
            Country: "Iraq",
            Continent: "Asia",
            Area: 26,
            Density: 56,
            Population: 15
        },
        {
            ID: 81,
            City: "Jeddah",
            Country: "Saudi Arabia",
            Continent: "Asia",
            Area: 23,
            Density: 67,
            Population: 15
        },
        {
            ID: 82,
            City: "Kuwait City",
            Country: "Kuwait",
            Continent: "Asia",
            Area: 16,
            Density: 85,
            Population: 14
        },
        {
            ID: 83,
            City: "Hanoi",
            Country: "Vietnam",
            Continent: "Asia",
            Area: 15,
            Density: 89,
            Population: 13
        },
        {
            ID: 84,
            City: "Kuala Lumpur",
            Country: "Malaysia",
            Continent: "Asia",
            Area: 22,
            Density: 73,
            Population: 16
        },
        {
            ID: 85,
            City: "Taipei",
            Country: "Taiwan",
            Continent: "Asia",
            Area: 30,
            Density: 61,
            Population: 18
        },
        {
            ID: 86,
            City: "Almaty",
            Country: "Kazakhstan",
            Continent: "Asia",
            Area: 19,
            Density: 70,
            Population: 13
        },
        {
            ID: 87,
            City: "Seattle",
            Country: "United States",
            Continent: "North America",
            Area: 19,
            Density: 84,
            Population: 16
        },
        {
            ID: 88,
            City: "Montreal",
            Country: "Canada",
            Continent: "North America",
            Area: 20,
            Density: 81,
            Population: 16
        },
        {
            ID: 89,
            City: "Vancouver",
            Country: "Canada",
            Continent: "North America",
            Area: 23,
            Density: 73,
            Population: 17
        },
        {
            ID: 90,
            City: "Phoenix",
            Country: "United States",
            Continent: "North America",
            Area: 16,
            Density: 91,
            Population: 15
        },
        {
            ID: 91,
            City: "Guadalajara",
            Country: "Mexico",
            Continent: "North America",
            Area: 18,
            Density: 82,
            Population: 15
        },
        {
            ID: 92,
            City: "Monterrey",
            Country: "Mexico",
            Continent: "North America",
            Area: 21,
            Density: 75,
            Population: 16
        },
        {
            ID: 93,
            City: "Caracas",
            Country: "Venezuela",
            Continent: "South America",
            Area: 20,
            Density: 78,
            Population: 16
        },
        {
            ID: 94,
            City: "Quito",
            Country: "Ecuador",
            Continent: "South America",
            Area: 19,
            Density: 73,
            Population: 14
        },
        {
            ID: 95,
            City: "Montevideo",
            Country: "Uruguay",
            Continent: "South America",
            Area: 17,
            Density: 71,
            Population: 13
        },
        {
            ID: 96,
            City: "Asunción",
            Country: "Paraguay",
            Continent: "South America",
            Area: 16,
            Density: 69,
            Population: 11
        },
        {
            ID: 97,
            City: "La Paz",
            Country: "Bolivia",
            Continent: "South America",
            Area: 18,
            Density: 67,
            Population: 12
        },
        {
            ID: 98,
            City: "San Salvador",
            Country: "El Salvador",
            Continent: "North America",
            Area: 14,
            Density: 86,
            Population: 12
        },
        {
            ID: 99,
            City: "Panama City",
            Country: "Panama",
            Continent: "North America",
            Area: 16,
            Density: 82,
            Population: 13
        },
        {
            ID: 100,
            City: "San José",
            Country: "Costa Rica",
            Continent: "North America",
            Area: 15,
            Density: 79,
            Population: 12
        }
    ];
```

## Free Community & Course Materials
🆓 Get access to our free Power Apps crash course (and our community) here: 
- https://tinyurl.com/DarrensStuffFree 🔗

## Support

I hope you have found this helpful. If you need any help with the Power Platform, don't hesitate to email us at 
* [support@superpowerlabs.co](support@superpowerlabs.co).
* https://powerplatformlinks.com 

## Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
