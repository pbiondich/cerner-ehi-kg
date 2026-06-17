# BR_DEFAULT_PERSON_SEARCH

> default settings for person search filters and results

**Description:** Bedrock default person search  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_DEFAULT_PERSON_SEARCH_ID` | DOUBLE | NOT NULL |  | Unique id for the table |
| 3 | `DISPLAY` | VARCHAR(50) |  |  | name of filter or result |
| 4 | `EMPI_IND` | DOUBLE |  |  | indicator to determine the defaults that are used |
| 5 | `SEQUENCE` | DOUBLE |  |  | orders the display of the filters or results |
| 6 | `SETTING_MEAN` | VARCHAR(20) |  |  | meaning to link types of rows |
| 7 | `START_VERSION_NBR` | DOUBLE |  |  | Identifies which version of start has been loaded |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

