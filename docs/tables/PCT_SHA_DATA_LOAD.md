# PCT_SHA_DATA_LOAD

> This is a temporary LOAD table.

**Description:** PCT SHA Data Load  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BTHAS_SC_NBR` | DOUBLE |  |  | Barriers To Housing And Services Score |
| 2 | `BTHAS_SC_R_NBR` | DOUBLE |  |  | Rank Of Barriers To Housing And Services Score (Where 1 Is Most Deprived) |
| 3 | `CAD_SC_NBR` | DOUBLE |  |  | Crime And Disorder Score |
| 4 | `CAD_SC_R_NBR` | DOUBLE |  |  | Rank Of Crime and Disorder Score (Where 1 Is Most Deprived) |
| 5 | `CANNET_TXT` | VARCHAR(3) |  |  | The former cancer network that each postcode falls within. Closed in March 2013 and replaced with Strategic Clinical Networks. |
| 6 | `CANREG_TXT` | VARCHAR(5) |  |  | The cancer registry that each postcode falls within. |
| 7 | `CENED_TXT` | VARCHAR(6) |  |  | Same as PSED except a Census code is provided |
| 8 | `CTRY_TXT` | VARCHAR(9) | NOT NULL |  | The code for the appropriate country |
| 9 | `CYPSD_SC_NBR` | DOUBLE |  |  | Children/Young People Sub-Domain Score |
| 10 | `CYPSD_SC_R_NBR` | DOUBLE |  |  | Rank of Children/Young People Sub-Domain Score (Where 1 Is Most Deprived) |
| 11 | `DOINTR_DT_TM` | DATETIME | NOT NULL |  | The most recent occurrence of the postcode¿s date of introduction. |
| 12 | `DOTERM_DT_TM` | DATETIME |  |  | If present, the most recent occurrence of the postcode¿s date of termination, otherwise 31-DEC-2100 indicates live postcode. |
| 13 | `EDIND_FLAG` | DOUBLE |  |  | Shows the status of the assigned ED. |
| 14 | `EMPL_SC_NBR` | DOUBLE |  |  | Employment Score |
| 15 | `EMPL_SC_R_NBR` | DOUBLE |  |  | Rank Of Employment Score (Where 1 Is Most Deprived) |
| 16 | `ESAT_SC_NBR` | DOUBLE |  |  | Education Skills And Training Score |
| 17 | `ESAT_SC_R_NBR` | DOUBLE |  |  | Rank Of Education Skills And Training Score (Where 1 Is Most Deprived) |
| 18 | `GBSD_SC_NBR` | DOUBLE |  |  | Geographical Barriers Sub-Domain Score |
| 19 | `GBSD_SC_R_NBR` | DOUBLE |  |  | Rank of Geographical Barriers Sub-Domain Score (Where 1 Is Most Deprived) |
| 20 | `GOR_TXT` | VARCHAR(9) |  |  | The Region code for each postcode. |
| 21 | `HDAD_SC_NBR` | DOUBLE |  |  | Health Deprivation And Disability Score |
| 22 | `HDAD_SC_R_NBR` | DOUBLE |  |  | Rank Of Health Deprivation And Disability Score (Where 1 Is Most Deprived) |
| 23 | `HRO_TXT` | VARCHAR(3) |  |  | The former Pan SHA responsible for the associated strategic health authority for each postcode in England. |
| 24 | `IDACI_SC_NBR` | DOUBLE |  |  | Income Deprivation Affecting Children Index Score |
| 25 | `IDACI_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Deprivation Affecting Children Index Score (Where 1 Is Most Deprived) |
| 26 | `IDAOPI_SC_NBR` | DOUBLE |  |  | Income Deprivation Affecting Older People Index Score |
| 27 | `IDAOPI_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Deprivation Affecting Older People Index Score (Where 1 Is Most Deprived) |
| 28 | `IMD_SC_NBR` | DOUBLE |  |  | Index of Mass Deprivation Score |
| 29 | `IMD_SC_R_NBR` | DOUBLE |  |  | Rank of Index of Mass Deprivation Score (Where 1 Is Most Deprived) |
| 30 | `INC_SC_NBR` | DOUBLE |  |  | Income Score |
| 31 | `INC_SC_R_NBR` | DOUBLE |  |  | Rank Of Income Score (Where 1 Is Most Deprived) |
| 32 | `ISD_SC_NBR` | DOUBLE |  |  | Indoors Sub-Domain Score |
| 33 | `ISD_SC_R_NBR` | DOUBLE |  |  | Rank of Indoors Sub-Domain Score (Where 1 Is Most Deprived) |
| 34 | `LE_SC_NBR` | DOUBLE |  |  | Living Environment Score |
| 35 | `LE_SC_R_NBR` | DOUBLE |  |  | Rank Of Living Environment Score (Where 1 Is Most Deprived) |
| 36 | `LSOA01_TXT` | VARCHAR(9) | NOT NULL |  | The 2001 Census Lower Layer SOA code for England and Wales, SOA code for Northern Ireland and data zone code for Scotland. |
| 37 | `LSOA11_TXT` | VARCHAR(9) |  |  | The 2011 Census lower layer SOA code for England and Wales, SOA code for Northern Ireland and data zone code for Scotland. |
| 38 | `MSOA01_TXT` | VARCHAR(9) |  |  | The 2001 Census Middle Layer SOA (MSOA) code for England and Wales and intermediate zone for Scotland. |
| 39 | `MSOA11_TXT` | VARCHAR(9) |  |  | The 2011 Census middle layer SOA (MSOA) code for England and Wales and intermediate zone for Scotland. |
| 40 | `NHSAT_TXT` | VARCHAR(3) |  |  | The Area Team code for the postcode. |
| 41 | `NHSCR_TXT` | VARCHAR(3) |  |  | The Commissioning Region code for the postcode. |
| 42 | `OA01_TXT` | VARCHAR(10) |  |  | The 2001 Census Output Areas were built from unit postcodes and constrained to 2003 `statistical¿ wards, and they form the building bricks for defining higher level geographies. |
| 43 | `OA11_TXT` | VARCHAR(9) |  |  | The 2011 Census output areas were based on 2001 Census output areas, and they form the building bricks for defining higher level geographies. |
| 44 | `ODSLAUA_TXT` | VARCHAR(3) |  |  | Organisation Data Service allocated identifiers for top-tier Local Authority organisations in England and Wales to which the postcode has been assigned |
| 45 | `OLDHA_TXT` | VARCHAR(3) |  |  | The health authority existing prior to the reorganisation of health areas (England in 2002, Wales in 2003). |
| 46 | `OLDHRO_TXT` | VARCHAR(3) |  |  | The pre-Pan SHA IT Cluster responsible for the associated strategic health authority for each postcode in England. |
| 47 | `OLDPCT_TXT` | VARCHAR(3) |  |  | The pre-October 2006 code for the primary care areas in England and Wales; primary care areas do not exist in Scotland or Northern Ireland. |
| 48 | `OSCTY_TXT` | VARCHAR(9) |  |  | The county to which the postcode has been assigned. |
| 49 | `OSD_SC_NBR` | DOUBLE |  |  | Outdoors Sub-Domain Score |
| 50 | `OSD_SC_R_NBR` | DOUBLE |  |  | Rank of Outdoors Sub-Domain Score(Where 1 Is Most Deprived) |
| 51 | `OSEAST100M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Easting to 100 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 52 | `OSEAST1M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Easting to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 53 | `OSGRDIND_FLAG` | DOUBLE | NOT NULL |  | Shows the status of the assigned grid reference. |
| 54 | `OSHAPREV_TXT` | VARCHAR(3) |  |  | The health area code for the postcode prior to the NHS reorganisation on 1 July 2006. |
| 55 | `OSLAUA_TXT` | VARCHAR(9) |  |  | The district/UA to which the postcode has been assigned. |
| 56 | `OSNRTH100M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Northing to 100 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 57 | `OSNRTH1M_NBR` | DOUBLE |  |  | The Ordnance Survey postcode grid reference Northing to 1 metre resolution; blank for postcodes in the Channel Islands and the Isle of Man. Grid references for postcodes in Northern Ireland relate to the Irish Grid system. |
| 58 | `OSWARD_TXT` | VARCHAR(9) |  |  | The administrative/electoral area to which the postcode has been assigned. |
| 59 | `PCDS_TXT` | VARCHAR(8) | NOT NULL |  | Unformatted postcode:2, 3 or 4-character outward codeSingle space () 3-character inward codePseudo country postcode as used by the NHS. |
| 60 | `PCON_TXT` | VARCHAR(9) |  |  | The Westminster Parliamentary Constituency code for each postcode. Pseudo codes are included for Channel Islands and Isle of Man. |
| 61 | `PCT_RESIDENCE` | VARCHAR(3) | NOT NULL |  | PCT/CT of Residence |
| 62 | `PCT_TXT` | VARCHAR(3) |  |  | The code for the Primary Care areas in England, LHBs in Wales, CHPs in Scotland, LCG in Northern Ireland and PHD in the Isle of Man prior to the abolition of PCTs in 2013; there are no equivalent areas in the Channel Islands |
| 63 | `POSTCODE` | VARCHAR(8) | NOT NULL |  | Residence Postcode |
| 64 | `PSED_TXT` | VARCHAR(8) |  |  | The code for the 1991 Census ED. |
| 65 | `SCN_TXT` | VARCHAR(3) |  |  | The Strategic Clinical Network that each postcode falls within. Introduced in April 2013. |
| 66 | `SHA_RESIDENCE` | VARCHAR(3) | NOT NULL |  | Strategic Health Authority of Residence |
| 67 | `SSD_SC_NBR` | DOUBLE |  |  | Skills Sub-Domain Score |
| 68 | `SSD_SC_R_NBR` | DOUBLE |  |  | Rank of Skills Sub-Domain Score (Where 1 Is Most Deprived) |
| 69 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 70 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 71 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 72 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 73 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 74 | `UR01IND_TXT` | VARCHAR(1) |  |  | The 2001 Census Urban and rural classification of Output Areas for England and Wales, Scotland and Northern Ireland. |
| 75 | `USERTYPE_FLAG` | DOUBLE | NOT NULL |  | Shows whether the postcode is a small or large user.0 = small user;1 = large user |
| 76 | `WARD98_TXT` | VARCHAR(6) |  |  | The 1998 administrative and electoral areas for each postcode. |
| 77 | `WBSD_SC_NBR` | DOUBLE |  |  | Wider Barriers Sub-Domain Score |
| 78 | `WBSD_SC_R_NBR` | DOUBLE |  |  | Rank of Wider Barriers Sub-Domain Score (Where 1 Is Most Deprived) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

