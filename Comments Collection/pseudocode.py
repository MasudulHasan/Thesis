
"""
    We will be collecting comments in this order: Season/Year > Series > Articles

    Starting with 2014 for now.

    * Link 1: view-source:http://www.espncricinfo.com/ci/engine/series/index.html?season=2014;view=season

        Here, the 'season' variable will be changed every time. "2014%2F15" gives season 2014/15, "2015" gives 2015 and so on.

    From Link 1, using Beautiful Soup, we can easily find all < class="teams" > and extract the link of all the ODI series of the year
    under the heading <h2>One-Day Internationals</h2>.

    * Let each of these series links be Link 2.

        While in Link 2, we should be collecting all relevant information like the teams playing, venues, conditions (if possible) etc.

    From Link 2, we can find links to *Articles* of all the matches in the series by searching for the tag containing the term 'Articles'
    in it. If the series had three matches, the search should be returning three results. Then the links can be extracted from there.

    * Let each of these links containing list of articles for one match be Link 3.

    From Link 3, finding all < class = "SpecialsHead" > takes us to all articles. Comments can then be extracted from these links like
    before. It will be useful to get rid of the <p> tags and directly get just the comment texts for further usage.

        While collecting these comments, we should be collecting all relevant information like time of article, number of comments,
        teams involved in this match (if more than two nations in the series) etc.

"""