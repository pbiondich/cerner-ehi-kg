# ZIP_DEFAULT

> Zip code defaults table.

**Description:** Zip Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CITY` | VARCHAR(40) |  |  | Name of the City. |
| 6 | `CITY_CD` | DOUBLE | NOT NULL |  | The code value for the city. |
| 7 | `COUNTY` | VARCHAR(40) |  |  | Name of the county. |
| 8 | `COUNTY_CD` | DOUBLE | NOT NULL |  | Code value for the county. |
| 9 | `COUNTY_FIPS` | VARCHAR(5) |  |  | The FIPS county code is a five-digit Federal Information Processing Standard (FIPS) code (FIPS 6-4) which uniquely identifies counties and county equivalents in the United States, certain U.S. possessions, and certain freely associated states. The first two digits are the FIPS state code and the last three are the county code within the state or possession. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PREFERRED_TYPE` | VARCHAR(1) |  |  | The preferred type of zip code. |
| 12 | `PREFIX` | VARCHAR(10) |  |  | Phone number prefix. |
| 13 | `STATE` | VARCHAR(40) |  |  | Two letter abbreviation for a state. |
| 14 | `STATE_CD` | DOUBLE | NOT NULL |  | Code value for a state. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `ZIPCODE` | VARCHAR(10) |  |  | The postal code used to identify a geographical region. |
| 21 | `ZIP_DEFAULT_ID` | DOUBLE | NOT NULL |  | Primary key for this table. |
| 22 | `ZIP_PRIMARY_IND` | DOUBLE |  |  | Primary indicator. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

