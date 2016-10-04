import urllib
import urllib.request
from http.cookiejar import CookieJar

# from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup
import re
import datetime


def content(theurl,label):
    #theurl = a
    thepage = urllib.request.urlopen(theurl).read()
    # print(thepage)
    soup = BeautifulSoup(thepage, "html.parser")
    input = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- hostname: wci031, country: bd, cluster: bd, created: 2016-08-12 15:11:05 -->
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://developers.facebook.com/schema/" >
<head>
 <script type="text/javascript">var _sf_startpt=(new Date()).getTime()</script>
 <meta name="google-site-verification" content="ZxdgH3XglRg0Bsy-Ho2RnO3EE4nRs53FloLS6fkt_nc" />
 <title>Cricket  | Only ODI: Scotland v England at Aberdeen, May 9, 2014 Cricket | ESPN Cricinfo</title>
 <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
 <meta name="keywords" content="" />

 <meta name="description" content="" />
<!--[if IE 9]>
<script language="javascript" type="text/javascript">
function fnCreateJumpList(iScenario) {
fnClearJumpList();
window.external.msSiteModeCreateJumpList("Quick Links")
window.external.msSiteModeShowJumpList();
}
function fnClearJumpList() {
window.external.msSiteModeClearJumplist();
}
</script>

<meta name="msapplication-task" content="name=Live Scores;action-uri=http://www.espncricinfo.com/ci/engine/current/match/scores/live.html;icon-uri=/favicon.ico"/>
<meta name="msapplication-task" content="name=Latest News;action-uri=http://www.espncricinfo.com/ci/content/current/story/news.html;icon-uri=/favicon.ico"/>
<meta name="msapplication-task" content="name=Fixtures;action-uri=http://www.espncricinfo.com/ci/content/current/match/fixtures/index.html;icon-uri=/favicon.ico"/>
<meta name="msapplication-task" content="name=Results;action-uri=http://www.espncricinfo.com/ci/engine/current/match/scores/recent.html;icon-uri=/favicon.ico"/>
<meta name="msapplication-task" content="name=Photos;action-uri=http://www.espncricinfo.com/ci/content/current/image/index.html;icon-uri=/favicon.ico"/>
<meta name="msapplication-task" content="name=Audio/Video;action-uri=http://www.espncricinfo.com/ci/content/video_audio/index.html;icon-uri=/favicon.ico"/>
<script language="javascript" type="text/javascript">
        fnCreateJumpList(2);
</script>
<![endif]-->


 <meta name="robots" content="index, follow" />
 <meta name="googlebot" content="index, follow" />
 <meta property="og:type" content="article"/>
 <meta property="og:title" content=""/>

 <link rel="shortcut icon" href="/favicon.ie9new.ico" />
 <link rel="icon" type="image/png" href="/favicon.png" />
 <link rel="icon" type="image/gif" href="/favicon.gif" />

 <link rel="apple-touch-icon" href="http://i.imgci.com/espncricinfo/ci_apple_webclip.png"/>
<meta property="fb:app_id" content="260890547115" />
<meta property="og:site_name" content="Cricinfo" />

<!-- Cricinfo Global News RSS feed link -->
<link href="/rss/content/story/feeds/0.xml" rel="alternate" type="application/rss+xml" title="Global News RSS Feed" />
<link href="/rss/livescores.xml" rel="alternate" type="application/rss+xml" title="Cricinfo live scores RSS feed" />

<link rel="stylesheet" type="text/css" href="/navigation/cricinfo/ci/global.css?1462365844"/>

<script language="javascript" type="text/javascript">
	if(navigator.userAgent.indexOf('Linux') != -1) {
		var linux = '/navigation/cricinfo/ci/global_linux.css?1359981014';
		var linuxcss=document.createElement("link");
		linuxcss.setAttribute("rel", "stylesheet");
		linuxcss.setAttribute("type", "text/css");
		linuxcss.setAttribute("href", linux);
		document.getElementsByTagName("head")[0].appendChild(linuxcss);
	}
</script>

 <script language="javascript" type="text/javascript" src="/navigation/cricinfo/ci/jquery-1.7.2.min.js"></script>
 <script language="javascript" type="text/javascript" src="/navigation/cricinfo/ci/default.js?1444812066"></script>

<script src="http://a.espncdn.com/combiner/c?js=jquery-1.7.1.js,plugins/jquery.metadata.js,plugins/jquery.pubsub.r5.js,plugins/ba-debug-0.4.js,espn.l10n.r12.js,espn.core.duo.r55.js,espn.storage.r6.js,espn.p13n.r16.js,espn.geo.r2.js"></script>
<script src="/navigation/cricinfo/ci/video/js/min/espni.video-0.0.3.min.js?1421654561"></script>


<script language="javascript"  type="text/javascript">
	if (typeof $ === 'undefined'){
		var $ = jQuery;
	}
	ord=Math.random()*10000000000000000;
	var ad_counter = 1;

	cqanswer = 'bd';
	location_country = 'bd';
	location_cluster = 'bd';
</script>

<script src="/navigation/cricinfo/ci/assets/js/plugins/jquery.cookie-1.4.1.js"></script>

