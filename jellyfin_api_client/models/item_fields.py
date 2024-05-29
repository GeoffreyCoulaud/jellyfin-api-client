from enum import Enum


class ItemFields(str, Enum):
    AIRTIME = "AirTime"
    CANDELETE = "CanDelete"
    CANDOWNLOAD = "CanDownload"
    CHANNELIMAGE = "ChannelImage"
    CHANNELINFO = "ChannelInfo"
    CHAPTERS = "Chapters"
    CHILDCOUNT = "ChildCount"
    CUMULATIVERUNTIMETICKS = "CumulativeRunTimeTicks"
    CUSTOMRATING = "CustomRating"
    DATECREATED = "DateCreated"
    DATELASTMEDIAADDED = "DateLastMediaAdded"
    DATELASTREFRESHED = "DateLastRefreshed"
    DATELASTSAVED = "DateLastSaved"
    DISPLAYPREFERENCESID = "DisplayPreferencesId"
    ENABLEMEDIASOURCEDISPLAY = "EnableMediaSourceDisplay"
    ETAG = "Etag"
    EXTERNALETAG = "ExternalEtag"
    EXTERNALSERIESID = "ExternalSeriesId"
    EXTERNALURLS = "ExternalUrls"
    EXTRAIDS = "ExtraIds"
    GENRES = "Genres"
    HEIGHT = "Height"
    HOMEPAGEURL = "HomePageUrl"
    INHERITEDPARENTALRATINGVALUE = "InheritedParentalRatingValue"
    ISHD = "IsHD"
    ITEMCOUNTS = "ItemCounts"
    LOCALTRAILERCOUNT = "LocalTrailerCount"
    MEDIASOURCECOUNT = "MediaSourceCount"
    MEDIASOURCES = "MediaSources"
    MEDIASTREAMS = "MediaStreams"
    ORIGINALTITLE = "OriginalTitle"
    OVERVIEW = "Overview"
    PARENTID = "ParentId"
    PATH = "Path"
    PEOPLE = "People"
    PLAYACCESS = "PlayAccess"
    PRESENTATIONUNIQUEKEY = "PresentationUniqueKey"
    PRIMARYIMAGEASPECTRATIO = "PrimaryImageAspectRatio"
    PRODUCTIONLOCATIONS = "ProductionLocations"
    PROVIDERIDS = "ProviderIds"
    RECURSIVEITEMCOUNT = "RecursiveItemCount"
    REFRESHSTATE = "RefreshState"
    REMOTETRAILERS = "RemoteTrailers"
    SCREENSHOTIMAGETAGS = "ScreenshotImageTags"
    SEASONUSERDATA = "SeasonUserData"
    SERIESPRESENTATIONUNIQUEKEY = "SeriesPresentationUniqueKey"
    SERIESPRIMARYIMAGE = "SeriesPrimaryImage"
    SERIESSTUDIO = "SeriesStudio"
    SERVICENAME = "ServiceName"
    SETTINGS = "Settings"
    SORTNAME = "SortName"
    SPECIALEPISODENUMBERS = "SpecialEpisodeNumbers"
    SPECIALFEATURECOUNT = "SpecialFeatureCount"
    STUDIOS = "Studios"
    TAGLINES = "Taglines"
    TAGS = "Tags"
    THEMESONGIDS = "ThemeSongIds"
    THEMEVIDEOIDS = "ThemeVideoIds"
    TRICKPLAY = "Trickplay"
    WIDTH = "Width"

    def __str__(self) -> str:
        return str(self.value)
