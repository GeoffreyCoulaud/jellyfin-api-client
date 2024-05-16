from enum import Enum


class ItemSortBy(str, Enum):
    AIREDEPISODEORDER = "AiredEpisodeOrder"
    AIRTIME = "AirTime"
    ALBUM = "Album"
    ALBUMARTIST = "AlbumArtist"
    ARTIST = "Artist"
    COMMUNITYRATING = "CommunityRating"
    CRITICRATING = "CriticRating"
    DATECREATED = "DateCreated"
    DATELASTCONTENTADDED = "DateLastContentAdded"
    DATEPLAYED = "DatePlayed"
    DEFAULT = "Default"
    INDEXNUMBER = "IndexNumber"
    ISFAVORITEORLIKED = "IsFavoriteOrLiked"
    ISFOLDER = "IsFolder"
    ISPLAYED = "IsPlayed"
    ISUNPLAYED = "IsUnplayed"
    NAME = "Name"
    OFFICIALRATING = "OfficialRating"
    PARENTINDEXNUMBER = "ParentIndexNumber"
    PLAYCOUNT = "PlayCount"
    PREMIEREDATE = "PremiereDate"
    PRODUCTIONYEAR = "ProductionYear"
    RANDOM = "Random"
    RUNTIME = "Runtime"
    SEARCHSCORE = "SearchScore"
    SERIESDATEPLAYED = "SeriesDatePlayed"
    SERIESSORTNAME = "SeriesSortName"
    SIMILARITYSCORE = "SimilarityScore"
    SORTNAME = "SortName"
    STARTDATE = "StartDate"
    STUDIO = "Studio"
    VIDEOBITRATE = "VideoBitRate"

    def __str__(self) -> str:
        return str(self.value)