<style type="text/css">
.video-play-button{background: url(http://img.cricinfo.com/espncricinfo/video/play-icon.png) no-repeat center center;bottom: 0px;left: 0px;position: absolute;right: 0px;text-shadow: none;top: 0px;width: 100%;background-size: 50px auto;opacity: .6;color: transparent;cursor:pointer;}
.video-play-button:hover{opacity: 1;}
</style>

<meta name="application-name" content="ESPNcricinfo"/>
<meta name="msapplication-TileColor" content="#266ab4"/>
<meta name="msapplication-TileImage" content="http://i.imgci.com/espncricinfo/6b245241-3938-499c-8c79-9b80f97bed96.png"/>


<!-- Load GPT JavaScript library used by DFP -->
<script type="text/javascript">
  var googletag = googletag || {};
  googletag.cmd = googletag.cmd || [];
  (function() {
    var gads = document.createElement("script");
    gads.async = true;
    gads.type = "text/javascript";
    var useSSL = "https:" == document.location.protocol;
    gads.src = (useSSL ? "https:" : "http:") + "//www.googletagservices.com/tag/js/gpt.js";
    var node =document.getElementsByTagName("script")[0];
    node.parentNode.insertBefore(gads, node);
   })();
</script>
<script type="text/javascript" src="http://a.espncdn.com/combiner/c?js=swfobject/2.2/swfobject.js?minify=false"></script>


<style>
.espni-ad-slot{line-height: 0;}
pre.gpt-debug{padding: 10px; background: burlywood;}
</style>

  <script type='text/javascript'> var ad_setting = {"adtar":"","kvbrand":"ci","kvcluster":"bd","kvnavtype":"","kvpt":"index","kvsite":"","networkid":"6444","path":"/6444/espn.cricinfo.com/others","sp":"cricinfo","template":"desktop","template_type":"non_responsive"}; var __GPTenabled = true; </script>


</head>
<body

 id="cric_old_template" >






<div id="ciMainContainer">



 <div id="ciHomeMastContainer">


	<div id="ciHomeLeaderboard">
		<div class="bnrHldr" style="margin-bottom:8px;float:none;width:980px;" align="center">
<div class="espni-ad-slot ad-banner" data-slot-type="banner" data-kvpos="top"></div>
		</div>
	</div>
<div id="ciHomeLogoholder">
    <div style="position:relative;width:375px;float:left;margin-bottom:-5px; z-index: 100000;">
        <a style="background:none;" id="link" href="/" title="ESPN Cricinfo"><img src="http://i.imgci.com/espncricinfo/espncricinfologo.png" width="260px" height="35px" /></a>
        <span style="display: block; width: 85px; height:20px; position: absolute; left:270px; top:24px; z-index: 999999; overflow: hidden;">
          <fb:like href="http://www.facebook.com/Cricinfo" send="false" layout="button_count" width="450" show_faces="false" font="tahoma" style="position:absolute; top:0; left:0; width:85px; overflow: hidden;"></fb:like>
        </span>
    </div>
    <div class="ciMemebermgmt" id="ciMemebermgmt">
        <ul style="display:inline-block; width:300px;">
          <li class="espni-edit-profile" style="color:#0D82E9; font-size:11px; padding-bottom:5px; padding-bottom:5px; margin:0;">Welcome Guest </li>
          <li class="signin" style="float:left"><a href="javascript:void(0);" class="signintxt espni-profile-signin">Sign In</a>&nbsp;&nbsp;&nbsp;<span>|</span></li>
          <li class="signin" style="float:left"><a href="javascript:void(0);" class="signintxt espni-profile-register">Register</a></li>
          <li class="signin" style="float:left"><a href="javascript:void(0);" class="signintxt espni-profile-signout">Sign Out</a></li>
        </ul>
    </div>
    <div class="ciGlobalSearch">
        <form method="get" enctype="application/x-www-form-urlencoded" action="/ci/content/site/search.html" onSubmit="return  validateData()" ;>
            <div class="ciGblSearchhldr">
                <input class="glbSearchBox" name="search" id="cricinfoSearch" type="text" value="Search" onfocus="return searchClrTxt('cricinfoSearch');" onblur="if (jQuery(this).val()=='' ){jQuery(this).attr('value','Search');}" />
                <input type="submit" name="gblsearch" class="gblSearchBtn" value="" />
            </div>
        </form>
                <!-- <div class="ciGblHotSearch"> -->
            <!-- <span class="HotsearchHead">Popular:</span> -->
            <!-- <a style="display: block;text-align: right;margin-top: 4px;" href="/ci/content/player/most_wanted.html">
                <img src="http://i.imgci.com/espncricinfo/most_wanted_players.png" alt="Most wanted players" title="Most wanted players" /></a> -->
                    <!-- </div> -->

        <!-- Search box ends -->
    </div>
    <!-- Logo and Search ends -->
</div>
<style type="text/css">
    #ciMemebermgmt{display: none;}
</style>
 </div>
<style>
/* CSSTerm.com Simple Horizontal DropDown CSS menu */
.ci_main_menu{
	width:100%;
	float:left;
	margin-bottom:10px;
}
.ci_drop_menu {
	background:#fff;
	padding:0;
	margin:0;
	list-style-type:none;
	height: 25px;
	display:table;
	width:100%;
	border-top: 1px solid #ccc;
	border-right:1px solid #ccc;
}
.ci_drop_menu  .home{
	padding:0;
	width: 25px;
	height: 28px;
	cursor:pointer;
	background: #0066CA;
}
.ci_drop_menu  .home a{
	background: url('http://i.imgci.com/espncricinfo/ci_home_icon.jpg') no-repeat #0066CA;
	width: 25px;
	height:20px;
	padding: 0px;
	display:block;
	overflow: hidden;
	text-indent: 100%;
	white-space:nowrap;
	text-decoration:none;
}
.ci_drop_menu .home:hover{
background: url('http://i.imgci.com/espncricinfo/ci_home_icon.jpg') no-repeat #0066CA;
opacity:0.9;
}
.ci_drop_menu .home a:hover{
background: url('http://i.imgci.com/espncricinfo/ci_home_icon.jpg') no-repeat;
}
.ci_drop_menu .home a:hover{
padding:0;
}

.ci_drop_menu li { display:table-cell;border-right:1px solid #ccc;background:#fff;border-bottom:1px solid #ccc;}

.ci_drop_menu li:last-child {border-right:0px; }
.ci_drop_menu li:last-child:hover ul li a, .ci_drop_menu li:nth-last-child(2):hover ul li a{text-align:right; }
.ci_drop_menu li:last-child:hover .subnav_content,.ci_drop_menu li:nth-last-child(2):hover .subnav_content{right: -1px;left: auto;padding: 5px 0 10px 20px;}
.ci_drop_menu li:last-child:hover .subnav, .ci_drop_menu li:nth-last-child(2):hover .subnav{width:100%;}
.ci_drop_menu li:last-child:hover .subnav li a, .ci_drop_menu li:nth-last-child(2):hover .subnav li a{margin-right: 10px;margin-left:0;}
.ci_drop_menu li a {
		padding: 6px 10px 3px 10px;
		display: block;
		color: #035bac;
		text-decoration: none;
		font: bold 12px Tahoma, Arial, Verdana, sans-serif;
		text-align: center;
}

.ci_drop_menu li a:hover {
		text-decoration:underline;
		background:#fff;
}

/* Submenu */
.subnav_content{
	position:absolute;
	top:29px;
	width:auto;
	background:#fff;
	border-left: 1px solid #ccc;
	border-right: 1px solid #ccc;
}
.subnav_content li{
	display:inline;
}
.ci_drop_menu ul {
	position:relative;
	display:none;
	list-style-type:none;
	z-index:99999;
}
.subnav{
	display:none;
	width:auto;
	float:left;
	background:#fff !important;
	float:left;
	border-right:1px dotted #ccc;
	background:#fff;
}
.subnav li a{
	text-align:left;
}
.ci_drop_menu .sub_drop:hover .subnav_content{
	display:table;
	z-index: 99999;
	border-bottom: 1px solid #ccc;
	box-shadow: 1px 2px 3px #ccc;
	left: -1px;
	padding: 5px 5px 12px 0;
}
.ci_drop_menu .sub_drop:hover .subnav_wrap{
	display:table-row;
}
.ci_drop_menu .sub_drop:hover .subnav{
	display:table-cell;
}
.ci_drop_menu .sub_drop .subnav li{
	width:auto;
	white-space:nowrap;
	background:#fff;
}
.ci_drop_menu li:hover { position:relative;background:#fff;border-bottom:none;}
.ci_drop_menu li:hover ul {
	left:0px;
	background:#fff;
	padding:0px;
}

.ci_drop_menu li:hover ul li a {
	display:block;
	margin-left:10px;
	background-color:#fff;
	color:#666;
	font-size:11px;
	font-weight:normal;
}
.ci_drop_menu li:hover ul li a:hover { background:#fff;font-weight:bold; }
.two-column{
	width:270px !important;
}
.three-column{
	width:340px !important;
}
.four-column{
	width:496px !important;
}
.ci_drop_menu .subnav li{
	border:none;
}
.subnav:last-child{
	border-right:0;
 }
</style>



<div class="ci_main_menu">
	<ul class="ci_drop_menu">
		<li class="home">
			<a href='/'></a>
		</li>

		<li class="sub_drop">
			<a href="/ci/engine/match/index.html?view=live" name="&lpos=cricinfo_mainnav&lid=livescores">Live Scores</a>

			<div class="subnav_content">
			<div class="subnav_wrap">
				<ul class="subnav">

					<li><a href="/ci/engine/match/index.html?view=live"  name="&lpos=cricinfo_mainnav&lid=livescoreshome">Live Scores Home</a></li>

					<li><a href="/ci/engine/match/index.html?view=week"  name="&lpos=cricinfo_mainnav&lid=matchesbyweek">Matches by week</a></li>

					<li><a href="/ci/engine/series/index.html?view=month"  name="&lpos=cricinfo_mainnav&lid=matchesbymonth">Matches by month</a></li>

					<li><a href="/ci/engine/series/index.html?view=season"  name="&lpos=cricinfo_mainnav&lid=matchesbyseason">Matches by season</a></li>

					<li><a href="/ci/engine/series/index.html"  name="&lpos=cricinfo_mainnav&lid=matchseriesarchive">Match series archive</a></li>

					<li><a href="/ci/content/match/fixtures_futures.html"  name="&lpos=cricinfo_mainnav&lid=currentandfuturetours">Current and Future tours</a></li>

					<li><a href="/ci/engine/match/index.html?view=calendar"  name="&lpos=cricinfo_mainnav&lid=upcominginternationalmatches">Upcoming international matches</a></li>

					<li><a href="javascript:openS('/ci/engine/match/scores/desktop.html','dsktpScrBrd')"  name="&lpos=cricinfo_mainnav&lid=desktopscoreboard">Desktop Scoreboard</a></li>

				</ul>
			</div>
			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/match/fixtures_futures.html" name="&lpos=cricinfo_mainnav&lid=series">Series</a>

			<div class="subnav_content">
			<div class="subnav_wrap">
				<ul class="subnav">

					<li><a href="/england-v-pakistan-2016/content/series/913583.html"  name="&lpos=cricinfo_mainnav&lid=englandvpakistan">England v Pakistan</a></li>

					<li><a href="/west-indies-v-india-2016/content/series/1018687.html"  name="&lpos=cricinfo_mainnav&lid=westindiesvindia">West Indies v India</a></li>

					<li><a href="/sri-lanka-v-australia-2016/content/series/995431.html"  name="&lpos=cricinfo_mainnav&lid=srilankavaustralia">Sri Lanka v Australia</a></li>

					<li><a href="/zimbabwe-v-new-zealand-2016/content/series/1024039.html"  name="&lpos=cricinfo_mainnav&lid=zimbabwevnewzealand">Zimbabwe v New Zealand</a></li>

					<li><a href="/south-africa-v-new-zealand-2016/content/series/936105.html"  name="&lpos=cricinfo_mainnav&lid=southafricavnewzealand">South Africa v New Zealand</a></li>

					<li><a href="/caribbean-premier-league-2016/content/series/971665.html"  name="&lpos=cricinfo_mainnav&lid=caribbeanpremierleague">Caribbean Premier League</a></li>

					<li><a href="/county-cricket-2016/content/series/928261.html"  name="&lpos=cricinfo_mainnav&lid=countycricket2016">County Cricket 2016</a></li>

					<li><a href="/ci/content/match/fixtures_futures.html"  name="&lpos=cricinfo_mainnav&lid=morecurrentandfutureseries">More current and future series</a></li>

					<li><a href="/icc-intercontinental-cup-2015-17/content/series/870857.html"  name="&lpos=cricinfo_mainnav&lid=iccintercontinentalcup">ICC Intercontinental Cup</a></li>

				</ul>
			</div>
			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/site/cricket_squads_teams/index.html" name="&lpos=cricinfo_mainnav&lid=countries">Countries</a>

			<div class="subnav_content three-column">

				<ul class="subnav">

					<li><a href='/australia/content/team/2.html'>Australia</a></li>

					<li><a href='/bangladesh/content/team/25.html'>Bangladesh</a></li>

					<li><a href='/england/content/team/1.html'>England</a></li>

					<li><a href='/india/content/team/6.html'>India</a></li>

					<li><a href='/newzealand/content/team/5.html'>New Zealand</a></li>

					<li><a href='/pakistan/content/team/7.html'>Pakistan</a></li>

					<li><a href='/southafrica/content/team/3.html'>South Africa</a></li>

					<li><a href='/srilanka/content/team/8.html'>Sri Lanka</a></li>

					<li><a href='/westindies/content/team/4.html'>West Indies</a></li>

					<li><a href='/zimbabwe/content/team/9.html'>Zimbabwe</a></li>

				</ul>

				<ul class="subnav">

					<li><a href='/afghanistan/content/team/40.html'>Afghanistan</a></li>

					<li><a href='/hkg/content/team/19.html'>Hong Kong</a></li>

					<li><a href='/ireland/content/team/29.html'>Ireland</a></li>

					<li><a href='/png/content/team/20.html'>PNG</a></li>

					<li><a href='/scotland/content/team/30.html'>Scotland</a></li>

					<li><a href='/uae/content/team/27.html'>UAE</a></li>

				</ul>

				<ul class="subnav">

					<li><a href='/other/content/site/207463.html'>Other Countries</a></li>

					<li><a href='/women/content/site/207455.html'>Women's Cricket</a></li>

					<li><a href='/ci-icc/content/site/297120.html'>ICC</a></li>

					<li><a href='/canada/content/team/17.html'>Canada</a></li>

					<li><a href='/kenya/content/team/26.html'>Kenya</a></li>

					<li><a href='/netherlands/content/team/15.html'>Netherlands</a></li>

					<li><a href='/nepal/content/team/33.html'>Nepal</a></li>

					<li><a href='/oman/content/team/37.html'>Oman</a></li>

					<li><a href='/usa/content/team/11.html'>USA</a></li>

				</ul>

			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/story/news.html" name="&lpos=cricinfo_mainnav&lid=news">News</a>

			<div class="subnav_content ">

				<ul class="subnav">

					<li><a href='/ci/content/story/news.html'>News Home</a></li>

					<li><a href='/blogs/content/story/blogs?genre=454'>The Buzz</a></li>

					<li><a href='/ci/content/url/643069.html'>The Surfer</a></li>

					<li><a href='/infocus/content/story/infocus.html'>In Focus</a></li>

				</ul>

			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/story/features.html" name="&lpos=cricinfo_mainnav&lid=features">Features</a>

			<div class="subnav_content four-column">

				<ul class="subnav">
<li style="padding: 0px 10px 3px 20px; font-weight: bold;">Writers</li>
					<li><a href='/ci/content/story/author.html?author=31'>Sambit Bal</a></li>

					<li><a href='/ci/content/story/author.html?author=589'>Simon Barnes</a></li>

					<li><a href='/ci/content/story/author.html?author=367'>Daniel Brettig</a></li>

					<li><a href='/ci/content/story/author.html?author=261'>Ian Chappell</a></li>

					<li><a href='/ci/content/story/author.html?author=276'>Aakash Chopra</a></li>

					<li><a href='/ci/content/story/author.html?author=268'>Brydon Coverdale</a></li>

					<li><a href='/ci/content/story/author.html?author=116'>George Dobell</a></li>

					<li><a href='/ci/content/story/author.html?author=383'>David Hopps</a></li>

					<li><a href='/ci/content/story/author.html?author=329'>Jarrod Kimber</a></li>

				</ul>

				<ul class="subnav">

					<li><a href='/ci/content/story/author.html?author=375'>Ashley Mallett</a></li>

					<li><a href='/ci/content/story/author.html?author=9'>Andrew Miller</a></li>

					<li><a href='/ci/content/story/author.html?author=272'>Sidharth Monga</a></li>

					<li><a href='/ci/content/story/author.html?author=315'>Firdose Moonda</a></li>

					<li><a href='/ci/content/story/author.html?author=384'>Mark Nicholas</a></li>

					<li><a href='/ci/content/story/author.html?author=380'>Ed Smith</a></li>

					<li><a href='/ci/content/story/author.html?author=291'>Rob Steen</a></li>

					<li><a href='/ci/content/story/author.html?author=355'>Sharda Ugra</a></li>

					<li><a href='/ci/content/story/author.html?author=311'>Andy Zaltzman</a></li>

					<li><a href='/ci/content/story/genre.html?genre=256'>Guest Column</a></li>

				</ul>

				<ul class="subnav">
<li style="padding: 0px 10px 3px 20px; font-weight: bold;">Sections</li>
					<li><a href='/ci/content/story/genre.html?genre=6'>Ask Steven</a></li>

					<li><a href='/ci/content/story/genre.html?genre=268'>Diaries</a></li>

					<li><a href='/ci/content/story/genre.html?genre=169'>Features</a></li>

					<li><a href='/ci/content/story/genre.html?genre=174'>Gleanings</a></li>

					<li><a href='/ci/content/story/genre.html?genre=188'>I Was There</a></li>

					<li><a href='/ci/content/story/genre.html?genre=175'>Interviews</a></li>

					<li><a href='/magazine/content/story/magazine/otd.html'>On This Day</a></li>

				</ul>

				<ul class="subnav">

					<li><a href='/ci/content/story/genre.html?genre=176'>Profiles</a></li>

					<li><a href='/ci/content/story/genre.html?genre=12'>Numbers Game</a></li>

					<li><a href='/ci/content/story/genre.html?genre=340'>Quick Singles</a></li>

					<li><a href='/magazine/content/quote/index.html'>Quote Unquote</a></li>

					<li><a href='/ci/content/story/genre.html?genre=21'>Reviews</a></li>

					<li><a href='/ci/content/story/genre.html?genre=173'>Talking Cricket</a></li>

					<li><a href='/thestands/content/site/thestands'><b>The Stands</b></a></li>

					<li><a href='/ci/content/story/editors_pick.html'><b>EDITOR'S PICKS</b></a></li>

				</ul>

			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/video_audio/index.html" name="&lpos=cricinfo_mainnav&lid=videos">Videos</a>

			<div class="subnav_content two-column">

				<ul class="subnav">

					<li><a href='/ci/content/video_audio/index.html'>Videos Home</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=155'>Match Day</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=46'>Features</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=9'>Interviews</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=129'>Let's Talk About</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=1'>Match Analysis</a></li>

					<li><a href='/ci/content/video_audio/modern_masters/index.html'>Modern Masters</a></li>

				</ul>

				<ul class="subnav">

					<li><a href='/ci/content/video_audio/index.html?genre=53'>My XI</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=34'>News and Analysis</a></li>

					<li><a href='/ci/content/story/genre.html?genre=668'>Numbers Don't Lie</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=119'>Polite Enquiries</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=2'>Press Conference</a></li>

					<li><a href='/ci/content/video_audio/index.html?genre=27'>Switch Hit</a></li>

					<li><a href='http://www.youtube.com/ESPNCricinfo'>YouTube</a></li>

				</ul>

			</div>

		</li>

		<li class="sub_drop">
			<a href="/blogs/content/story/blogs/cordon.html" name="&lpos=cricinfo_mainnav&lid=blogs">Blogs</a>

			<div class="subnav_content">
			<div class="subnav_wrap">
				<ul class="subnav">

					<li><a href="/blogs/content/story/blogs/cordon.html"  name="&lpos=cricinfo_mainnav&lid=thecordon">The Cordon</a></li>

					<li><a href="/blogs/content/story/blogs?genre=457"  name="&lpos=cricinfo_mainnav&lid=theconfectionerystall">The Confectionery Stall</a></li>

					<li><a href="/thestands/content/site/thestands/genre.html?genre=451"  name="&lpos=cricinfo_mainnav&lid=inbox">Inbox</a></li>

					<li><a href="/blogs/content/story/blogs?genre=463"  name="&lpos=cricinfo_mainnav&lid=shotselection">Shot Selection</a></li>

					<li><a href="/blogs/content/story/blogs?genre=427"  name="&lpos=cricinfo_mainnav&lid=tourdiaries">Tour Diaries</a></li>

				</ul>
			</div>
			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/image/index.html" name="&lpos=cricinfo_mainnav&lid=photos">Photos</a>

			<div class="subnav_content">
			<div class="subnav_wrap">
				<ul class="subnav">

					<li><a href="/ci/content/image/index.html"  name="&lpos=cricinfo_mainnav&lid=photoshome">Photos Home</a></li>

					<li><a href="/ci/content/gallery/index.html"  name="&lpos=cricinfo_mainnav&lid=galleries">Galleries</a></li>

				</ul>
			</div>
			</div>

		</li>

		<li class="sub_drop">
			<a href="/ci/content/stats/index.html" name="&lpos=cricinfo_mainnav&lid=stats">Stats</a>

			<div class="subnav_content">
			<div class="subnav_wrap">
				<ul class="subnav">

					<li><a href="/ci/content/stats/index.html"  name="&lpos=cricinfo_mainnav&lid=statshome">Stats home</a></li>

					<li><a href="/ci/engine/stats/index.html"  name="&lpos=cricinfo_mainnav&lid=statsguru">Statsguru</a></li>

					<li><a href="/ci/engine/records/index.html?id=2016;type=year"  name="&lpos=cricinfo_mainnav&lid=2016records">2016 records</a></li>

					<li><a href="/ci/engine/records/index.html?id=2015;type=year"  name="&lpos=cricinfo_mainnav&lid=2015records">2015 records</a></li>

					<li><a href="/ci/engine/records/index.html"  name="&lpos=cricinfo_mainnav&lid=allrecords">All records</a></li>

					<li><a href="/ci/engine/series/index.html"  name="&lpos=cricinfo_mainnav&lid=matchandseriesarchive">Match and series archive</a></li>

					<li><a href="/ci/content/player/index.html"  name="&lpos=cricinfo_mainnav&lid=players">Players</a></li>

					<li><a href="/ci/content/ground/index.html"  name="&lpos=cricinfo_mainnav&lid=grounds">Grounds</a></li>

					<li><a href="/rankings/content/page/211271.html"  name="&lpos=cricinfo_mainnav&lid=teamrankings/playerrankings">Team Rankings / Player Rankings</a></li>

					<li><a href="/ci/content/story/genre.html?genre=668"  name="&lpos=cricinfo_mainnav&lid=numbersdon'tlie">Numbers Don't Lie</a></li>

					<li><a href="http://www.espncricinfo.com/wisdenalmanack/content/story/almanack"  name="&lpos=cricinfo_mainnav&lid=wisdenalmanack">Wisden Almanack</a></li>

					<li><a href="/insights"  name="&lpos=cricinfo_mainnav&lid=insights">Insights</a></li>

				</ul>
			</div>
			</div>

		</li>

</ul>
<script>
if( $(window).width() <= 1024 && 'ontouchstart' in window == true ){
$(".sub_drop > a").on( "click", function(event) {
	console.log("clicked");
	event.preventDefault();
});
}
</script>
</div>
 <div id="ciHomeContent">


<div class="pnlHdr980Tp" style="_margin-bottom:-9px;_margin-top:5px;"></div>

<div id="ciGblSubnav" style="background:none;margin-top:0px;margin-bottom:0px;width:978px;border-left:1px solid #cdcdcd;border-right:1px solid #cdcdcd;height:auto;">
 <div class="ciGblSubnavbody" style="width:978px;background:#FFF url(http://i.imgci.com/espncricinfo/img_grypnlCtrbg.gif) repeat-x;height:auto;">

<h1 class="SubnavSitesection" style="margin-top:4px;line-height:95%;min-width:22%;width:auto;float:left;">

Only ODI: Scotland v England at Aberdeen, May 9, 2014  <span class="SubnavSitesectionSep">/</span>
  <span class="SubnavSubsection"></span>
 </h1>


<span style="float:right;width:90px; position:relative; z-index:9999;">




</span>



  <div class="divSubnavSeparator" style="clear:both; "></div>

  <div id="ciSubnav">
   <ul>
			    <li class="pad"><a href="/ci/content/story/news.html" >Home</a></li>
		    <li class="pad">|</li>
			    <li class="pad"><a href="/infocus/content/story/infocus.html" >In Focus</a></li>
		    <li class="pad">|</li>
			    <li class="pad"><a href="/ci/content/rss/feeds_rss_cricket.html" >RSS Index</a></li>
		    <li class="pad">|</li>
			    <li class="pad"><a href="http://blogs.cricinfo.com/surfer/" >The Surfer</a></li>
		    <li class="pad">|</li>
			    <li class="pad"><a href="/ci/content/site/product/widgets/news_sizes.html" >News Widget</a></li>





   </ul>
  </div>
 </div>
</div>
<div class="pnlHdr980Btm" style="_overflow:hidden; _height:15px;"></div>
  <div id="ciHomeContentlhs">
<div class="seriesSpncr" align="center" style="height:auto; margin:0; padding:0;text-align: center;" >
<style>.seriesSpncr img{padding-top:0; padding-bottom: 10px;}</style>
</div>
   <!-- START 650 AREA -->




<script language="javascript">
	var omniPageName = "index";
	var omniSiteSection1 = "news";
	var omniCt = "news index";
	var omniSrhType = "news";
</script>

<div id="searchCalendar">
 <div id="searchCalBoxLeft"></div>
 <div id="searchPanel">
  <form type="GET" action="/ci/content/story/search.html" name="storySearch" style="margin:0px; padding:0px;">
   <input type="hidden" name="object" value="684679">

   <div id="srchTxtBg" style="margin-top:24px;">
    <input type="text" name="search" id="stryTxtBox" class="srchTxtBx" value="Search this section" onclick="searchClrTxt('stryTxtBox');" /><input type="image" src="http://i.imgci.com/espncricinfo/searchBtn_new.gif" class="searchBtn" width="56" height="24" border="0" alt="Search" title="Search" align="absmiddle" style="padding-top:0px; margin-top:-4px;"/>
   </div>
  </form>
 </div>
 <div id="calendarPanel">
 </div>
 <div id="searchCalBoxRight"></div>
</div>


<div class="pnl650T"></div>
<div class="pnl650M">


 <p class="srchResHd">Showing news for <b>Only ODI: Scotland v England at Aberdeen, May 9, 2014</b></p>
 <div class="ciPhotoPagination"  style="padding-top:3px; margin-top:0px;" >
<table cellpadding="0" cellspacing="0" border="0" width="100%">
 <tr>
  <td width="30%" class="PaginationHd">
   Showing <span class="PaginationNmbrs">1-5</span>
  </td>
  <td width="30%">
   <img src="http://i.imgci.com/espncricinfo/ciPhotoPrev-disable-icon_13x13.gif" width="13" height="13" alt="Previous page" title="Previous page" border="0" align="texttop" style="padding-left: 13px; padding-right:5px; float:left;" /><span class="Paginationdisable" style="float:left; margin-bottom:2px; margin-left:3px;">Previous</span>
  </td>
  <td width="30%">
   <span class="Paginationdisable" style="padding-right: 13px;">Next <img src="http://i.imgci.com/espncricinfo/ciPhotoNext-disable.gif" width="13" height="13" alt="Next page" title="Next page" border="0" align="texttop" style="padding-left: 5px;" /></span>
  </td>

  <td width="10%" align="right"><a href="/rss/content/story/feeds/684679.xml?type_id=7,8,11"><div id="rssIcon" title="Only ODI: Scotland v England at Aberdeen, May 9, 2014 News RSS Feed" alt="Global News RSS Feed" style="width:20px; float:right; padding: 6px 0 12px 0;"></div></a></td>
 </tr>
</table>
 </div>

 <div class="ciPhotoContainer" >
  <p class="ciSeriesnewsheadtxt">Only ODI, Aberdeen</p>
  <p class="SpecialsHead"><a href="/wisdenalmanack/content/story/918347.html" class="SpecialsHead">Scotland v England, 2014 </a></p>
  <p class="ciSeriesnewscontext">
   <b>Apr 8, 2015</b>:
Wisden's review of the only ODI between Scotland v England, 2014  </p>
  <div class="ciSeriesnewsitalic"><i></i></div>
  <div class="divSeparator"></div>
  <p class="ciSeriesnewsheadtxt">Scotland v England, only ODI, Aberdeen</p>
  <p class="SpecialsHead"><a href="/scotland/content/story/743135.html" class="SpecialsHead">England avoid Scottish slip-up</a></p>
  <p class="ciSeriesnewscontext">
   <b>May 8, 2014</b>:
England's new era has begun with a workmanlike victory over Scotland in Aberdeen  </p>
  <div class="ciSeriesnewsitalic"><i>The Report by George Dobell in Aberdeen</i></div>
  <div class="divSeparator"></div>
  <p class="ciSeriesnewsheadtxt">Scotland v England, only ODI, Aberdeen</p>
  <p class="SpecialsHead"><a href="/england/content/story/742959.html" class="SpecialsHead">England's no-win trip north</a></p>
  <p class="ciSeriesnewscontext">
   <b>May 8, 2014</b>:
Scotland will aim to take advantage of England's vulnerability in a fixture that does little to aid the long-term planning of Peter Moores and Alastair Cook  </p>
  <div class="ciSeriesnewsitalic"><i>George Dobell in Aberdeen</i></div>
  <div class="divSeparator"></div>
  <p class="ciSeriesnewsheadtxt">Scotland v England, only ODI, Aberdeen</p>
  <p class="SpecialsHead"><a href="/scotland/content/story/742877.html" class="SpecialsHead">England's new era begins with tricky test</a></p>
  <p class="ciSeriesnewscontext">
   <b>May 8, 2014</b>:
ESPNcricinfo previews the one-off ODI between Scotland and England in Aberdeen  </p>
  <div class="ciSeriesnewsitalic"><i>The Preview by Alan Gardner</i></div>
  <div class="divSeparator"></div>
  <p class="ciSeriesnewsheadtxt"></p>
  <p class="SpecialsHead"><a href="/magazine/content/story/742805.html" class="SpecialsHead">Auld, dreich, and thran</a></p>
  <p class="ciSeriesnewscontext">
   <b>May 8, 2014</b>:
As England prepare to take on Scotland in an ODI in Aberdeen, a look at the rich history of cricket in and around Mannofield   </p>
  <div class="ciSeriesnewsitalic"><i>Liam Herringshaw</i></div>
 </div>

 <div class="PaginationBttm"  style="margin-top:25px;" >
<table cellpadding="0" cellspacing="0" border="0" width="100%">
 <tr>
  <td width="30%" class="PaginationHd">
   Showing <span class="PaginationNmbrs">1-5</span>
  </td>
  <td width="30%">
   <img src="http://i.imgci.com/espncricinfo/ciPhotoPrev-disable-icon_13x13.gif" width="13" height="13" alt="Previous page" title="Previous page" border="0" align="texttop" style="padding-left: 13px; padding-right:5px; float:left;" /><span class="Paginationdisable" style="float:left; margin-bottom:2px; margin-left:3px;">Previous</span>
  </td>
  <td width="30%">
   <span class="Paginationdisable" style="padding-right: 13px;">Next <img src="http://i.imgci.com/espncricinfo/ciPhotoNext-disable.gif" width="13" height="13" alt="Next page" title="Next page" border="0" align="texttop" style="padding-left: 5px;" /></span>
  </td>

  <td width="10%" align="right"><a href="/rss/content/story/feeds/684679.xml?type_id=7,8,11"><div id="rssIcon" title="Only ODI: Scotland v England at Aberdeen, May 9, 2014 News RSS Feed" alt="Global News RSS Feed" style="width:20px; float:right; padding: 6px 0 12px 0;"></div></a></td>
 </tr>
</table>
 </div>

 <div style="float:left;">
  <p class="ciPhotoGalleryTop" >
  <a href="#"><img src="http://i.imgci.com/espncricinfo/IMG_gallery_top.gif" width="7" align="absmiddle" height="4" border="0" hspace="4"></a><a href="#" class="ciPhotoGalleryToptxt">Top</a>
  </p>
 </div>
</div>


<div class="pnl650B"></div>

   <!-- END 650 AREA -->
  </div>





<div id="ciHomeContentrhs">
<style>
.lvScrAdvt{ width:300px; background:#e5e5e5; text-align:center; height:19px; margin-bottom:5px;}
.lvScrAdvt .txtlnk{ display: inline-block; padding-top: 2px;}
.lvScrAdvt .imglnk{ width: 61px; *float: right; *margin-top: -15px;}
</style>
	<div id="ciHomeLivescoresPanel">
	 <div id="lvScrCnt">
<div class="rhs310" style="margin:0;padding;0; text-align:center" align="center">
<style>.rhs310 img{padding-top:0; padding-bottom: 10px;}</style>

</div>	  <div id="resultsTab" style="height:22px;padding-top:3px;margin:0;background:transparent url(http://i.imgci.com/espncricinfo/wideTabs.gif) no-repeat scroll left top;">
	   <span id="resultTabTxt" class="rsltTbTxt1" style="width:300px;">Tour Results</span>
	  </div>

	  <div id="rstbCont1" style="display:block;">
   <div class="item">
    <a href="/ci/engine/match/684679.html" class="lsMatch" ><b>Scotland v England at Aberdeen    </b></a>
    <span class="lsDate">- May 9, 2014</span><br>
    <span class="lsRslt2">England won by 39 runs (D/L method)    </span>
   </div>


	   <div class="lsRulr"></div>


		   <a href="/ci/engine/series/684673.html" class="ciSectionFooterlink">More results &raquo;</a>
  </div>
 </div>
</div>
 <div id="lvScrBottom"></div>
<div class="pnl320T"></div><div class="pnl320M"><div class="espni-ad-slot ad-incontent" data-slot-type="incontent" data-kvpos="top"></div></div><div class="pnl320B"></div><style type="text/css">
a.mstbactive {
        background:url("http://i.imgci.com/espncricinfo/newsDownarw.jpg") no-repeat scroll 50% 100% transparent;
        color:red;
        font-size:11px;
        color:#333333 !important;
        font-weight:bold !important;
        text-decoration:none;
}
.mstlstnws {background:none !important;padding-bottom:0 !important}
.days {font-size:11px;float:right;#margin-top:-25px;}
.cont #mostnews-1-content,.cont #mostnews-2-content,.cont #mostnews-3-content{display:none}
.latest div{ display:none}
.mostvwd div{ display:none}
.mostdsd div{ display:none}
.standings-nav  a.mstbactive:hover{text-decoration:none !important;}
.standings-nav a:hover{text-decoration:underline;}

</style>
<script type="text/javascript">
jQuery(function ($) {
    jQuery(".srstabHldr li").bind("click", function () {
        var i = jQuery(this).attr("id");
        if (!jQuery(this).hasClass("current")) {
            jQuery(this).siblings().removeClass("current");
            jQuery(this).addClass("current");
        }
        jQuery(this).parents("div.srstabHldr").siblings("div.cont").children("div").css("display", "none");
        jQuery(this).parents("div.srstabHldr").siblings("div.cont").children("div#" + i + "-content").css("display", "block");
    });
        jQuery(".standings-nav a").bind("click", function () {
        var i = jQuery(this).attr("id");
        if (!jQuery(this).hasClass("mstbactive")) {
            jQuery(this).siblings().removeClass("mstbactive");
            jQuery(this).addClass("mstbactive");
        }
        jQuery(this).parents("div.standingsGutter").siblings("div.latest").children("div").css("display", "none");
        jQuery(this).parents("div.standingsGutter").siblings("div.latest").children("div#" + i + "-content").css("display", "block");
                jQuery(this).parents("div.standingsGutter").siblings("div.mostvwd").children("div").css("display", "none");
        jQuery(this).parents("div.standingsGutter").siblings("div.mostvwd").children("div#" + i + "-content").css("display", "block");
                jQuery(this).parents("div.standingsGutter").siblings("div.mostdsd").children("div").css("display", "none");
        jQuery(this).parents("div.standingsGutter").siblings("div.mostdsd").children("div#" + i + "-content").css("display", "block");
    });
});
function changedays(tabname, camefrom) {
	if (tabname == '1') {
		if(jQuery("#mostviw-2").attr("class") == "mstbactive") {
			jQuery(".days").html("Last 7 days");
		} else {
			jQuery(".days").html("Last 3 days");
		}
	} else if (tabname == '2') {
		if(jQuery("#mostdisd-2").attr("class") == "mstbactive") {
			jQuery(".days").html("Last 7 days");
		} else {
			jQuery(".days").html("Last 3 days");
		}
	} else if(tabname == "news") {
                if (camefrom == "mostv") {
                        jQuery("#mostviw-1").attr("class", "mstbactive");
                        jQuery("#mostviw-2").attr("class", "inactive");
                } else if (camefrom == "mostd") {
                        jQuery("#mostdisd-1").attr("class", "mstbactive");
                        jQuery("#mostdisd-2").attr("class", "inactive");
                }
		jQuery(".days").html("Last 3 days");
	} else if (tabname == "specials") {
		if (camefrom == "mostv") {
			jQuery("#mostviw-1").attr("class", "inactive");
			jQuery("#mostviw-2").attr("class", "mstbactive");
		} else if (camefrom == "mostd") {
                        jQuery("#mostdisd-1").attr("class", "inactive");
                        jQuery("#mostdisd-2").attr("class", "mstbactive");
		}
		jQuery(".days").html("Last 7 days");
	}
}
</script>
<div class="srstabHldr">
 <ul id="mostNewtab" class="gryTab">
  <li id="mostnews-1" class="current"><a href="javascript:void(0);">Latest</a></li>
  <li id="mostnews-2"><a href="javascript:void(0);changedays('1');">Most Viewed</a></li>
  <li id="mostnews-3"><a href="javascript:void(0);changedays('2');">Most Discussed</a></li>
 </ul>
</div>

<div class="cont">
  <div style="display:block; _float:left;" id="mostnews-1-content">
    <div class="ciSrstabhldr" style="_width:318px;">
      <div class="lnHeadline" style="padding-top:6px;margin-bottom:4px;">
        <div class="standingsGutter">
          <!-- Latest news sub Tabs -->
          <div class="standings-nav" style="text-align:left;">
            <a class="mstbactive" id="latest-1" href="javascript:void(0);" onClick="mostviwd('mostviw','mostviw_link'); return false;">
              News
            </a> |
            <a id="latest-2" class="inactive" href="javascript:void(0);" onClick="mostviwd('mostvwtab','mostvwtab_link'); return false;">
              Features
            </a>
	  </div>
        </div>
        <!-- Latest News tab content -->
        <div class="latest">
          <div id="latest-1-content" style="display:block;">
   	   <ul>
    	     <li >
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1045195.html">Hales fined for dissent over dismissal
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/scotland/content/story/1045169.html">Scotland's next World Cup win can't take another 21 games - Cannon
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1045157.html">Raina, Yuvraj out of T20Is in USA
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1045155.html">Shafiq leads solid Pakistan reply
	       </a>
    	     </li>
    	     <li class="mstlstnws">
     	       <a class="lnHdlLnks" href="/sri-lanka-v-australia-2016/content/story/1045153.html">It's going to be a turner again, Mathews warns Australia
	       </a>
    	     </li>
   	   </ul>
  	   <div class="ciPanelMoreLink" style="padding-top:0px;_padding-left:10px;">
	     <a href="/ci/content/current/story/news.html" class="ciSectionFooter">More News &raquo;</a>
	   </div>


 	  </div>

	  <div id="latest-2-content" style="display:none;">
<p class='SpecialsHead'> <span id='magazine'  style='margin:0px;'>&nbsp;&nbsp;&nbsp;&nbsp;</span><a href='/magazine/content/story/1044675.html' class='SpecialsHead'>Wild about Zimbabwe</a></p><p class='SpecialsSummary'><b>Diary:</b> Firdose Moonda gets up close to a bunch of rhinos, and also happens to cover a couple of Tests by the by</p><p class='SpecialsHead'> <span id='magazine'  style='margin:0px;'>&nbsp;&nbsp;&nbsp;&nbsp;</span><a href='/magazine/content/story/1045001.html' class='SpecialsHead'>Why Australia can't catch a break in Asia</a></p><p class='SpecialsSummary'><b>Numbers Game:</b> The struggles of Warner, Smith and Lyon in Asia have a lot to do with the team's recent misfortunes</p><p class='SpecialsHead'> <span id='magazine'  style='margin:0px;'>&nbsp;&nbsp;&nbsp;&nbsp;</span><a href='/magazine/content/story/1044163.html' class='SpecialsHead'>The solitary master</a></p><p class='SpecialsSummary'>Loneliness was a theme not just of Hanif Mohammad's batting but also of his career and life. By <b>Osman Samiuddin</b></p><p class='SpecialsHead'><a href='/tcm/content/story/1032793.html' class='SpecialsHead'>Schoolboy Imran</a></p><p class='SpecialsSummary'>How Imran Khan the student became Imran Khan the world-class bowler. By <b>Francis Kelly</b><br><a href='/ci/content/url/784439.html'><b>The Cricket Monthly August issue</b></a></p>    	   <p class="SpecialsHead">
     	     <a class="hpSpecialsHead" href="/blogs/content/story/1037221.html">The hinterland of 40</a>
    	   </p>
    	   <p class="SpecialsSummaryLast"><b>Jon Hotten:</b> At Lord's we saw three in-between scores of the sort that are as likely to annoy the selectors as excite them</p>
   	  </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Most Viewed content start-->


  <div id="mostnews-2-content">
    <div class="ciSrstabhldr" style="_width:318px;">
      <div class="lnHeadline" style="padding-top:6px;margin-bottom:4px;">
        <div class="standingsGutter">
          <!-- Most Viewed sub Tabs -->
          <div class="standings-nav" style="text-align:left;">
	    <a class="mstbactive" id="mostviw-1" href="javascript:void(0);" onClick="changedays('news','mostv'); mostviwd('mostviw','mostviw_link'); return false;">
	      News
 	    </a> |
	    <a  id="mostviw-2" class="inactive" href="javascript:void(0);" onClick="changedays('specials','mostv'); mostviwd('mostvwtab','mostvwtab_link'); return false;">
	      Features
            </a>
	    <span id="daysdisp" class="days">Last 3 days</span>
	  </div>
        </div>

        <!--Most Viewed News tab content -->
        <div class="mostvwd">
          <div id="mostviw-1-content" style="display: block;">
   	   <ul>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044217.html">Ashwin, Saha rescue India on testing day
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044525.html">West Indies reply solidly to India's 353
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1044707.html">Magnificent Moeen punishes Pakistan for lapses
	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044151.html">Carlos Brathwaite named West Indies T20 captain
	       </a>
    	     </li>
    	     <li class="mstlstnws">
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1044231.html">Umar Gul returns to Pakistan's ODI squad
	       </a>
    	     </li>
   	   </ul>
  	   <div class="ciPanelMoreLink" style="padding-top:0px;_padding-left:10px;">
	     <a href="/ci/content/current/story/news.html" class="ciSectionFooter">More News &raquo;</a>
	   </div>


          </div>
      	<!--Most Viewed Spaecials tab content -->
        <div id="mostviw-2-content" style="display: none;">
   	   <p class="SpecialsHead">
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1043897.html">Shami and Ishant - a tale of two bowlers
	       </a>
    	     </p>
	     <p class="SpecialsSummary">
		On his return from a long injury lay-off, Mohammed Shami has executed plans, induced edges and taken wickets. Ishant Sharma, meanwhile, still grapples with familiar concerns
	     </p>
   	   <p class="SpecialsHead">
     	       <a class="lnHdlLnks" href="/sri-lanka-v-australia-2016/content/story/1042811.html">Lucky? Lucky to be playing Australia
	       </a>
    	     </p>
	     <p class="SpecialsSummary">
		As Sri Lanka stretched their lead in Galle after another Australian surrender to spin bowling, stump microphones picked up a touring player using the words 'f*** you guys are lucky'. How so?
	     </p>
   	   <p class="SpecialsHead">
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044419.html">Vijay and Pujara conspicuous by their absence
	       </a>
    	     </p>
	     <p class="SpecialsSummary">
		By leaving out M Vijay and Cheteshwar Pujara, India have compromised the solidity of their top order and perhaps affected the mindset of the omitted batsmen
	     </p>
   	   <p class="SpecialsHead">
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044371.html">Allrounder Ashwin, and India's No. 3 trouble
	       </a>
    	     </p>
	     <p class="SpecialsSummary">
		Stats highlights from the first day's play in St Lucia where R Ashwin and Wriddhiman Saha rescued India after a top-order failure
	     </p>
   	   <p class="SpecialsHead">
     	       <a class="lnHdlLnks" href="/magazine/content/story/1042869.html">What's eating Cheteshwar Pujara?
	       </a>
    	     </p>
	     <p class="SpecialsSummary">
		India's solid No. 3 has been looking out of sorts lately. The problem seems more mental than anything else
	     </p>
   	   </ul>
  	   <div class="ciPanelMoreLink" style="padding-top:0px;_padding-left:10px;">
	     <a href="/ci/content/current/story/news.html" class="ciSectionFooter">More News &raquo;</a>
	   </div>


        </div>
      </div>
    </div>
  </div>
</div>
<!-- Most Discussed content start-->

<div id="mostnews-3-content">
  <div class="ciSrstabhldr" style="_width:318px;">
      <div class="lnHeadline" style="padding-top:6px;margin-bottom:4px;">
      <!--Most discussed news content start -->
      <div class="standingsGutter">
        <!-- Most discussed sub Tabs -->
        <div class="standings-nav" style="text-align:left;">
	  <a class="mstbactive" id="mostdisd-1" href="javascript:void(0);" onClick="changedays('news', 'mostd'); mostdiscd('mostdisd','mostdisd_link'); return false;">
	    News
	  </a> |
	  <a id="mostdisd-2" class="inactive" href="javascript:void(0);" onClick="changedays('specials', 'mostd'); mostdiscd('mostdsdtab','mostdsdtab_link'); return false;">
	    Features
	  </a>
	  <span id="daysdisp" class="days">Last 3 days</span>
	</div>
      </div>
      <!-- Most discussed News Tab content -->
      <div class="mostdsd">
        <div id="mostdisd-1-content" style="display: block;">

	<ul>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044217.html">Ashwin, Saha rescue India on testing day
 (373)	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1044707.html">Magnificent Moeen punishes Pakistan for lapses
 (175)	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044525.html">West Indies reply solidly to India's 353
 (138)	       </a>
    	     </li>
    	     <li >
     	       <a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044151.html">Carlos Brathwaite named West Indies T20 captain
 (127)	       </a>
    	     </li>
    	     <li class="mstlstnws">
     	       <a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1044231.html">Umar Gul returns to Pakistan's ODI squad
 (121)	       </a>
    	     </li>
   	   </ul>

        </div>
        <div id="mostdisd-2-content" style="display: none;">


   	   <ul>
   	   		<p class="SpecialsHead">
     	    	<a class="lnHdlLnks" href="/england-v-pakistan-2016/content/story/1043881.html">England's test of endurance bodes well for Indian winter
 (121)	       		</a>
    	    </p>
	     	<p class="SpecialsSummary">
			In their patient approach to victory at Edgbaston, England unfurled a template that could enable them to repeat their triumph in India this winter
	     	</p>
   	   		<p class="SpecialsHead">
     	    	<a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1044419.html">Vijay and Pujara conspicuous by their absence
 (106)	       		</a>
    	    </p>
	     	<p class="SpecialsSummary">
			By leaving out M Vijay and Cheteshwar Pujara, India have compromised the solidity of their top order and perhaps affected the mindset of the omitted batsmen
	     	</p>
   	   		<p class="SpecialsHead">
     	    	<a class="lnHdlLnks" href="/sri-lanka-v-australia-2016/content/story/1042811.html">Lucky? Lucky to be playing Australia
 (82)	       		</a>
    	    </p>
	     	<p class="SpecialsSummary">
			As Sri Lanka stretched their lead in Galle after another Australian surrender to spin bowling, stump microphones picked up a touring player using the words 'f*** you guys are lucky'. How so?
	     	</p>
   	   		<p class="SpecialsHead">
     	    	<a class="lnHdlLnks" href="/magazine/content/story/1042869.html">What's eating Cheteshwar Pujara?
 (76)	       		</a>
    	    </p>
	     	<p class="SpecialsSummary">
			India's solid No. 3 has been looking out of sorts lately. The problem seems more mental than anything else
	     	</p>
   	   		<p class="SpecialsHead">
     	    	<a class="lnHdlLnks" href="/west-indies-v-india-2016/content/story/1043897.html">Shami and Ishant - a tale of two bowlers
 (64)	       		</a>
    	    </p>
	     	<p class="SpecialsSummary">
			On his return from a long injury lay-off, Mohammed Shami has executed plans, induced edges and taken wickets. Ishant Sharma, meanwhile, still grapples with familiar concerns
	     	</p>
   	   </ul>
        </div>
      </div>
    </div>
  </div>
</div>
</div>
<div class="pnl320B"></div>

<div class="pnl320T"></div>
<div class="pnl320M">
<div id="ciHomeRHSAdslot">
    <ul>
      <li class="left">
      </li>
      <li class="right">
      </li>
    </ul>
    </div>
</div>
<div class="pnl320B"></div>
<div class="pnl320T"></div>
<div class="pnl320M">

 <div class="div300Pad">

  <div class="hpSpncrHead">Sponsored Links</div>
  <p class="ciHomeSponcerLink"><a href="/ci/content/url/742307.html" class="ciHomeSponcerLink" target="_blank"><b>BET NOW on all Tests, ODIs & T20 internationals</b></a></p>
  <p class="spncrSmry">Tournament, match & LIVE fixed odds at bet365</p>
  <div class="divSeparator"></div>
 </div>

</div>
<div class="pnl320B"></div>



<div class="pnl320T"></div><div class="pnl320M"><div class="espni-ad-slot ad-incontent" data-slot-type="incontent" data-kvpos="bottom"></div></div><div class="pnl320B"></div></div>
<div style="clear:both"><!----></div>


 </div>




<script type="text/javascript">
	var endpoint = "submit.espncricinfo.com";
	var server = "www.espncricinfo.com";
</script>

<script src="/navigation/cricinfo/ci/assets/js/src/DisneyOneID.old.min.js?v=1468479867"></script>
<div style="clear: both;"></div>
<div id="footer2Container">
  <div class="footercurveleft"></div>
  <div class="footerContentHolder">
   <div id="cifooternav">
    <ul>
     <li>
      <a href="/ci/content/site/company/site_map.html" class="maintabs">Sitemap</a><span class="maintabseperator">|</span>
      <a href="/ci/content/submit/forms/feedback.html" class="maintabs">Feedback</a><span class="maintabseperator">|</span>
      <a href="/ci/content/rss/feeds_rss_cricket.html" class="maintabs">RSS</a><span class="maintabseperator">|</span>
      <!--<a href="/ci/content/page/156050.html" class="maintabs">Contact us</a><span class="maintabseperator">|</span>-->
      <a href="/ci/content/page/156066.html" class="maintabs">About Us</a><span class="maintabseperator">|</span>

      <a href="http://disneyprivacycenter.com/" class="maintabs" target="_blank">Privacy Policy</a><span class="maintabseperator">|</span>
      <a href="http://disneytermsofuse.com/" class="maintabs" target="_blank">Terms of Use</a>
     </li>
    </ul>
    <ul>
        <li><a class="maintabs" target="_blank" href="http://preferences-mgr.truste.com/?type=espn&affiliateId=148">Interest Based Ads</a><span class="maintabseperator">|</span>
        <a class="maintabs" target="_blank" href="https://disneyprivacycenter.com/notice-to-california-residents/">Your California Privacy Rights</a><span class="maintabseperator">|</span>
        <a class="maintabs" target="_blank" href="https://disneyprivacycenter.com/kids-privacy-policy/english/">Children’s Online Privacy Policy</a></li>
    </ul>
   </div>
   <div id="ciHomefooterlogos">
    <ul>
     <li class="ciespnlogoft"><a href="http://espn.co.uk/" target="_blank" title="ESPN">ESPN</a></li>
     <li class="ciseplogoft"></li>
     <li class="cif1logoft"><a href="http://www.espnf1.com/" target="_blank" title="ESPNF1">ESPNF1</a></li>
     <li class="ciseplogoft"></li>
     <li class="ciscrumlogoft"><a href="http://www.espnscrum.com" target="_blank" title="ESPN Scrum">Espn Scrum</a></li>
     <li class="ciseplogoft"></li>
     <li class="cisoccernetlogoft"><a href="http://soccernet.espn.go.com" target="_blank" title="Espnfc">Espnfc</a></li>
	 <li class="ciseplogoft"></li>
     <li class="footytips"><a href="http://footytips.com.au" target="_blank" title="Footytips">Footytips</a></li>
    </ul>
    <div class="copyright">
    &copy; ESPN Sports Media Ltd.
    </div>
   </div>

  </div>
  <div class="footercurveright"></div>
 </div>
 <style>
#footer2Container .copyright {
    width:125px;
    height:30px;
	font-weight: normal;
	font-size: 11px;
	color: #222222;
	margin: auto;
	padding-top:0px;
	padding-left:3px;
	float:right;
}
#footer2Container #cifooternav ul {
	float:left;
	margin:0px;
	padding: 0px;
	list-style-type: none;
	width:600px;
	height:25px;
}
#footer2Container #ciHomefooterlogos ul {
	margin:0px;
	padding: 0 0 0 0;
	list-style-type: none;
    height: 25px;
}
 </style>


</div>
<!-- Main page Holder ends-->


<script type="text/javascript" language="JavaScript">

	var s_account="wdgespcricinfo";	//(Excludes Wireless)

	//alert(window.location.hostname);
	//alert(s_account);
</script>


<script language="JavaScript" type="text/javascript" src="http://www.espncricinfo.com/navigation/cricinfo/omniture/omniture_global.js?1458313689"></script>


<script src="/navigation/cricinfo/ci/assets/js/src/omniutils.js"></script>

<script type="text/javascript" language="JavaScript">
<!--

//Clearing variable values for link tracking call
function clrLnkTrckVar(){
	//Clear variables
	s_omni.pageName = "";
	s_omni.server = "";
	s_omni.prop1 = "";
	s_omni.prop3 = "";
	s_omni.eVar2 = "";
}

//Link tracking like Video Tab, Video headlines, audio downloads etc.
function lnkTrackVals(name){

	//alert("Video Tab");
	clrLnkTrckVar(); //Clear variables

	var lnkTrck = name;
	s_omni.prop3 = s_omni.eVar2 = lnkTrck;
	s_omni.t();
	//alert(lnkTrck);

}

/* You may give each page an identifying name, server, and channel on the next lines. */
s_omni.server = window.location.host; // Server from the Host
s_omni.prop1 = "cricinfo";

//s_omni.pageName = omniPageName.toLowerCase(); //Omniture Page Name(S)

if(typeof omniSiteSection2 != 'undefined' && typeof omniSiteSubSection3 != 'undefined'){
	s_omni.pageName = omniSiteSection1.toLowerCase() + ":" + omniSiteSection2.toLowerCase() + ":" + omniSiteSection3.toLowerCase() + ":" + omniPageName.toLowerCase(); 	//Page name
}else if(typeof omniSiteSection2 != 'undefined'){
	s_omni.pageName = omniSiteSection1.toLowerCase() + ":" + omniSiteSection2.toLowerCase() + ":" + omniPageName.toLowerCase(); 												//Page name
}else{
	s_omni.pageName = omniSiteSection1.toLowerCase() + ":" + omniPageName.toLowerCase(); 																									//Page name
}

var omniPath = location.pathname;
//alert(omniPath);
if(typeof omniSiteSection1 != 'undefined'){
	s_omni.channel = omniSiteSection1.toLowerCase();
}

//Error page variables
if(typeof omniPageType == 'undefined'){
	s_omni.pageType = "";
}
else{
	s_omni.pageType = "errorPage";
	s_omni.pageName = "";
	s_omni.server = "";
	s_omni.prop1 = "";
}

if(typeof omniCt != 'undefined'){
	s_omni.prop4 = omniCt.toLowerCase();	//Content type
}

if(typeof omniSiteSection2 != 'undefined' && typeof omniSiteSubSection3 != 'undefined'){
	s_omni.prop5 = s_omni.channel + ":" +  omniSiteSection2.toLowerCase() + ":"+  omniSiteSubSection3.toLowerCase();
}else if(typeof omniSiteSection2 != 'undefined'){
	s_omni.prop5 = s_omni.channel + ":" +  omniSiteSection2.toLowerCase();
} else {
	s_omni.prop5 = omniSiteSection1.toLowerCase() + ":" + omniPageName.toLowerCase();
}

if(typeof omniStoryId != 'undefined'){
	s_omni.prop15 = s_omni.eVar20 = omniStoryId; //Story Object id
}
s_omni.prop16 = s_omni.eVar12 = cqanswer //Country where the page is viewed
s_omni.prop17 = s_omni.eVar9 = "en" // Language Code

if(typeof omniAuthId != 'undefined'){
	s_omni.prop23 = s_omni.eVar10 = omniAuthId; //Columnist id
}

s_omni.prop25 = s_omni.eVar19 = "cricket"; // Sport

//Prop29 for capturing the Registered users
var user_name = (typeof getCookie !== "undefined") && getCookie('un');
if (user_name != "");
{
	if (user_name == null || undefined)
	{
		s_omni.prop29 = "anonymous";
}
	else
	{
	s_omni.prop29 = "Registered:Logged in Active";
	}
}

//Prop32 for capturing Player and Grounds ID for the Most viewed objects
if(typeof omniMVO != 'undefined'){
	s_omni.prop32 = omniMVO; //Most viewed objects for Plyers and Grounds
}

//Prop42 for capturing Hawkeye tabs
if(typeof omniHawk != 'undefined'){
	s_omni.prop33 = omniHawk; //capturing Hawkeye tabs
}

s_omni.hier1 = s_omni.pageName;																	//Content Hierarchy
if(typeof omniSrhType != 'undefined'){
	s_omni.eVar11 = omniSrhType;
}
s_omni.eVar13 = s_omni.prop1 + ":" + s_omni.pageName; 						//Page name

//s_omni.prop42 = omniHawk;

/************* DO NOT ALTER ANYTHING BELOW THIS LINE ! **************/
var s_code=s_omni.t();if(s_code)document.write(s_code)//-->

</script>
<!-- End SiteCatalyst code version: H.14. -->

<script type="text/javascript" src="http://content.dl-rms.com/rms/mother/30883/nodetag.js"></script>

<!-- called from lightbox.inc-->
<!-- the photo lightbox starts here...the js for this lies in the base js file -->
<script type="text/javascript">
//Omniture Zoom Tracking

function pickNextImgId(id){



	if(nextId){
		clickMap(nextId,null,null,this,s_omni.prop4);
	}
}
function pickPrevImgId(id){




	if(prevId){
		clickMap(prevId,null,null,this,s_omni.prop4);
	}
}

</script>
<div id="lbBg">
</div>
<div id="photoLightBox" style="display:none;">
	<div id="lboxArea">
		<p class="text" style="float:left;margin:0;padding:0;width:80%;padding:0.3em 0;"></p>
		<p class="close"><a href=""><span class="txt">CLOSE</span><span></span></a></p>
		<div id="lbImg" style="position:relative;">
			<img src="http://i.imgci.com/spacer.gif" />

		</div>
		<div id="lbExtra">

		</div>
		<div id="imgLoading">
			<img src="http://i.imgci.com/espncricinfo/lightbox-ico-loading.gif" align="center" height="32" width="32" />
		</div>
	</div>
</div>




<!-- Begin comScore Tag -->
<script>
var p = document.location.protocol == "https:" ? "https://sb" : "http://b";
var coms_url = p + '.scorecardresearch.com/beacon.js';
$.getScript( coms_url, function( data, textStatus, jqxhr ) {
  if(jqxhr.status === 200){
    COMSCORE.beacon({
    c1:2,
    c2: "3000005",

    c5: "03"

    });
  }
});
</script>
<noscript>
<img src="http://b.scorecardresearch.com/p?c1=2&c2=3000005&c3=dictionary_value1&c4=dictionary_value2&c5=03&c6=dictionary_value3&c10=5-8&cv=2.0&cj=1"/>
</noscript>
<!-- End comScore Tag -->


<script type='text/javascript'>
    var _sf_async_config={};
    /** CONFIGURATION START **/
    _sf_async_config.uid = 26455;
    _sf_async_config.domain = 'espncricinfo.com';
    _sf_async_config.useCanonical = true;
    _sf_async_config.authors  = 'bd';
    _sf_async_config.sections = 'Story';
    /** CONFIGURATION END **/
    (function(){
      function loadChartbeat() {
        window._sf_endpt=(new Date()).getTime();
        var e = document.createElement('script');
        e.setAttribute('language', 'javascript');
        e.setAttribute('type', 'text/javascript');
        e.setAttribute('src',
           (('https:' == document.location.protocol) ? 'https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/' : 'http://static.chartbeat.com/') +
           'js/chartbeat.js');
        document.body.appendChild(e);
      }
      var oldonload = window.onload;
      window.onload = (typeof window.onload != 'function') ?
      loadChartbeat : function() { oldonload(); loadChartbeat(); };
    })();
</script>


<script src="/navigation/cricinfo/ci/assets/js/src/espncricinfo.gpt.1.0.0.min.js?v=1458313688"></script>
</body>
</html>

'''
    # soup = BeautifulSoup(input, "html.parser")
    print(len(soup('p', "SpecialsHead")))

    target = open("TESTT_ODIArticleLink.txt", 'a')
    target.write("Label: " + label + '\n')
    try:
        # line1 = soup.find_all('div', {"class": "teams"}).find('a')
        div = soup.find_all('p', "SpecialsHead")
        # print(div.find_all('a'))
        for line in div:
            links = line.findAll('a', class_="SpecialsHead")
            for a in links:
                # print
                # if 'story'in a['href']:
                #     print('found a url with Story in the link')
                var = 'http://www.espncricinfo.com' + a['href']
                target.write(var)
                target.write('\n')
                # print(var)
            # s = str(links)
            # s=s+'\n'
            # print(s)
            # print('\n')
            # target.write(s)

    except Exception as e:
        print
        str(e)
    target.write('\n\n\n')
def main():
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/index.html?object=667899"
    # content(theurl)
    line_number = 1
    s1=""
    with open('ODIMatchDetail.txt', encoding='utf-8') as a_file:
        for a_line in a_file:
            # print('{:>4} {}'.format(line_number, a_line.rstrip()))
            s = a_line.rstrip()
            if(s!=" "):
                # s = a_line.rstrip()
                # print("HII"+s)
                try:
                    if (s.startswith("Label")):
                        # target.write(s+'\n')
                        # print('here')
                        s1 = s
                        # print("Here "+s)
                        # print(s1)
                    else:
                        content(s, s1)
                        line_number += 1
                except Exception as e:
                    print("Here"+s)
main()


def test():
    # wp = urllib.request.urlopen("http://www.espncricinfo.com")
    # pw = wp.read()
    # print(pw)
    input = '''<html>
 <head><title>Page title</title></head>
 <body>
 <p id="firstpara" align="center">This is paragraph <b>one</b>.
 <p id="secondpara" align="blah">This is paragraph <b>two</b>.
 </html>'''
    soup = BeautifulSoup(input)
    titleTag = soup.html.head.title
    # print(titleTag)
    print(len(soup('p')))

# test()