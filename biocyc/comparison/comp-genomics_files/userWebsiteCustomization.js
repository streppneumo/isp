YAHOO.namespace ("ptools");

YAHOO.ptools.popularDatabases = ["ECOLI", "META", "HUMAN", "MTBRV", "BSUB", "YEAST"];

function addSiteSpecificMenuItems () {
  adjustTextpressoMenuItem(orgID()); 
}

function userAdjustMenuItemsOrgID(orgid){
  adjustTextpressoMenuItem(orgid);
  adjustBioCycGuideMenuItem();
}

function adjustTextpressoMenuItem(orgid) {
 var menuItem = YAHOO.widget.MenuManager.getMenuItem("textpressoMenuItem");
 if (orgid == 'ECOLI') {
    if (menuItem == null) {
       var searchMenu = YAHOO.widget.MenuManager.getMenu("search");
       if (searchMenu != null) searchMenu.addItem ({ id:"textpressoMenuItem", url: "/ecocyc/textpresso.shtml", text: "Search Full-text Articles"});
    } else menuItem.cfg.setProperty("disabled",false); 
  } else 
  // Deactivate the menu item since it is not E. coli
  if (menuItem != null) menuItem.cfg.setProperty("disabled",true);
}

function adjustBioCycGuideMenuItem() {
 var menuItem = YAHOO.widget.MenuManager.getMenuItem("BioCycGuide");
 var orgid = orgIDFromHostname();
 if (orgid == 'ECOLI') {
     menuItem.cfg.setProperty("text","Guide&nbsp;to&nbsp;EcoCyc");
     menuItem.cfg.setProperty("url", "http://asmscience.org/content/journal/ecosalplus/10.1128/ecosalplus.ESP-0009-2013");
 }
 else if (orgid == 'META') {
     menuItem.cfg.setProperty("text","Guide&nbsp;to&nbsp;MetaCyc");
     menuItem.cfg.setProperty("url", "/MetaCycUserGuide.shtml");
 }
}

/*  
    Potentially make visible one of the TmpMsg div in the page which
    is typically in the banner. We do not show the message if it
    contains only spaces, newlines, and tabs. Note: the space for the
    message is small. See parameter width below.
    
    The page might contain one or several of the div IDs listed below:
    biocycTmpMessages, ecocycTmpMessages, metacycTmpMessages,
    humancycTmpMessages, or bsubcycTmpMessages.  

    Each division contains one or several DIVs
    that might contain a message.  One of these messages is randomly
    selected to be displayed as temporary message in the banner.

    This function does not assume that all or any of these
    temporary message DIVs exist.

    See also file temporary-message.shtml.

    Returns: nothing.
*/
function insertTemporaryMessage(){
    var orgID    = window.orgID(); // Not sure why this has to be fully qualified
                                   // But doesn't work if it's not.
    var bioTmp   = document.getElementById('biocycTmpMessages');
    var ecoTmp   = document.getElementById('ecocycTmpMessages');
    var metaTmp  = document.getElementById('metacycTmpMessages');
    var humanTmp = document.getElementById('humancycTmpMessages');
    var bsubTmp  = document.getElementById('bsubcycTmpMessages');
    var tmpDivs  = [{orgID: 'ECOLI', div: ecoTmp}, 
	{orgID: 'META',  div: metaTmp}, 
	{orgID: 'HUMAN', div: humanTmp},
        {orgID: 'BSUB',  div: bsubTmp},
	{orgID: false,   div: bioTmp} // must be the last one and is the default.
    ];
    // In the following do not assume that any of the elements
    // above exist.

    // Make all of the temporary messages invisible.
    for (var j=0; j < tmpDivs.length; j++){
	if (tmpDivs[j].div  != null) {
	    var childs = tmpDivs[j].div.childNodes;
	    var n      = (childs == null) ? 0 : childs.length;
	    // Turn off the display of all the childs.
	    for (var i=0; i < n; i++) {
		var oneTmp = childs[i];
		if (oneTmp && oneTmp.style) {
		    oneTmp.style.width   = '0';
		    oneTmp.style.display = 'none';
		}}}}

    // Make one of the temporary message visible if such a message is not empty.
    for (var j=0; j < tmpDivs.length; j++) {
	var oneEntry = tmpDivs[j];
	var oneDiv   = oneEntry.div;
	if (oneDiv && (orgID == oneEntry.orgID || !oneEntry.orgID)) {
	    // The orgID says to use this oneDiv.
	    var childs = oneDiv.childNodes;
	    var n      = (childs == null) ? 0 : childs.length;
	    // Gather the childs that have indeed a message in it.
	    var nonEmptyChilds = new Array();
	    for (var i=0; i < n; i++) {
		var oneDivChild = childs[i]; 
		if (oneDivChild.innerHTML && oneDivChild.innerHTML.search('[^ \n\t]') >= 0) {
		    nonEmptyChilds.push(oneDivChild);
		}
	    }

	    var nb   = nonEmptyChilds.length;
	    // Select randomly one of the non-empty div child
	    if (nb > 0) {
		var seed = (new Date()).getSeconds();
		var r    = Math.floor(Math.random(seed)*nb);
		if (nonEmptyChilds[r].style) {
		    nonEmptyChilds[r].style.width   = '180px';
		    nonEmptyChilds[r].style.display = 'block'; 
		}
	    }
	    return;
	}
    }
}


