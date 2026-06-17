# BR_DTA_LOINC

> Stores LOINC codes imported from files received from foreign systems.

**Description:** Bedrock Discrete Task Assay LOINC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_TXT` | VARCHAR(20) | NOT NULL |  | The activity type of the orderable (I.E. Lab) |
| 2 | `BR_DTA_LOINC_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a specific LOINC association. |
| 3 | `LOINC_TXT` | VARCHAR(20) | NOT NULL |  | The LOINC code associated with a foreign file system DTA. |
| 4 | `LONG_DTA_NAME` | VARCHAR(60) | NOT NULL |  | The long name of a foreign file system DTA. |
| 5 | `SHORT_DTA_NAME` | VARCHAR(40) | NOT NULL |  | The short name of a foreign file system DTA. |
| 6 | `SOURCE_IDENTIFIER_NAME` | VARCHAR(40) | NOT NULL |  | The name of the foreign file containing the DTA/LOINC associations. |
| 7 | `SPECIMEN_TYPE_TXT` | VARCHAR(40) | NOT NULL |  | Textual display of the specimen type associated with a LOINC code. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WIZARD_MEAN_TXT` | VARCHAR(100) | NOT NULL |  | Used to identify which build tool will be reading the rows on the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

