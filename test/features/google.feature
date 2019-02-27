Feature: Google Search Within Website
 	As a Google user
 	I want to have the ability to prefix my searches with a Website
 	So I can search within a specific domain

  @regression
  Scenario Outline: Searching within domain
        Given I want to find <term> within website <website>
        When I search on Google
        Then the results are returned

        Examples:
            | website          | term             |
            | www.bbc.co.uk    | Harry Kane       |
            | www.costa.co.uk  | beans            |