// paley:Jul-24-2013 The behavior below has been eliminated now that the
// selected organism should always match the page content.  However, if the
// selected organism does not match the virtual host, redirect to biocyc.org.
// Old behavior:
// If we've been redirected to a biocyc.org url from a metacyc, ecocyc or 
// humancyc url, then set the current organism to the organism in the referer
// URL. 
// latendre:Nov-19-2009: but even if we are coming from metacyc, it does not
// mean that the selected organism was meta, it can be any organism.
// paley:Feb-16-2010 To solve the issue Mario mentions (the user deliberately
//  selects a different organism from, say, the metacyc home page, check for an
//  orgid in the URL first.
// paley:Sep-15-2010 If the referrer is a non-biocyc site, change the selected
//  organism to the one in the url, if any.
function userDefinedBeforePathwayToolsInit() {
    var urlOrg = orgIDFromURL ();
    var hostnameOrg = orgIDFromHostname();
    if (hostnameOrg && urlOrg && (urlOrg != hostnameOrg)) {
	// If the hostname doesn't match the url org, redirect to biocyc.org
	var hostElts = location.hostname.split(".");
	if (hostElts.length >=2 
	    && hostElts[hostElts.length - 2].toUpperCase() == "SRI")
	    location.hostname = "brg-preview.ai.sri.com"; // preview server
	else location.hostname = "www.biocyc.org";
   }
    /* ;; paley:Jul-24-2013 Replace all this w/ the above few lines
  var org;
  if (location.pathname.search(/redirect=T/i) >= 0 || 
      document.referrer == undefined) {
    org = orgIDFromURL();
    if (orgNameFromOrgID(org)) setOrganism(org);
  }
  else if (document.referrer != undefined && 
           location.hostname.search(/biocyc/i) >= 0) {
    var pos = document.referrer.search(/ecocyc/i);
    if (pos == -1) pos = document.referrer.search(/metacyc/i);
    if (pos == -1) pos = document.referrer.search(/humancyc/i);
    if (pos == -1) pos = document.referrer.search(/bsubcyc/i);
    if (pos > 0) {
      org = orgIDFromURL() || document.referrer.substring(pos).split("/")[1];
      if (orgNameFromOrgID(org)) setOrganism(org);
    }
    else if (document.referrer.search(/biocyc.org/i) == -1) {
      org = orgIDFromURL();
      if (orgNameFromOrgID(org)) setOrganism(org);
    }
  }
    */
    setLogoLink();
}

/* Use this function to override the default link that the banner logo
   links to. It's overridden by organism.
*/
function setLogoLink () {
    var banner   = document.getElementById('ptbanner');
    var logolink = document.getElementById('logoLink');

    var org = orgID();
    if ( org == 'ECOL316407' ) {
        logolink.href = "http://www.porteco.org";
    }
}

function userDefinedAfterPathwayToolsInit(){
    setLogoLink();
}

