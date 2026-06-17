# PCT_SHA_DATA

> This table stores relationships between the Postcode, Primary Care Trust, and Strategic Health Authority residence

**Description:** PCT SHA Data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 81

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BTHAS_SC_NBR` | DOUBLE |  |  | Barriers To Housing And Services Score |
| 3 | `BTHAS_SC_R_NBR` | DOUBLE |  |  | Rank Of Barriers To Housing And Services Score (Where 1 Is Most Deprived) |
| 4 | `CAD_SC_NBR` | DOUBLE |  |  | Crime And Disorder Score |
| 5 | `CAD_SC_R_NBR` | DOUBLE |  |  | Rank Of Crime and Disorder Score (Where 1 Is Most Deprived) |
| 6 | `CANNET_TXT` | VARCHAR(3) |  |  | The former cancer network that each postcode falls within. Closed in March 2013 and replaced with Strategic Clinical Networks. |
| 7 | `CANREG_TXT` | VARCHAR(5) |  |  | The cancer registry that each postcode falls within. |
| 8 | `CENED_TXT` | VARCHAR(6) |  |  | Same as PSED except a Census code is provided |
| 9 | `CTRY_TXT` | VARCHAR(9) | NOT NULL |  | The code for the appropriate country |
| 10 | `CYPSD_SC_NBR` | DOUBLE |  |  | Children/Young People Sub-Domain Score |
| 11 | `CYPSD_SC_R_NBR` | DOUBLE |  |  | Rank of Children/Young People Sub-Domain Score (Where 1 Is Most Deprived) |
| 12 | `DOINTR_DT_TM` | DATETIME | NOT NULL |  | The most recent occurrence of the postcode¿s date of introduction. |
| 13 | `DOTERM_DT_TM` | DATETIME |  |  | If present, the most recent occurrence of the postcode¿s date of termination, otherwise 31-DEC-2100 indicates live postcode. |
| 14 | `EDIND_FLAG` | DOUBLE | NOT NULL |  | Shows the status of the assigned ED. |
| 15 | `EMPL_SC_NBR` | DOUBLE |  |  | Employment Score |
| 16 | `EMPL_SC_R_NBR` | DOUBLE |  |  | Rank Of Employment Score (Where 1 Is Most Deprived) |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `ESAT_SC_NBR` | DOUBLE |  |  | Education Skills And Training Score |
| 19 | `ESAT_SC_R_NBR` | DOUBLE |  |  | Rank Of Education Skills And Training Score (Where 1 Is Most Deprived) |
| 20 | `GBSD_SC_NBR` | DOUBLE |  |  | Geographical Barriers Sub-Domain Score |
| 21 | `GBSD_SC_R_NBR` | DOUBLE |  |  | Rank of Geographical Barriers Sub-Domain Score (Where 1 Is Most Deprived) |
| 22 | `GOR_TXT` | VARCHAR(9) |  |  | The Region code for each postcode. |
| 23 | `HDAD_SC_NBR` | DOUBLE |  |  | Health Deprivation And Disability Score |
| 24 | `HDAD_SC_R_NBR` | DOUBLE |  |  | Rank Of Health Deprivation And Disability Score (Where 1 Is Most Deprived) |
| 25 | `HRO_TXT` | VARCHAR(3) |  |  | The former Pan SHA responsible for the associated strategic health authority for each postcode in England. |
| 26 | `IDACI_SC_NBR` | DOUBLE |  |  | Income Deprivation Affecting Children Index Score |
| 27 | `IDACI_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Deprivation Affecting Children Index Score (Where 1 Is Most Deprived) |
| 28 | `IDAOPI_SC_NBR` | DOUBLE |  |  | Income Deprivation Affecting Older People Index Score |
| 29 | `IDAOPI_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Deprivation Affecting Older People Index Score (Where 1 Is Most Deprived) |
| 30 | `IMD_SC_NBR` | DOUBLE |  |  | Index of Mass Deprivation Score |
| 31 | `IMD_SC_R_NBR` | DOUBLE |  |  | Rank of Index of Mass Deprivation Score (Where 1 Is Most Deprived) |
| 32 | `INC_SC_NBR` | DOUBLE |  |  | Income Score |
| 33 | `INC_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Score (Where 1 Is Most Deprived) |
| 34 | `ISD_SC_NBR` | DOUBLE |  |  | Indoors Sub-Domain Score |
| 35 | `ISD_SC_R_NBR` | DOUBLE |  |  | Rank of Indoors Sub-Domain Score (Where 1 Is Most Deprived) |
| 36 | `LE_SC_NBR` | DOUBLE |  |  | Living Environment Score |
| 37 | `LE_SC_R_NBR` | DOUBLE |  |  | Rank Of Living Environment Score (Where 1 Is Most Deprived) |
| 38 | `LSOA01_TXT` | VARCHAR(9) | NOT NULL |  | The 2001 Census Lower Layer SOA code for England and Wales, SOA code for Northern Ireland and data zone code for Scotland. |
| 39 | `LSOA11_TXT` | VARCHAR(9) |  |  | The 2011 Census lower layer SOA code for England and Wales, SOA code for Northern Ireland and data zone code for Scotland. |
| 40 | `MSOA01_TXT` | VARCHAR(9) |  |  | The 2001 Census Middle Layer SOA (MSOA) code for England and Wales and intermediate zone for Scotland. |
| 41 | `MSOA11_TXT` | VARCHAR(9) |  |  | The 2011 Census middle layer SOA (MSOA) code for England and Wales and intermediate zone for Scotland. |
| 42 | `NHSAT_TXT` | VARCHAR(3) |  |  | The Area Team code for the postcode. |
| 43 | `NHSCR_TXT` | VARCHAR(3) |  |  | The Commissioning Region code for the postcode. |
| 44 | `OA01_TXT` | VARCHAR(10) |  |  | The 2001 Census Output Areas were built from unit postcodes and constrained to 2003 `statistical¿ wards, and they form the building bricks for defining higher level geographies. |
| 45 | `OA11_TXT` | VARCHAR(9) |  |  | The 2011 Census output areas were based on 2001 Census output areas, and they form the building bricks for defining higher level geographies. |
| 46 | `ODSLAUA_TXT` | VARCHAR(3) |  |  | Organisation Data Service allocated identifiers for top-tier Local Authority organisations in England and Wales to which the postcode has been assigned |
| 47 | `OLDHA_TXT` | VARCHAR(3) |  |  | The health authority existing prior to the reorganisation of health areas (England in 2002, Wales in 2003). |
| 48 | `OLDHRO_TXT` | VARCHAR(3) |  |  | The pre-Pan SHA IT Cluster responsible for the associated strategic health authority for each postcode in England. |
| 49 | `OLDPCT_TXT` | VARCHAR(3) |  |  | The pre-October 2006 code for the primary care areas in England and Wales; primary care areas do not exist in Scotland or Northern Ireland. |
| 50 | `OSCTY_TXT` | VARCHAR(9) |  |  | The county to which the postcode has been assigned. |
| 51 | `OSD_SC_NBR` | DOUBLE |  |  | Outdoors Sub-Domain Score |
| 52 | `OSD_SC_R_NBR` | DOUBLE |  |  | Rank of Outdoors Sub-Domain Score(Where 1 Is Most Deprived) |
| 53 | `OSEAST100M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Easting to 100 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 54 | `OSEAST1M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Easting to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 55 | `OSGRDIND_FLAG` | DOUBLE | NOT NULL |  | Shows the status of the assigned grid reference. |
| 56 | `OSHAPREV_TXT` | VARCHAR(3) |  |  | The health area code for the postcode prior to the NHS reorganisation on 1 July 2006. |
| 57 | `OSLAUA_TXT` | VARCHAR(9) |  |  | The district/UA to which the postcode has been assigned. |
| 58 | `OSNRTH100M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Northing to 100 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 59 | `OSNRTH1M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Northing to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 60 | `OSWARD_TXT` | VARCHAR(9) |  |  | The administrative/electoral area to which the postcode has been assigned. |
| 61 | `PCDS_TXT` | VARCHAR(8) | NOT NULL |  | Unformatted postcode:2, 3 or 4-character outward codeSingle space () 3-character inward codePseudo country postcode as used by the NHS. |
| 62 | `PCON_TXT` | VARCHAR(9) |  |  | The Westminster Parliamentary Constituency code for each postcode. Pseudo codes are included for Channel Islands and Isle of Man. |
| 63 | `PCT_RESIDENCE` | VARCHAR(3) | NOT NULL |  | PCT/CT of Residence |
| 64 | `PCT_TXT` | VARCHAR(3) |  |  | The code for the Primary Care areas in England, LHBs in Wales, CHPs in Scotland, LCG in Northern Ireland and PHD in the Isle of Man prior to the abolition of PCTs in 2013; there are no equivalent areas in the Channel Islands |
| 65 | `POSTCODE` | VARCHAR(8) | NOT NULL |  | Residence Postcode |
| 66 | `POSTCODE_KEY` | VARCHAR(8) |  |  | key value form of Residence Postcode |
| 67 | `PSED_TXT` | VARCHAR(8) |  |  | The code for the 1991 Census ED. |
| 68 | `SCN_TXT` | VARCHAR(3) |  |  | The Strategic Clinical Network that each postcode falls within. Introduced in April 2013. |
| 69 | `SHA_RESIDENCE` | VARCHAR(3) | NOT NULL |  | Strategic Health Authority of Residence |
| 70 | `SSD_SC_NBR` | DOUBLE |  |  | Skills Sub-Domain Score |
| 71 | `SSD_SC_R_NBR` | DOUBLE |  |  | Rank of Skills Sub-Domain Score (Where 1 Is Most Deprived) |
| 72 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 73 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 74 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 75 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 76 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 77 | `UR01IND_TXT` | VARCHAR(1) |  |  | The 2001 Census Urban and rural classification of Output Areas for England and Wales, Scotland and Northern Ireland. |
| 78 | `USERTYPE_FLAG` | DOUBLE | NOT NULL |  | Shows whether the postcode is a small or large user.0 = small user;1 = large user |
| 79 | `WARD98_TXT` | VARCHAR(6) |  |  | The 1998 administrative and electoral areas for each postcode. |
| 80 | `WBSD_SC_NBR` | DOUBLE |  |  | Wider Barriers Sub-Domain Score |
| 81 | `WBSD_SC_R_NBR` | DOUBLE |  |  | Rank of Wider Barriers Sub-Domain Score (Where 1 Is Most Deprived) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

