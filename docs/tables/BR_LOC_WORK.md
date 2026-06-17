# BR_LOC_WORK

> legacy locations

**Description:** BEDROCK LOCATION WORK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS1` | VARCHAR(100) |  |  | address of the location |
| 2 | `ADDRESS2` | VARCHAR(100) |  |  | optional second line for address |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `CITY` | VARCHAR(100) |  |  | city the facility is in |
| 5 | `COUNTRY_CD` | DOUBLE | NOT NULL |  | country the facility is in |
| 6 | `COUNTY_CD` | DOUBLE | NOT NULL |  | county the facility is in |
| 7 | `EXTENSION` | VARCHAR(100) |  |  | Telephone extension |
| 8 | `LOCATION_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 9 | `LOC_DISPLAY` | VARCHAR(50) |  |  | short name of the location |
| 10 | `NAME` | VARCHAR(60) |  |  | name of the location |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | identifies the organization the location is tied to |
| 12 | `OUTREACH_IND` | DOUBLE | NOT NULL |  | indicates if the facility is an outreach facility |
| 13 | `PHONE` | VARCHAR(50) |  |  | phone number of the facility |
| 14 | `PREFIX` | VARCHAR(6) |  |  | The location prefix. |
| 15 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 16 | `STATE_CD` | DOUBLE | NOT NULL |  | state the facility is in |
| 17 | `TYPE` | VARCHAR(30) |  |  | type of location |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `ZIP` | VARCHAR(25) |  |  | zip code of the facility |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

