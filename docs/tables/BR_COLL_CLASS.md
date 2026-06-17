# BR_COLL_CLASS

> Bedrock data for collection classes

**Description:** BEDROCK COLLECTION CLASS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE` | VARCHAR(12) | NOT NULL |  | Activity type with which this collection class is associated, i.e. GLB |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Client identifier |
| 3 | `CODE_VALUE` | DOUBLE | NOT NULL |  | Actual code_value of the collection class on code set 231 |
| 4 | `COLLECTION_CLASS` | VARCHAR(20) | NOT NULL |  | Standard name of the collection class, i.e. Chemistry |
| 5 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | indicates that the defaults were selected |
| 6 | `DISPLAY_NAME` | VARCHAR(10) |  |  | Actual value of the display name on code set 231 |
| 7 | `FACILITY_ID` | DOUBLE | NOT NULL |  | ID for facility for which this collection class has been created |
| 8 | `PROPOSED_NAME_SUFFIX` | VARCHAR(6) |  |  | Short name to be concatenated to the facility prefix, i.e. CHEM |
| 9 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 10 | `STORAGE_TRACKING_IND` | DOUBLE | NOT NULL |  | Set to 1 to indicate that storage tracking is on, 0 for off |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

