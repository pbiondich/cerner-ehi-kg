# OMF_OUTCOME_INDICATOR

> Contains the list of indicators

**Description:** OMF_OUTCOME_INDICATOR  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME |  |  | date when we started using this indicator |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `INDICATOR_LONG_NAME` | VARCHAR(200) |  |  | This is the long description for this indicator |
| 4 | `INDICATOR_NBR` | DOUBLE | NOT NULL |  | This is the Cerner defined number for this indicator |
| 5 | `INDICATOR_SHORT_NAME` | CHAR(50) |  |  | Short description of the indicator |
| 6 | `JCAHO_MEASURE_NBR` | DOUBLE |  |  | jcaho oryx indicator number |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

