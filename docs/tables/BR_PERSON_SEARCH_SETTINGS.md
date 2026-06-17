# BR_PERSON_SEARCH_SETTINGS

> all available person search filters or results

**Description:** Bedrock Person Search Settings  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_PERSON_SEARCH_SETTINGS_ID` | DOUBLE | NOT NULL |  | Unique id |
| 3 | `CODESET` | DOUBLE |  |  | codeset number if linked to a code_value row |
| 4 | `DATA_TYPE_FLAG` | DOUBLE |  |  | number assigned to the type of filter or result |
| 5 | `DESCRIPTION` | VARCHAR(50) |  |  | name of filter or result |
| 6 | `DISPLAY` | VARCHAR(50) |  |  | name of filter or result |
| 7 | `MEANING` | VARCHAR(20) |  |  | cdf_meaning if linked to a code_value row |
| 8 | `SETTING_MEAN` | VARCHAR(20) |  |  | meaning to link types of rows |
| 9 | `START_VERSION_NBR` | DOUBLE |  |  | Identifies which version of start has been loaded |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

